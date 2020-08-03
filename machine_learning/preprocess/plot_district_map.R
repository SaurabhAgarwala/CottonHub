library(rgdal)
library(broom)

distr_rename <- list(
    'Amreli' = 'Amreli',
    'Kachchh' = 'Kachchh',
    'Bhavnagar' = 'Bhavnagar',
    'Sabarkantha' = 'Sabar Kantha',
    'Vadodara(Baroda)' = 'Vadodara',
    'Surendranagar' = 'Surendranagar',
    'Ahmedabad' = 'Ahmadabad',
    'Rajkot' = 'Rajkot',
    'Jamnagar' = 'Jamnagar',
    'Kheda' = 'Kheda',
    'Junagarh' = 'Junagadh',
    'Gandhinagar' = 'Gandhinagar',
    'Surat' = 'Surat',
    'Patan' = 'Patan',
    'Mehsana' = 'Mahesana',
    'Morbi' = 'NULL',
    'Wardha' = 'Wardha',
    'Nanded' = 'Nanded',
    'Nagpur' = 'Nagpur',
    'Beed' = 'Bid',
    'Parbhani' = 'Parbhani',
    'Chandrapur' = 'Chandrapur',
    'Coimbatore' = 'Coimbatore',
    'Villupuram' = 'Viluppuram',
    'Salem' = 'Salem',
    'Tuticorin' = 'Thoothukkudi',
    'Dharmapuri' = 'Dharmapuri',
    'Virudhunagar' = 'Virudunagar',
    'Theni' = 'Theni',
    'Madurai' = 'Madurai',
    'Krishnagiri' = 'Krishnagiri',
    'Kurnool' = 'Kurnool',
    'Guntur' = 'Guntur',
    'Prakasam' = 'Prakasam',
    'Krishna' = 'Krishna',
    'Cuddapah' = 'Y.s.r',
    'East Godavari' = 'East Godavari',
    'Anantapur' = 'Anantapur',
    'Adilabad' = 'Adilabad',
    'Karimnagar' = 'Karimnagar',
    'Khammam' = 'Khammam',
    'Medak' = 'Medak',
    'Warangal' = 'Warangal',
    'Nizamabad' = 'Nizamabad',
    'Ganganagar' = 'Ganganagar',
    'Ajmer' = 'Ajmer',
    'Jodhpur' = 'Jodhpur',
    'Hanumangarh' = 'Hanumangarh',
    'Alwar' = 'Alwar',
    'Hissar' = 'Hisar',
    'Fatehabad' = 'Fatehabad',
    'Sirsa' = 'Sirsa',
    'Jind' = 'Jind',
    'Fazilka' = 'NULL',
    'Mansa' = 'Mansa',
    'Muktsar' = 'Muktsar',
    'Faridkot' = 'Faridkot',
    'Bhatinda' = 'Bathinda',
    'Dharwad' = 'Dharwad',
    'Bijapur' = 'Bijapur',
    'Chitradurga' = 'Chitradurga',
    'Davangere' = 'Davanagere',
    'Haveri' = 'Haveri',
    'Bellary' = 'Bellary',
    'Raichur' = 'Raichur',
    'Badwani' = 'Barwani',
    'Khargone' = 'West Nimar',
    'Dhar' = 'Dhar',
    'Jhabua' = 'Jhabua',
    'Alirajpur' = 'Alirajpur',
    'Chhindwara' = 'Chhindwara'
)

state_coord <- list(
    'National' = c(67, 103, 6, 38),
    'Gujarat' = c(68, 76, 20, 25),
    'Andhra Pradesh' = c(75, 87, 12, 20),
    'Karnataka' = c(73, 81, 11, 19),
    'Rajasthan' = c(69, 80, 21, 31),
    'Madhya Pradesh' = c(73, 85, 19, 28),
    'Tamil Nadu' = c(75, 83, 8, 14),
    'Maharashtra' = c(72, 83, 15, 23),
    'Haryana' = c(74, 79, 26.5, 31.5)
)

