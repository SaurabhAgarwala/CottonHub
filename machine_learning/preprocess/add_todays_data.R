add_todays_data <- function(data)
{
    library(sys)
    todays_date <- Sys.Date()
    cats <- unique(data$Category)
    data$Forecast_Num <- rep(0, nrow(data))
    
    for (cat in cats)
    {
        cat_max_date <- max(subset(data, Category == cat)[, 'Date'])
        duplicate_row <- data[(data$Date == cat_max_date) & (data$Category == cat), ]
        for (forecast_num in seq(7))
        {
            duplicate_idx <- nrow(data) + 1
            data[duplicate_idx, ] <- duplicate_row
            data[duplicate_idx, 'Date'] <- todays_date + forecast_num - 1
            for (i in seq(15 - forecast_num))
                data[duplicate_idx, paste('day', 15-i+1, sep = '_')] <- data[duplicate_idx, paste('day', 15-i+1-forecast_num, sep = '_')]
            data[duplicate_idx, paste('day', forecast_num, sep = '_')] <- data[duplicate_idx, 'Modal_Price']
            data[duplicate_idx, 'Forecast_Num'] <- forecast_num
        }
    }
    data <- transform(data, ID = paste(Category, Date, sep = '_x_'))
    data <- data[order(data$ID), ]
    
    data
}
