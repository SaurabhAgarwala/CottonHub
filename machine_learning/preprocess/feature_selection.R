feature_selection <- function(data, k = 100, day_num = 1)
{
    tsfresh_feat_names <- readLines(paste('./data/Training_Data/Tsfresh_Features/day_', day_num, '.txt', sep = ''))
    tsfresh_diff_feat_names <- readLines(paste('./data/Training_Data/Tsfresh_Diff_Features/day_', day_num, '.txt', sep = ''))
    
    data['Prev_Modal_Price'] <- data[paste('day_', day_num, sep = '')]
    non_feat_cols <- c(
        "ID", "State", "District", "Market", "Variety", "Date", "Min_Price", "Modal_Price",
        "Max_Price", "Category", "Modal_Price_Diff", "Prev_Modal_Price")
    
    ############################################################
    # Scaling Features
    ############################################################
    for (col in colnames(data))
    {
        if(!(col %in% non_feat_cols))
            data[, col] <- scale(data[, col])
    }
    ############################################################
    
    #corrs <- list()
    #corrs_diff <- list()
    #for (col in colnames(data))
    #{
    #    if(!(col %in% non_feat_cols))
    #    {
    #        col_corr <- abs(cor(data[, col], data[, 'Modal_Price']))
    #        corrs[col] <- col_corr
    #        col_corr_diff <- abs(cor(data[, col], data[, 'Modal_Price_Diff']))
    #        corrs_diff[col] <- col_corr_diff
    #    }
    #}
    #corrs <- list(sort(unlist(corrs), decreasing = TRUE))[[1]]
    #corrs_diff <- list(sort(unlist(corrs_diff), decreasing = TRUE))[[1]]
    
    #col_type_names <- c("tsfresh_daydiff_", "tsfresh_day_", "day_", "daydiff_", "date_")
    #col_type_cols <- c("yellow", 'black', 'red', 'blue', 'green')
    
    #col_type <- c()
    #for (col in names(corrs))
    #{
    #    for (col_type_ind in seq_along(col_type_names))
    #    {
    #        if(grepl(col_type_names[col_type_ind], col))
    #        {
    #            col_type <- c(col_type, col_type_cols[col_type_ind])
    #            break
    #        }
    #    }
    #}
    
    #col_type_diff <- c()
    #for (col in names(corrs_diff))
    #{
    #    for (col_type_ind in seq_along(col_type_names))
    #    {
    #        if(grepl(col_type_names[col_type_ind], col))
    #        {
    #            col_type_diff <- c(col_type_diff, col_type_cols[col_type_ind])
    #            break
    #        }
    #    }
    #}
    
    #par(mfrow = c(2, 1), xaxt = 'n')
    #barplot(corrs, col = col_type, main = "Correlation with Price", ylab = 'Correlation', xlab = 'Features')
    #legend('topright', legend = col_type_names, col = col_type_cols, lwd = 1)
    #barplot(corrs_diff, col = col_type_diff, main = "Correlation with Price Diff", ylab = 'Correlation', xlab = 'Features')
    #legend('topright', legend = col_type_names, col = col_type_cols, lwd = 1)
    #dev.off()
    
    #print("Best Columns for Price:")
    #best_cols <- names(corrs)[1:10]
    #for (col in best_cols)
    #{
    #    if(grepl('tsfresh_day_', col))
    #    {
    #        tsfresh_feat_num <- as.numeric(strsplit(c(col), '_')[[1]][3])
    #        print(paste(tsfresh_feat_names[tsfresh_feat_num], col, sep = '___'))
    #    }
    #    else if(grepl('tsfresh_daydiff_', col))
    #    {
    #        tsfresh_feat_num <- as.numeric(strsplit(c(col), '_')[[1]][3])
    #        print(paste(tsfresh_diff_feat_names[tsfresh_feat_num], col, sep = '___'))
    #    }
    #    else
    #        print(col)
    #}
    
    #print("Best Columns for Diff:")
    #best_cols <- names(corrs_diff)[1:10]
    #for (col in best_cols)
    #{
    #    if(grepl('tsfresh_day_', col))
    #    {
    #        tsfresh_feat_num <- as.numeric(strsplit(c(col), '_')[[1]][3])
    #        print(paste(tsfresh_feat_names[tsfresh_feat_num], '(', col, ')'))
    #    }
    #    else if(grepl('tsfresh_daydiff_', col))
    #    {
    #        tsfresh_feat_num <- as.numeric(strsplit(c(col), '_')[[1]][3])
    #        print(paste(tsfresh_diff_feat_names[tsfresh_feat_num], '(', col, ')'))
    #    }
    #    else
    #        print(col)
    #}
    
    train_data <- data[, !(colnames(data) %in% non_feat_cols)]
    #orig_cols <- colnames(train_data)
    train_data <- as.matrix(train_data)
    
    #dist_col <- dist(t(train_data))
    #hcl = hclust(dist_col)
    
    #col_type_names <- c("tsfresh_daydiff_", "tsfresh_day_", "tsfresh_day_", "day_", "daydiff_", "date_")
    #col_type_thresh <- c(0, 0.5, 0, 0, 0, 0)
    #col_type_cols <- c("yellow", 'black', 'red', 'blue', 'green', 'cyan')
    #col_type <- c()
    #for (col in colnames(train_data))
    #{
    #    for (col_type_ind in seq_along(col_type_names))
    #    {
    #        if(grepl(col_type_names[col_type_ind], col))
    #        {
    #            if(corrs[col] > col_type_thresh[col_type_ind])
    #            {
    #                col_type <- c(col_type, col_type_cols[col_type_ind])
    #                break
    #            }
    #        }
    #    }
    #}
    
    #library(rafalib)
    #par(mfrow = c(1, 1))
    #myplclust(hcl, lab.col = col_type)
    #legend('topright', legend = paste(col_type_names, col_type_thresh, sep = ' > '), col = col_type_cols, pch = 19)
    #dev.off()
    
    #inter_corr <- abs(cor(train_data))
    #heatmap(inter_corr, symm = TRUE, ColSideColors = col_type, RowSideColors = col_type)
    #legend('topleft', legend = paste(col_type_names, col_type_thresh, sep = ' > '), col = col_type_cols, pch = 19, cex = 0.8)
    #dev.off()
    
    ############################################################
    # Singular Value Decomposition
    ############################################################
    
    #sel_cols <- colnames(train_data)
    #sel_data <- train_data[, sel_cols]
    #s <- svd(sel_data)
    
    #par(mfrow = c(1, 1), xaxt = 's')
    #plot(x = 1:length(s$d), y = cumsum((s$d ^ 2) / sum(s$d ^ 2) * 100), main = "SVD Information Retention", ylab = 'Percentege Retention (%)', xlab = 'No. of Feature')
    #dev.off()
    
    #new_data <- s$u[, 1:k] %*% diag(s$d[1:k])
    #new_data <- as.data.frame(new_data)
    ############################################################
    
    ############################################################
    # Extracting only n-day features
    ############################################################

    #sel_cols <- colnames(train_data)[grepl("^day_", colnames(train_data))]
    #new_data <- subset(train_data, select = sel_cols)
    #sel_cols <- colnames(train_data)[grepl("^daydiff_", colnames(train_data))]
    #new_data <- subset(train_data, select = sel_cols)
    ############################################################
    
    ############################################################
    # Using all features
    ############################################################
    
    new_data <- as.data.frame(train_data)
    ############################################################

    ############################################################
    # Final Merge
    ############################################################
    
    colnames(new_data) <- sapply(seq(ncol(new_data)), function(i) {paste('feat', i, sep = '_')})
    #colnames(new_data) <- orig_cols
    data <- subset(data, select = non_feat_cols)
    data <- cbind(data, new_data)
    ############################################################
    
    ############################################################
    # Final Scaling
    ############################################################

    #for (col in colnames(data))
    #{
    #    if(!(col %in% non_feat_cols))
    #        data[, col] <- scale(data[, col])
    #}
    ############################################################
    
    data
}

for (day_num in seq(7))
{
    print(paste("Selecting features for day ", day_num, sep = ''))
    data <- read.csv(paste("./data/Training_Data/day_", day_num, ".csv", sep = ''))
    data$Date <- as.Date(data$Date, format = "%d/%m/%Y")
    str_cols = c("State", "District", "Market", "Variety")
    for (str_col in str_cols)
        data[, str_col] <- as.character(data[, str_col])
    
    # Total no. of features when using SVD
    k = 100
    
    new_data <- feature_selection(data, k = k, day_num = day_num)
    
    new_data[, "Date"] <- as.factor(strftime(new_data[, "Date"], format = "%d/%m/%Y"))
    factor_cols <- c("State", "District", "Market", "Variety")
    for (col in factor_cols)
        new_data[, col] <- as.factor(as.character(new_data[, col]))
    write.csv(new_data, paste("./data/Training_Data/final_", day_num, ".csv", sep = ''), row.names = FALSE)
}