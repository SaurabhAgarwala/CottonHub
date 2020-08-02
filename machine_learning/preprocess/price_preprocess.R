price_preprocess <- function(data)
{
    is_null <- function(i)
    {
        (is.na(i) | (i<=0))
    }
    
    ############################################################
    # Fill NA values
    ############################################################
    
    rem_idx <- c()
    
    null_min <- sapply(data$Min_Price, is_null)
    null_modal <- sapply(data$Modal_Price, is_null)
    null_max <- sapply(data$Max_Price, is_null)
    
    null_all <- null_min & null_modal & null_max
    rem_idx <- c(rem_idx, which(null_all))
    
    null_min_only <- null_min & !null_modal & !null_max
    for (idx in which(null_min_only))
    {
        repl_val <- 2 * data[idx, "Modal_Price"] - data[idx, "Max_Price"]
        if(repl_val <= 0)
            data[idx, "Min_Price"] <- data[idx, "Modal_Price"]
        else
            data[idx, "Min_Price"] <- repl_val
    }
    
    null_modal_only <- !null_min & null_modal & !null_max
    for (idx in which(null_modal_only))
        data[idx, "Modal_Price"] <- (data[idx, "Min_Price"] + data[idx, "Max_Price"]) / 2
    
    null_max_only <- !null_min & !null_modal & null_max
    for (idx in which(null_max_only))
        data[idx, "Max_Price"] <- 2 * data[idx, "Modal_Price"] - data[idx, "Min_Price"]
    
    null_min_modal <- null_min & null_modal & !null_max
    null_modal_max <- !null_min & null_modal & null_max
    null_min_max   <- null_min & !null_modal & null_max
    
    for (idx in which(null_min_modal))
    {
        repl_val <- data[idx, "Max_Price"]
        data[idx, "Min_Price"] <- repl_val
        data[idx, "Modal_Price"] <- repl_val
    }
    
    for (idx in which(null_modal_max))
    {
        repl_val <- data[idx, "Min_Price"]
        data[idx, "Modal_Price"] <- repl_val
        data[idx, "Max_Price"] <- repl_val
    }
    
    for (idx in which(null_min_max))
    {
        repl_val <- data[idx, "Modal_Price"]
        data[idx, "Min_Price"] <- repl_val
        data[idx, "Max_Price"] <- repl_val
    }
    
    if(length(rem_idx) != 0)
        data <- data[-rem_idx, ]
    rownames(data) <- 1:nrow(data)
    
    #par(mfrow = c(1, 1))
    #y_rng <- range(data$Min_Price, data$Modal_Price, data$Max_Price)
    #boxplot(log10(data$Min_Price), log10(data$Modal_Price), log10(data$Max_Price), ylab = "log10(Price)", main = "Min-Modal-Max Price Comparison")
    #axis(1, at = 1:3, labels = c("Min", "Modal", "Max"))
    #dev.off()
    
    ############################################################
    # Make logical checks
    ############################################################
    
    modal_lt_min <- data$Modal_Price < data$Min_Price
    for (idx in which(modal_lt_min))
    {
        temp <- data[idx, 'Modal_Price']
        data[idx, 'Modal_Price'] <- data[idx, 'Min_Price']
        data[idx, 'Min_Price'] <- temp
    }
    
    max_lt_modal <- data$Max_Price < data$Modal_Price
    for (idx in which(max_lt_modal))
    {
        temp <- data[idx, 'Max_Price']
        data[idx, 'Max_Price'] <- data[idx, 'Modal_Price']
        data[idx, 'Modal_Price'] <- temp
    }
    
    data
}