data <- read.csv("./data/Prices.csv")
data <- subset(data, select = -Commodity)

data$Date <- as.Date(data$Date, format = "%d/%m/%Y")
str_cols = c("State", "District", "Market", "Variety")
for (str_col in str_cols)
    data[, str_col] <- as.character(data[, str_col])

# Minimum no. of data points initially required
final_cat_thresh <- 1000

# Maximum no. of days between today & latest date in data
diff_thresh <- 365

source('./preprocess/state_distr_market_preprocess.R')
source('./preprocess/price_preprocess.R')
source('./preprocess/variety_preprocess.R')
source('./preprocess/category_preprocess.R')
source('./preprocess/TS_trainable_data_preprocess.R')
source('./preprocess/outlier_preprocess.R')
source('./preprocess/TS_NA_preprocess.R')
source('./preprocess/TS_squeeze_data.R')

new_data <- data
new_data <- state_distr_market_preprocess(new_data)
new_data <- variety_preprocess(new_data)
new_data <- category_preprocess(new_data, final_thresh = final_cat_thresh)
new_data$State <- sapply(as.character(new_data$Category), function(i) { strsplit(i, split = '_x_')[[1]][1] })
new_data$District <- sapply(as.character(new_data$Category), function(i) { strsplit(i, split = '_x_')[[1]][2] })
new_data$Market <- sapply(as.character(new_data$Category), function(i) { strsplit(i, split = '_x_')[[1]][3] })
new_data$Variety <- sapply(as.character(new_data$Category), function(i) { strsplit(i, split = '_x_')[[1]][4] })
new_data <- transform(new_data, Category = paste(Market, Variety, sep = '_x_'))
new_data <- price_preprocess(new_data)
price_cols <- c("Modal_Price")
for (col in price_cols)
    new_data <- outlier_preprocess(new_data, sel_col = col)
new_data <- price_preprocess(new_data)
new_data <- TS_trainable_data_preprocess(new_data, diff_thresh = diff_thresh)

daily_data <- TS_squeeze_data(new_data, 1)
daily_data <- TS_NA_preprocess(daily_data)
weekly_data <- TS_squeeze_data(new_data, 7)
weekly_data <- TS_NA_preprocess(weekly_data)
monthly_data <- TS_squeeze_data(new_data, 30)
monthly_data <- TS_NA_preprocess(monthly_data)

daily_data[, "Today"] <- as.factor(strftime(daily_data[, "Today"], format = "%d/%m/%Y"))
factor_cols <- c("State", "District", "Market", "Variety")
for (col in factor_cols)
    weekly_data[, col] <- as.factor(as.character(weekly_data[, col]))
write.csv(daily_data, "./data/Preprocessed_Data/TS_Preprocessed_Daily_Prices.csv", row.names = FALSE)

weekly_data[, "Today"] <- as.factor(strftime(weekly_data[, "Today"], format = "%d/%m/%Y"))
factor_cols <- c("State", "District", "Market", "Variety")
for (col in factor_cols)
    weekly_data[, col] <- as.factor(as.character(weekly_data[, col]))
write.csv(weekly_data, "./data/Preprocessed_Data/TS_Preprocessed_Weekly_Prices.csv", row.names = FALSE)

monthly_data[, "Today"] <- as.factor(strftime(monthly_data[, "Today"], format = "%d/%m/%Y"))
factor_cols <- c("State", "District", "Market", "Variety")
for (col in factor_cols)
    monthly_data[, col] <- as.factor(as.character(monthly_data[, col]))
write.csv(monthly_data, "./data/Preprocessed_Data/TS_Preprocessed_Monthly_Prices.csv", row.names = FALSE)
