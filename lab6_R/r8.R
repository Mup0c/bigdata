library("ggplot2")
data <- read.csv("titanic_train.csv")
data <- data[which(!is.na(data$Age)),]
a = aggregate(data$Age, list(data$Pclass), mean)
qplot(x=a$Group.1, y=a$x,geom="col", fill=factor(a$x)) +xlab("") + ylab("")