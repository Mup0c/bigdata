library("ggplot2")
data <- read.csv("titanic_train.csv")

dev <- round(sd(data$Fare), digits = 2)
med <- round(median(data$Fare), digits = 2)
mx <- c(dev, med)
names(mx) <- c("deviation", "median")
pd <- c(dev, med)

qplot(x=names(mx), y=mx,geom="col") +xlab("") + ylab("")

med 
dev