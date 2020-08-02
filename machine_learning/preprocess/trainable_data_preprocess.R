trainable_data_preprocess <- function(data, n = 15, na_thresh = 7, consec_thresh = 5, diff_thresh = 200, cat_thresh = 200)
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
    # Remove data points having a lot of missing past data
    ############################################################
    # n             ->  No. of previous prices to consider
    # na_thresh     ->  Maximum no. of NAs in previous prices
    # consec_thresh ->  Maximum no. of consecutive NAs
    ############################################################
    
    rm_id <- c()
    cats <- as.character(unique(data$Category))
    for (cat in cats)
    {
        cat_data <- subset(data, Category == cat)
        cat_data <- cat_data[order(cat_data$Date), ]
        rownames(cat_data) <- 1:nrow(cat_data)
        
        rm_id <- c(rm_id, as.character(cat_data[1:n, 'ID']))
        for (i in seq(from = n+1, to = nrow(cat_data)))
        {
            # Calculating no. of dates out of n dates with prices available
            diff_days <- difftime(cat_data[i, 'Date'], cat_data[i-n+na_thresh, 'Date'], units = 'days')[[1]]
            if(diff_days > n)
                rm_id <- c(rm_id, as.character(cat_data[i, 'ID']))
        }
    }
    rm_id <- as.vector(rm_id)
    
    ndays_data <- c()
    ids_data <- c()
    for (cat in cats)
    {
        cat_data <- subset(data, Category == cat)
        cat_data <- cat_data[order(cat_data$Date), ]
        rownames(cat_data) <- 1:nrow(cat_data)
        
        valid_cat_data <- subset(cat_data, !(ID %in% rm_id))
        if(nrow(valid_cat_data) == 0)
            next
        rownames(valid_cat_data) <- 1:nrow(valid_cat_data)
        
        available_dates <- unique(cat_data$Date)
        for (i in seq(nrow(valid_cat_data)))
        {
            ndays <- c()
            consec_cnt <- 0
            current_date <- valid_cat_data[i, 'Date']
            for (j in seq(n))
            {
                past_date <- current_date - j
                if(past_date %in% available_dates)
                {
                    consec_cnt <- 0
                    ndays <- c(ndays, cat_data[cat_data$Date == past_date, 'Modal_Price'])
                }
                else
                {
                    consec_cnt <- consec_cnt + 1
                    # Checking for exceeding consecutive NAs or if the first or last price is NA
                    if((consec_cnt == consec_thresh) | (j == 1) | (j == n))
                    {
                        consec_cnt <- consec_thresh
                        break
                    }
                    ndays <- c(ndays, NA)
                }
            }
            
            if(consec_cnt != consec_thresh)
            {
                ndays_data <- c(ndays_data, ndays)
                ids_data <- c(ids_data, as.character(valid_cat_data[i, 'ID']))
            }
        }
    }
    
    ndays_data <- as.matrix(ndays_data)
    dim(ndays_data) <- c(n, length(ndays_data)/n)
    ndays_data <- t(ndays_data)
    
    df_cols <- sapply(seq(n), function(i) { paste("day", i, sep = '_') })
    ndays_df <- data.frame(ndays_data)
    colnames(ndays_df) <- df_cols
    rownames(ndays_df) <- 1:nrow(ndays_df)
    ndays_df$ID <- ids_data
    data <- merge(data, ndays_df, by = 'ID')
    
    ############################################################
    # Again remove categories which do not have 'latest' prices
    ############################################################
    
    today <- Sys.Date()
    diff_days <- c()
    for (cat in cats)
    {
        cat_data <- subset(data, Category == cat)
        diff_days <- c(diff_days, difftime(today, max(cat_data$Date), units = 'days')[[1]])
    }
    
    #par(mfrow = c(1, 1))
    #hist(diff_days, breaks = 100, main = "Updated Histogram of Difference between Latest Day and Today", xlab = "Difference (in Days)")
    #abline(v = diff_thresh, col = 'red')
    #dev.off()
    
    rm_cat <- cats[which(diff_days > diff_thresh)]
    data <- subset(data, !(Category %in% rm_cat))
    rownames(data) <- 1:nrow(data)
    
    cats <- as.character(unique(data$Category))
    for (cat in cats)
    {
        cat_data <- subset(data, Category == cat)
        if(nrow(cat_data) < cat_thresh)
            data <- subset(data, Category != cat)
    }
    rownames(data) <- 1:nrow(data)
    print(paste("Final No. of Categories: ", length(unique(data$Category))))
    
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