distr_colorbar <- function(cols, val_min = 0, val_max = 0, coords = c(67, 103, 6, 38))
{
    x_factor <- (coords[2] - coords[1]) / (103 - 67)
    y_factor <- (coords[4] - coords[3]) / (38 - 6)
    inc <- (coords[4] - coords[3]) / length(cols)
    for (col_ind in seq(cols))
    {
        rect(coords[2] - 4.5 * x_factor, coords[3] + (col_ind - 1) * inc, coords[2] - 3 * x_factor, coords[3] + col_ind * inc, col = cols[col_ind], border = NA)
    }
    text(coords[2] - 3 * y_factor, coords[3], paste('Rs. ', format(val_min, digits = 4), sep = ''), pos = 4, cex = 0.65, col = 'black')
    text(coords[2] - 3 * y_factor, coords[4], paste('Rs. ', format(val_max, digits = 4), sep = ''), pos = 4, cex = 0.65, col = 'black')
    text(coords[2] - 3 * y_factor, (coords[3] + coords[4])/2, paste('Rs.', format((val_min + val_max) / 2, digits = 4), sep = ''), pos = 4, cex = 0.65, col = 'black')
    text(coords[2] - 3 * y_factor, (3*coords[3] + coords[4])/4, paste('Rs.', format((3 * val_min + val_max) / 4, digits = 4), sep = ''), pos = 4, cex = 0.65, col = 'black')
    text(coords[2] - 3 * y_factor, (coords[3] + 3*coords[4])/4, paste('Rs.', format((val_min + 3 * val_max) / 4, digits = 4), sep = ''), pos = 4, cex = 0.65, col = 'black')
}

plot_distr_map <- function(data_vals, plot_area, coords = c(67, 103, 6, 38), title = '', subtitle = '', bins = 100, cols = c('green', 'blue'))
{
    my_spdf <- readOGR(dsn= "./data/India_Shapefiles/India_Districts/", layer="2011_Dist", verbose=FALSE)
    
    distr_data <- my_spdf@data
    distr_polygons <- my_spdf@polygons
    
    #for (missing_distr in names(unavail_distr))
    #    data_vals[unavail_distr[missing_distr][[1]]] <- data_vals[unavail_distr[missing_distr][[1]]] + data_vals[missing_distr]
    data_vals_names <- sapply(names(data_vals), function(i) {distr_rename[i]})
    names(data_vals) <- data_vals_names
    min_val <- min(data_vals)
    max_val <- max(data_vals)
    scaled_vals <- c(3000, 5000, data_vals)
    binned_vals <- as.numeric(cut(scaled_vals, breaks = bins, labels = seq(bins)))[3:length(scaled_vals)]
    
    cols = colorRampPalette(cols)(bins)
    par(mfrow = c(1, 1), mar = c(4, 1, 4, 1), xaxt = 'n', yaxt = 'n', fg = '#b7ce63', bg = '#b7ce63')
    plot(0, xlab = "", ylab = "", xlim = c(coords[1], coords[2]), ylim = c(coords[3], coords[4]), main = title)
    used_distr <- c()
    for (i in seq(length(distr_polygons)))
    {
        polygons <- distr_polygons[[i]]@Polygons
        state <- as.character(distr_data[as.character(distr_polygons[[i]]@ID), 'ST_NM'])
        if(plot_area != 'National')
        {
            if(state != plot_area)
                next
        }
        distr <- as.character(distr_data[as.character(distr_polygons[[i]]@ID), 'DISTRICT'])
        used_distr <- c(used_distr, distr)
        distr_col <- cols[binned_vals[match(distr, names(data_vals))]]
        if(is.na(distr_col))
            distr_col <- 'white'
        for (j in seq(length(polygons)))
            polygon(attributes(my_spdf@polygons[[i]]@Polygons[[j]])$coords, col = distr_col, border = 'black')
    }
    #print(unique(used_distr))
    mtext(subtitle, side = 1)
    distr_colorbar(cols, 3000, 5000, coords)
}

#state_distr_list <- read.csv('./data/state_distr_market_variety_map.csv')
#distr <- unique(state_distr_list$District)
#distr_vals <- sapply(distr, function(i) {runif(1, 0, 1)})
#names(distr_vals) <- distr
#state <- 'National'
#plot_distr_map(distr_vals, state, coords = state_coord[state][[1]], title = state, subtitle = "Map based on 2011 Census (Morbi considered under Rajkot)", bins = 100, cols = c('#7D98a1', '#B7EE63'))
