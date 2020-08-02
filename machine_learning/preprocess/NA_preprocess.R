NA_preprocess <- function(data, n = 15)
{
    day_cols <- sapply(seq(n), function(i) {paste('day', i, sep = '_')})
    
    #par(mfrow = c(1, 1), las = 2)
    #na_cols <- sapply(day_cols, function(i) {sum(is.na(data[, i]))})
    #barplot(na_cols)
    #title(main = 'Barplot of missing features')
    #dev.off()
    
    for (idx in seq(nrow(data)))
    {
        start_ind <- 0
        start_val <- 0
        stop_ind <- 0
        stop_val <- 0
        na_cnt <- 0
        for (col_ind in seq_along(day_cols))
        {
            val <- data[idx, day_cols[col_ind]][[1]]
            if(is.na(val) == TRUE)
                na_cnt <- na_cnt + 1
            else if((is.na(val) == FALSE) & (na_cnt == 0))
            {
                start_ind <- col_ind
                start_val <- val
            }
            else
            {
                stop_ind <- col_ind
                stop_val <- val
                
                interp <- approx(x = c(start_ind, stop_ind), y = c(start_val, stop_val), n = na_cnt + 2)
                for (interp_ind in seq(from = 2, to = na_cnt + 1))
                    data[idx, day_cols[interp$x[interp_ind]]] <- interp$y[interp_ind]
                
                na_cnt <- 0
                start_ind <- col_ind
                start_val <- val
            }
        }
    }
    
    #day_cols_corr <- sapply(day_cols, function(i) {cor(data[, i], data$Modal_Price)})
    #par(mfrow = c(1, 1), las = 2)
    #barplot(day_cols_corr)
    #title(main = 'Correlation of features with target')
    #dev.off()
    
    data
}