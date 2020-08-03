TS_trainable_data_preprocess <- function(data, diff_thresh = 200)
{
    cats <- as.character(unique(data$Category))
    #par(mfrow = c(1, 1), mar = c(4, 11, 2, 1), cex.axis = 0.75)
    #plot(x = data$Date, y = rep(0, dim(data)[1]), type = 'n', ylim = c(1, length(cats)), ylab = '', xlab = '', yaxt = 'n')
    #title(main = "Category-wise Data Distribution across Dates", xlab = "Date", ylab = " ")
    #for (cat_idx in seq_along(cats))
    #{
    #    cat_data <- subset(data, Category == cats[cat_idx])
    #    points(x = cat_data$Date, y = rep(cat_idx, dim(cat_data)[1]), pch = 16, col = rgb(0, 0, 0, alpha = 0.25), cex = 0.5)
    #}
    #axis(side = 2, labels = NA, at = 1:length(cats))
    #axis(side = 2, lwd = 0, line = -.4, las = 1, at = 1:length(cats), labels = cats)
    #dev.off()
    
    ############################################################
    # Remove categories which do not have 'latest' prices
    ############################################################
    
    library(sys)
    today <- Sys.Date()
    diff_days <- c()
    for (cat in cats)
    {
        cat_data <- subset(data, Category == cat)
        diff_days <- c(diff_days, difftime(today, max(cat_data$Date), units = 'days')[[1]])
    }
    
    #par(mfrow = c(1, 1))
    #hist(diff_days, breaks = 100, main = "Histogram of Difference between Latest Day and Today", xlab = "Difference (in Days)")
    #abline(v = diff_thresh, col = 'red')
    #dev.off()
    
    rm_cat <- cats[which(diff_days > diff_thresh)]
    data <- subset(data, !(Category %in% rm_cat))
    rownames(data) <- 1:nrow(data)
    
    ############################################################
    # Consider all data points for a category
    # Impute all missing values later to make it continuous
    ############################################################
    
    cats <- as.character(unique(data$Category))
    
    ndays_data <- list()
    max_date <- Sys.Date() - 1
    for (cat_idx in seq_along(cats))
    {
        cat_data <- subset(data, Category == cats[cat_idx])
        cat_data <- cat_data[order(cat_data$Date), ]
        rownames(cat_data) <- 1:nrow(cat_data)
        
        available_dates <- unique(cat_data$Date)
        min_date <- min(cat_data$Date)
        tot_days <- difftime(max_date, min_date, units = 'days')[[1]]
        ndays <- c()
        for (i in seq(from = 0, to = tot_days - 1))
        {
            sel_date <- min_date + i
            if(sel_date %in% available_dates)
                ndays <- c(ndays, cat_data[cat_data$Date == sel_date, 'Modal_Price'])
            else
                ndays <- c(ndays, -1)
        }
        # Assuming yesterday's price as the latest price
        repl_val <- mean(rev(ndays[which(ndays != -1)])[1:10])
        ndays <- c(ndays, repl_val)
        ndays_data[[cat_idx]] <- rev(ndays)
    }
    max_cnt <- max(sapply(seq_along(cats), function(i) {length(ndays_data[[i]])}))
    for (idx in seq_along(cats))
        length(ndays_data[[idx]]) <- max_cnt
    ndays_df <- matrix(nrow = length(cats), ncol = max_cnt)
    for (i in seq_along(cats))
        ndays_df[i, 1:max_cnt] <- unlist(ndays_data[[i]])
    
    df_cols <- sapply(seq(ncol(ndays_df)), function(i) { paste("day", i, sep = '_') })
    ndays_df <- as.data.frame(ndays_df)
    colnames(ndays_df) <- df_cols
    rownames(ndays_df) <- 1:nrow(ndays_df)
    ndays_df$Category <- cats
    ndays_df$Today <- rep(c(max_date + 1), nrow(ndays_df))
    data <- merge(ndays_df, unique(data[c('State', 'District', 'Market', 'Variety', 'Category')]), by = 'Category')
    rownames(data) <- 1:nrow(data)
    
    #cats <- as.character(unique(data$Category))
    #par(mfrow = c(1, 1), mar = c(4, 11, 2, 1), cex.axis = 0.75)
    #plot(x = data$Date, y = rep(0, dim(data)[1]), type = 'n', ylim = c(1, length(cats)), ylab = '', xlab = '', yaxt = 'n')
    #title(main = "Category-wise Data Distribution across Dates", xlab = "Date", ylab = " ")
    #for (cat_idx in seq_along(cats))
    #{
    #    cat_data <- subset(data, Category == cats[cat_idx])
    #    points(x = cat_data$Date, y = rep(cat_idx, dim(cat_data)[1]), pch = 16, col = rgb(0, 0, 0, alpha = 0.25), cex = 0.5)
    #}
    #axis(side = 2, labels = NA, at = 1:length(cats))
    #axis(side = 2, lwd = 0, line = -.4, las = 1, at = 1:length(cats), labels = cats)
    #dev.off()
    
    data
}
