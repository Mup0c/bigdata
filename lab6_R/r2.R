library("ggplot2")
data <- read.csv("titanic_train.csv")

qplot(factor(data$Pclass), fill=data$Sex) + labs(fill="class") + xlab("sex")
table(data$Pclass)

females = data[which(data$Sex == 'female'),]
males = data[which(data$Sex == 'male'),]

qplot(factor(males$Pclass), main = "Males", fill=factor(males$Pclass)) + labs(fill="class") + xlab("class")
qplot(factor(females$Pclass), main = "Females", fill=factor(females$Pclass)) + labs(fill="class") + xlab("class")

table(females$Pclass)
table(males$Pclass)