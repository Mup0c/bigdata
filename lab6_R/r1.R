library("ggplot2")
data <- read.csv("titanic_train.csv")

qplot(factor(data$Sex), fill=data$Sex) + labs(fill="Sex") + xlab("sex") + ylab("count")
table(sex)