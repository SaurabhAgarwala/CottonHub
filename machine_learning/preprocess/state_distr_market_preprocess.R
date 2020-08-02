state_distr_market_preprocess <- function(data)
{
    
    ############################################################
    # State name conversion for consistency
    ############################################################
    
    orig_name <- c('Odisha', 'Pondicherry', 'NCT of Delhi', 'Uttrakhand',  'Chattisgarh')
    new_name  <- c('Orissa', 'Puducherry',  'Delhi',        'Uttaranchal', 'Chhattisgarh')
    for (i in seq(length(orig_name)))
        data$State <- as.character(replace(data$State, data$State == orig_name[i], new_name[i]))
    
    ############################################################
    # Districts that were in multiple states
    ############################################################
    
    state_distr_map <- table(list(data$State, data$District))
    multiple_state_distr <- c()
    for (i in colnames(state_distr_map))
    {
        if(sum(state_distr_map[, i] != 0) != 1)
            multiple_state_distr <- c(multiple_state_distr, i)
    }
    
    #par(mfrow = c(length(multiple_state_distr), 1), mai = c(0, 0, 0, 0), oma = c(2, 2, 2, 0), yaxt = 'n')
    #date_rng = range(data$Date)
    #for (i in seq_along(multiple_state_distr))
    #{
    #    sample <- subset(data, District == multiple_state_distr[i])
    #    if(i == length(multiple_state_distr))
    #        plot(x = sample$Date, y = as.numeric(rep(1, nrow(sample))), col = as.factor(sample$State), xlim = date_rng)
    #    else
    #        plot(x = sample$Date, y = as.numeric(rep(1, nrow(sample))), col = as.factor(sample$State), xlim = date_rng, xaxt = 'n')
    #    mtext(multiple_state_distr[i], side = 2, cex = 0.75)
    #    legend('bottomleft', col = c(1, 2), legend = levels(as.factor(sample$State)), pch = c(1, 1))
    #}
    #mtext(text = "Districts with multiple States", outer = TRUE, cex = 1.25)
    #dev.off()
    
    for (i in multiple_state_distr)
    {
        distr_idx <- which(data$District == i)
        data[distr_idx, 'State'] <- as.character(rep(names(which.max(state_distr_map[, i])), length(distr_idx)))
    }
    
    ############################################################
    # Markets that were in multiple districts
    ############################################################
    
    distr_market_map <- table(list(data$District, data$Market))
    multiple_distr_market <- c()
    for (i in colnames(distr_market_map))
    {
        if(sum(distr_market_map[, i] != 0) != 1)
            multiple_distr_market <- c(multiple_distr_market, i)
    }
    
    #par(mfrow = c(length(multiple_distr_market), 1), mai = c(0, 0, 0, 0), oma = c(2, 2, 2, 0), yaxt = 'n')
    #date_rng = range(data$Date)
    #for (i in seq_along(multiple_distr_market))
    #{
    #    sample <- subset(data, Market == multiple_distr_market[i])
    #    if(i == length(multiple_distr_market))
    #        plot(x = sample$Date, y = as.numeric(rep(1, nrow(sample))), col = as.factor(sample$State), xlim = date_rng)
    #    else
    #        plot(x = sample$Date, y = as.numeric(rep(1, nrow(sample))), col = as.factor(sample$State), xlim = date_rng, xaxt = 'n')
    #    mtext(multiple_distr_market[i], side = 2, cex = 0.6)
    #    legend('bottomleft', col = c(1, 2), legend = levels(as.factor(sample$State)), pch = c(1, 1))
    #}
    #mtext(text = "Markets with multiple Districts / States", outer = TRUE, cex = 1.25)
    #dev.off()
    
    for (i in multiple_distr_market)
    {
        sample <- subset(data, Market == i)
        if(length(unique(sample$State)) == 1)
        {
            market_idx <- which(data$Market == i)
            data[market_idx, 'District'] <- as.character(rep(names(which.max(distr_market_map[, i])), length(market_idx)))
        }
        else
        {
            states <- unique(sample$State)
            for (j in states)
            {
                market_idx <- which((data$Market == i) & (data$State == j))
                data[market_idx, 'Market'] <- as.character(rep(paste(i, j, sep = '_'), length(market_idx)))
            }
        }
    }
    
    ############################################################
    # Visualize State Statistics
    ############################################################
    
    #source("./plot_map.R")
    
    #states <- unique(data$State)
    #state_cnt <- sapply(states, function(i) {nrow(subset(data, State == i))})
    #plot_map(state_cnt, title = "State Count Distribution")
    
    #cnt_thresh <- quantile(state_cnt, 0.25)
    #valid_states <- state_cnt > cnt_thresh
    #state_avg <- sapply(states[valid_states], function(i) {mean(subset(data, State == i)$Modal_Price, na.rm = TRUE)})
    #plot_map(state_avg, title = "State Average Cotton Prices Distribution", subtitle = paste("States with count >",cnt_thresh," considered only"))
    
    data
}
