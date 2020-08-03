data <- read.csv('./data/Preprocessed_Data/Temp_Prices.csv')
source('./preprocess/plot_district_map.R')
source('./preprocess/plot_map.R')

save_heatmap <- function(state, year)
{
    png(filename = paste(paste('./heatmaps/heatmap', state, year, sep = '_'), '.png', sep = ''))
    if(state != 'National')
    {
        sel_data <- data[grepl(year, data$Date), ]
        print(dim(sel_data))
        distr_vals <- aggregate(sel_data$Modal_Price, by = list(sel_data$District), FUN = mean)
        distr <- distr_vals$Group.1
        distr_vals <- distr_vals$x
        names(distr_vals) <- distr
        plot_distr_map(distr_vals, state, coords = state_coord[state][[1]], title = paste(state, year, sep = ' - '), bins = 100, cols = c('#463F3A', '#B7FE63'))
    }
    if(state == 'National')
    {
        sel_data <- data[grepl(year, data$Date), ]
        print(dim(sel_data))
        distr_vals <- aggregate(sel_data$Modal_Price, by = list(sel_data$State), FUN = mean)
        distr <- distr_vals$Group.1
        distr_vals <- distr_vals$x
        names(distr_vals) <- distr
        plot_map(distr_vals, title = paste(state, year, sep = ' - '), bins = 100, cols = c('#463F3A', '#B7FE63'))
    }
    dev.off()
}

for (year in 2015:2020)
{
    for (state in c('National', 'Gujarat', 'Maharashtra', 'Andhra Pradesh', 'Karnataka'))
    {
        save_heatmap(state, year)
    }
}

