library(rgdal)
library(broom)

colorbar <- function(cols, val_min = 0, val_max = 0, coords = c(67, 103, 6, 38))
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

plot_map <- function(data_vals, title = '', subtitle = '', bins = 100, cols = c('green', 'blue'))
{
  my_spdf <- readOGR(dsn= "./data/India_Shapefiles/India_States/", layer="India", verbose=FALSE)
  
  state_data <- my_spdf@data
  state_polygons <- my_spdf@polygons
  
  min_val <- min(data_vals)
  max_val <- max(data_vals)
  scaled_vals <- c(3000, 5000, data_vals)
  binned_vals <- as.numeric(cut(scaled_vals, breaks = bins, labels = seq(bins)))[3:length(scaled_vals)]
  
  cols = colorRampPalette(cols)(bins)
  par(mfrow = c(1, 1), mar = c(4, 1, 4, 1), xaxt = 'n', yaxt = 'n', fg = '#b7ce63', bg = '#b7ce63')
  plot(0, xlab = "", ylab = "", xlim = c(67, 103), ylim = c(6, 38), main = title)
  for (i in seq(length(state_polygons)))
  {
    polygons <- state_polygons[[i]]@Polygons
    state <- as.character(state_data[as.character(state_polygons[[i]]@ID), 'NAME_1'])
    state_col <- cols[binned_vals[match(state, names(data_vals))]]
    if(is.na(state_col))
      state_col <- 'white'
    for (j in seq(length(polygons)))
      polygon(attributes(my_spdf@polygons[[i]]@Polygons[[j]])$coords, col = state_col, border = 'black')
  }
  mtext(subtitle, side = 1)
  colorbar(cols, 3000, 5000)
}

#data_vals <- c("Maharashtra" = 10, "Gujarat" = 25, "Karnataka" = 15, "Andhra Pradesh" = 5, "Tamil Nadu" = 10)
#plot_map(data_vals, title = "Random State Distribution", bins = 100, subtitle = "(subtitle)")
