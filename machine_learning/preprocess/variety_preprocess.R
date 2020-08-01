variety_preprocess <- function(data)
{
    ############################################################
    # Combine varieties of the same type by name
    ############################################################
    
    new_vars <- list(
        '170-C2  (Ginned)' = '170-C',
        '170-CO2 (Unginned)' = '170-C',
        '320F' = '320F',
        'A-51-9 24mm. FIne' = 'A-51-9',
        'A.C. 122- H4' = 'A.C.',
        'A.K. 235  (Ginned)' = 'A.K.',
        'A.K. 235 (Unginned)' = 'A.K.',
        'Aka-1 (Unginned)' = 'Aka',
        'American' = 'American',
        'Assam Comilla' = 'Assam Comilla',
        'Bengal Deshi (A) FIne' = 'Bengal Desi',
        'Bramha' = 'Bramha',
        'Bunny' = 'Bunny',
        'CJ 73 22mm FIne' = 'CJ',
        'CO-2 (Unginned)' = 'CO2',
        'CO2  (Ginned)' = 'CO2',
        'Cotton (Ginned)' = 'Cotton',
        'Cotton (Unginned)' = 'Cotton',
        'Cotton US' = 'Cotton',
        'DCH-32  (Ginned)' = 'DCH',
        'DCH-32(Unginned)' = 'DCH',
        'DIGVIJAY 24mm, Superfine' = 'Digvijay',
        'Desi' = 'Desi',
        'F-1054' = 'F',
        'F-1378' = 'F',
        'F-505' = 'F',
        'F-846' = 'F',
        'Farm  (Ginned)' = 'Farm',
        'Farm (Unginned)' = 'Farm',
        'Farm PCG' = 'Farm',
        'G-6' = 'G',
        'G.Cot-13' = 'G.Cot',
        'G.Cot-21' = 'G.Cot',
        'GCH' = 'GCH',
        'H 420' = 'H',
        'H-4(A) 27mm FIne' = 'H',
        'H-6' = 'H',
        'H-777' = 'H',
        'H.B  (Ginned)' = 'H.B',
        'H.B (Unginned)' = 'H.B',
        'H.Y.4 (Unginned)' = 'H.Y.4',
        'H4' = 'H',
        'HB6' = 'H.B',
        'Hampi  (Ginned)' = 'Hampi',
        'Hampi(Unginned)' = 'Hampi',
        'Hy-4  (Ginned)' = 'Hy',
        'J-34' = 'J',
        'J3H' = 'J',
        'JKH 25' = 'J',
        'Jarilla  (Ginned)' = 'Jarilla',
        'Jarilla (Unginned)' = 'Jarilla',
        'Jayadhar' = 'Jayadhar',
        'Jayadhar (Ginned)' = 'Jayadhar',
        'Jayadhar 23mm-FIne' = 'Jayadhar',
        'Jayadhar(Unginned)' = 'Jayadhar',
        'Jayalakshmi (Unginned)' = 'Jayalakshmi',
        'Jaydhar' = 'Jayadhar',
        'Kapas (Adoni)' = 'Kapas',
        'Krishna' = 'Krishna',
        'L 147' = 'L',
        'L-K' = 'L',
        'LD-230' = 'LD',
        'LD-327' = 'LD',
        'LD-491' = 'LD',
        'LDH-11' = 'LDH',
        'LH-1556' = 'LH',
        'LRA' = 'LRA',
        'LRA  (Ginned)' = 'LRA',
        'Laxmi' = 'Lakshmi',
        'Laxmi  (Ginned)' = 'Lakshmi',
        'Laxmi (Unginned)' = 'Lakshmi',
        'Lh-1134' = 'LH',
        'Locaal' = 'Local',
        'Local' = 'Local',
        'MCU' = 'MCU',
        'MCU 5' = 'MCU',
        'MCU-5 (A) 31mm FIne' = 'MCU',
        'MCU-7' = 'MCU',
        'MECH-1' = 'Mech',
        'MECH-4' = 'Mech',
        'Mahico' = 'Mahico',
        'Mector' = 'Mector',
        'Mungari  (Ginned)' = 'Mungari',
        'Mungari (Unginned)' = 'Mungari',
        'N-44' = 'N',
        'Narma BT Cotton' = 'Narma',
        'Other' = 'Other',
        'PCO2' = 'PCO2',
        'R-51  (Ginned)' = 'R',
        'R-51 (Unginned)' = 'R',
        'R.G.J-34 24mm-Fine' = 'R.G.J',
        'RCH-2' = 'RCH',
        'Savita' = 'Savita',
        'Shanker 4 31mm FIne' = 'Shanker',
        'Shanker 6 (B) 30mm FIne' = 'Shanker',
        'Surabi' = 'Surabi',
        'Suvin 40mm(F)' = 'Suvin',
        'Suyodhar  (Ginned)' = 'Suyodhar',
        'V-797 22mm FIne' = 'V',
        'Varalakshmi  (Ginned)' = 'Varalakshmi',
        'Varalaxmi' = 'Varalakshmi',
        'Varalaxmi(A) 36mm(1-13/32)F' = 'Varalakshmi',
        'Wagad 20mm(F)' = 'Wagad',
        'Y-1' = 'Y',
        'Y-1/ Jyoti 24mm. FIne' = 'Y',
        'cotton (Ginned)' = 'Cotton',
        'lra (Unginned)' = 'LRA'
    )
    data <- transform(data, Variety = new_vars[Variety])
    
    #variety_distr <- sort(table(data$Variety), decreasing = TRUE)
    #variety_distr <- variety_distr / sum(variety_distr) * 100
    #variety_distr <- head(variety_distr, n = 10)
    #par(mfrow = c(1, 1), mar = c(8, 4, 3, 0), cex.axis = 0.7, cex.lab = 1, cex.main = 1.25)
    #barplot(variety_distr, width = 1, space = 0, xaxt = 'n', ylab = "Percentage Composition (%)")
    #axis(1, at = seq(1, length(variety_distr)) - 0.5, labels = names(variety_distr), las = 2)
    #title(main = "Distribution of Cotton Variety")
    #mtext("(Top 10 Cotton Varieties considered)", side = 3, cex = 1, at = c(5, 35))
    #dev.off()
    
    #library(ggplot2)
    #logged_data <- transform(data, Modal_Price = log10(Modal_Price), Min_Price = log10(Min_Price), Max_Price = log10(Max_Price))
    #top10_variety <- names(variety_distr)
    #variety_data <- subset(logged_data, logged_data$Variety %in% top10_variety)
    #g <- ggplot(data = variety_data, aes(x = Variety, y = Modal_Price))
    #g + geom_boxplot() + ylab("log10(Modal Prices)") + theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1))
    #dev.off()
    
    data
}