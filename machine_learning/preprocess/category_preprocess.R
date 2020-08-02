category_preprocess <- function(data, final_thresh = 2000)
{
    ############################################################
    # Filter out categories with less data than final_thresh
    ############################################################
    thresh <- seq(from = 0, to = 5000, by = 100)
    
    data <- transform(data, Category = paste(State, District, Market, Variety, sep = '_x_'))
    market_var_cnt_data <- table(data$Category)
    final_cats <- names(which(market_var_cnt_data > final_thresh))
    #market_var_num_cats <- sapply(thresh, function(i) { length(which(market_var_cnt_data$Count >= i)) })
    
    #distr_var_cnt_data <- aggregate(data[, 'Modal_Price'], list(data$District, data$Variety), length)
    #colnames(distr_var_cnt_data) <- c('District', 'Variety', 'Count')
    #distr_var_num_cats <- sapply(thresh, function(i) { length(which(distr_var_cnt_data$Count >= i)) })
    
    #market_cnt_data <- aggregate(data[, 'Modal_Price'], list(data$Market), length)
    #colnames(market_cnt_data) <- c('Market', 'Count')
    #market_num_cats <- sapply(thresh, function(i) { length(which(market_cnt_data$Count >= i)) })
    
    #distr_cnt_data <- aggregate(data[, 'Modal_Price'], list(data$District), length)
    #colnames(distr_cnt_data) <- c('District', 'Count')
    #distr_num_cats <- sapply(thresh, function(i) { length(which(distr_cnt_data$Count >= i)) })
    
    #par(mfrow = c(1, 1))
    #plot(0, xlab = "Threshold", ylab = 'No. of Categories', main = "Determining no. of categories", type = 'n', xlim = range(thresh), ylim = c(0, 500))
    #points(x = thresh, y = market_var_num_cats, col = 'red', type = 'l', lwd = 2)
    #points(x = thresh, y = distr_var_num_cats, col = 'blue', type = 'l', lwd = 2)
    #points(x = thresh, y = market_num_cats, col = 'green', type = 'l', lwd = 2)
    #points(x = thresh, y = distr_num_cats, col = 'magenta', type = 'l', lwd = 2)
    #legend('topright', col = c('red', 'blue', 'green', 'magenta'), legend = c("Market+Variety", "District+Variety", "Market", "District"), lwd = 2, title = " Grouping", title.adj = 0.1)
    #dev.off()
    
    data <- subset(data, Category %in% final_cats)
    data <- aggregate(data[, c('Min_Price', 'Modal_Price', 'Max_Price')], list(data$Category, data$Date), mean)
    colnames(data) <- c("Category", "Date", 'Min_Price', "Modal_Price", 'Max_Price')
    print(paste("No. of Categories with threshold ", final_thresh, " : ", length(final_cats), sep = ''))
    
    #final_state_distr <- table(data$State)
    #final_variety_distr <- table(data$Variety)
    #cols <- colorRampPalette(c('red', 'green', 'cyan', 'magenta'))
    #state_cols <- cols(length(final_state_distr))
    #variety_cols <- cols(length(final_variety_distr))
    
    #par(mfrow = c(2, 1), mar = c(2, 1, 2, 1))
    #pie(final_state_distr, col = state_cols, main = "State Distribution in Final Data", radius = 1)
    #pie(final_variety_distr, col = variety_cols, main = "Variety Distribution in Final Data", radius = 1)
    #dev.off()
    
    data
}
