data <- read.csv("./data/Prices.csv")
data <- subset(data, select = -Commodity)

data$Date <- as.Date(data$Date, format = "%d/%m/%Y")
str_cols = c("State", "District", "Market", "Variety")
for (str_col in str_cols)
    data[, str_col] <- as.character(data[, str_col])

# Minimum no. of data points initially required
final_cat_thresh <- 1000

# No. of previous prices considered
n <- 15

# Maximum no. of NAs in previous prices
na_thresh <- 7

# Maximum no. of consecutive NAs
consec_thresh <- 5

# Maximum no. of days between today & latest date in data
diff_thresh <- 365

source('./preprocess/state_distr_market_preprocess.R')
source('./preprocess/price_preprocess.R')
source('./preprocess/variety_preprocess.R')
source('./preprocess/category_preprocess.R')
source('./preprocess/trainable_data_preprocess.R')
source('./preprocess/outlier_preprocess.R')
source('./preprocess/NA_preprocess.R')
source('./preprocess/add_todays_data.R')

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
#new_data <- trainable_data_preprocess(new_data, n = n, na_thresh = na_thresh, consec_thresh = consec_thresh, diff_thresh = diff_thresh)
#new_data <- NA_preprocess(new_data, n = n)
#new_data <- add_todays_data(new_data)

new_data[, "Date"] <- as.factor(strftime(new_data[, "Date"], format = "%d/%m/%Y"))
factor_cols <- c("State", "District", "Market", "Variety")
for (col in factor_cols)
    new_data[, col] <- as.factor(as.character(new_data[, col]))
write.csv(new_data, "./data/Preprocessed_Data/Temp_Prices.csv", row.names = FALSE)
