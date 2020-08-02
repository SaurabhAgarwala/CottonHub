TS_squeeze_data <- function(data, squeeze_factor)
{
    day_cols <- colnames(data)[which(sapply(colnames(data), function(i) {grepl("^day_", i)}))]
    
    squeezed_ncol <- length(day_cols) %/% squeeze_factor
    squeezed_matrix <- matrix(nrow = nrow(data), ncol = squeezed_ncol)
    cats <- data$Category
    for (cat_idx in seq_along(cats))
    {
        cat_vals <- as.numeric(subset(data, Category == cats[cat_idx])[day_cols])
        for (squeeze_idx in seq(squeezed_ncol))
        {
            sel_vals <- cat_vals[((squeeze_idx - 1) * squeeze_factor + 1): (squeeze_idx * squeeze_factor)]
            na_cnt <- sum(is.na(sel_vals))
            if(na_cnt != 0)
                break
            avail_vals <- sel_vals[which(sel_vals != -1)]
            if(length(avail_vals) == 0)
                squeezed_matrix[cat_idx, squeeze_idx] <- -1
            else
                squeezed_matrix[cat_idx, squeeze_idx] <- mean(avail_vals)
        }
    }
    squeezed_df <- as.data.frame(squeezed_matrix)
    colnames(squeezed_df) <- sapply(seq(squeezed_ncol), function(i) {paste('group', squeeze_factor, i, sep = '_')})
    rownames(squeezed_df) <- 1:nrow(squeezed_df)
    squeezed_df$Category <- data$Category
    squeezed_df$State <- data$State
    squeezed_df$District <- data$District
    squeezed_df$Market <- data$Market
    squeezed_df$Variety <- data$Variety
    squeezed_df$Today <- data$Today
    
    squeezed_df
}