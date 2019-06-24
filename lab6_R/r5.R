library("ggplot2") 
data <- read.csv("titanic_train.csv") 

females = data[which(data$Sex == 'female'),]
males = data[which(data$Sex == 'male'),]

qplot((factor(females$Survived)),geom="bar", fill = factor(females$Survived),main = "females")+xlab("") + ylab("") + labs(fill="Survived")
qplot((factor(males$Survived)),geom="bar", fill = factor(males$Survived),main = "male")+xlab("") + ylab("") + labs(fill="Survived")
table(factor(females$Survived))
table(factor(males$Survived))