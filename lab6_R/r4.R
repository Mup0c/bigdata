library("ggplot2") 
data <- read.csv("titanic_train.csv") 

young <- data[which(data$Age < 30),] 
old <- data[which(data$Age > 60),] 

qplot((factor(young$Survived)),geom="bar", fill = factor(young$Survived),main = "Young")+xlab("") + ylab("") + labs(fill="Survived")
qplot((factor(old$Survived)),geom="bar", fill = factor(old$Survived),main = "Old")+xlab("") + ylab("") + labs(fill="Survived")
table(factor(young$Survived))
table(factor(old$Survived))