library("ggplot2")
data <- read.csv("titanic_train.csv")
males  = data[which(data$Sex == "male"),]

r <- lapply(males$Name, function(x) tail(strsplit(as.character(x), " ")[[1]], 1))
sortedNames <- sort(table(as.character(r)), decreasing = TRUE)
sortedNames[1:3]
qplot(x=rownames(sortedNames[1:10]), y=sortedNames[1:10], geom="col", fill=factor(sn))