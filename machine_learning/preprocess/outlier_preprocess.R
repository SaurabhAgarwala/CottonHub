outlier_preprocess <- function(data, sel_col = 'Modal_Price')
{
    data <- transform(data, ID = paste(Category, Date, sep = '_x_'))
    
    close_to_zero <- function(vals)
    {
        abs_vals <- abs(vals)
        return(vals[which.min(abs_vals)])
    }
    
    cats <- unique(data$Category)
    ids_data <- c()
    diff_data <- c()
    double_diff_data <- c()
    days_data <- c()
    for (cat in cats)
    {
        cat_data <- subset(data, Category == cat)
        cat_data <- cat_data[order(cat_data$Date), ]
        
        ids_data <- c(ids_data, as.character(cat_data[, 'ID']))
        
        cat_price_diff <- diff(cat_data[, sel_col])
        cat_price_diff <- c(mean(cat_price_diff), cat_price_diff)
        cat_date_diff <- diff(cat_data$Date)
        cat_date_diff <- sapply(seq(length(cat_date_diff)), function(i) { cat_date_diff[[i]] })
        cat_date_diff <- c(mean(cat_date_diff), cat_date_diff)
        
        cat_diff <- cat_price_diff / cat_date_diff
        diff_data <- c(diff_data, cat_diff)
        
        cat_double_diff <- -diff(cat_diff)
        cat_double_diff <- c(cat_double_diff, mean(cat_double_diff))
        padded_cat_double_diff <- c(0, cat_double_diff, 0)
        conv1_cat_double_diff <- convolve(padded_cat_double_diff, c(-5, 0, 0), type = 'filter')
        conv2_cat_double_diff <- convolve(padded_cat_double_diff, c(0, 0, -5), type = 'filter')
        cat_double_diff <- sapply(seq(length(cat_double_diff)), function(i) {close_to_zero(c(cat_double_diff[i], conv1_cat_double_diff[i], conv2_cat_double_diff[i]))})
        double_diff_data <- c(double_diff_data, cat_double_diff)
        
        days_data <- c(days_data, cat_date_diff)
    }
    
    diff_df <- data.frame(ids_data)
    diff_df$Diff <- diff_data
    diff_df$Double_Diff <- double_diff_data
    diff_df$Days_Gap <- days_data
    colnames(diff_df) <- c("ID", "Diff", "Double_Diff", "Days_Gap")
    data <- merge(data, diff_df, by = 'ID')
    
    cat_mean <- tapply(data$Double_Diff, data$Category, mean)
    cat_var <- tapply(data$Double_Diff, data$Category, var)
    z_scores <- vector(mode = 'numeric', length = nrow(data))
    for (ind in seq(nrow(data)))
    {
        cat <- data[ind, 'Category']
        double_diff <- data[ind, 'Double_Diff']
        z <- (double_diff - cat_mean[cat][[1]]) / sqrt(cat_var[cat][[1]])
        z_scores[ind] <- z
    }
    data$Z_Score <- z_scores
    
    is_outlier <- vector(mode = 'logical', length = nrow(data))
    z_thresh <- 10
    for (ind in seq(nrow(data)))
    {
        z <- data[ind, 'Z_Score']
        if(abs(z) > z_thresh)
            is_outlier[ind] <- TRUE
        else
            is_outlier[ind] <- FALSE
    }
    data$Outlier <- is_outlier
    
    data$Mod_Price <- vector(mode = 'numeric', length = nrow(data))
    for (ind in seq(nrow(data)))
    {
        if(data[ind, 'Outlier'] == TRUE)
        {
            req_diff <- 0
            req_price <- data[ind, sel_col] + data[ind, 'Days_Gap'] * (req_diff - data[ind, 'Diff'])
            data[ind, 'Mod_Price'] <- req_price
        }
        else
            data[ind, 'Mod_Price'] <- data[ind, sel_col]
    }
    
    #par(mfrow = c(5, 1))
    #cat_ind <- 1
    #cats <- unique(data$Category)
    # Loop Start
    #cat_data <- subset(data, Category == cats[cat_ind])
    #cat_ind <- cat_ind + 1
    #rownames(cat_data) <- 1:nrow(cat_data)
    #plot(cat_data$Date, cat_data[, sel_col], type = 'l')
    #plot(cat_data$Date, cat_data[, sel_col], type = 'l')
    #for (ind in seq(nrow(cat_data)))
    #{
    #    if(cat_data[ind, 'Outlier'] == TRUE)
    #        abline(v = cat_data[ind, 'Date'], col = 'red')
    #}
    #plot(cat_data$Date, cat_data$Mod_Price, type = 'l')
    #plot(cat_data$Date, cat_data$Diff, type = 'l')
    #plot(cat_data$Date, cat_data$Double_Diff, type = 'l')
    # Loop Stop
    
    data[, sel_col] <- data[, 'Mod_Price']
    data$Mod_Price <- NULL
    data$Diff <- NULL
    data$Double_Diff <- NULL
    data$Days_Gap <- NULL
    data$Z_Score <- NULL
    data$Outlier <- NULL
    
    data
}