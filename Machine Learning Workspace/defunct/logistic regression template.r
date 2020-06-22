# done in R, codes taken from parts of DSA notes

# logistic regression model
library(ISLR)
attach(Default) # load the data. But for us is read.csv("...")
summary(Default)

# run the logistic regression models
glm.def1 <- glm(default~., data=Default, family=binomial)
summary(glm.def1)

predict(glm.def1, data.frame(balance=c(1000, 2000)), type="response")  # here is prediction. We can put in a set of values to test


# confusion matrix (and from there calculate the specificity etc)
# set the threshold value to 0.5   # we can change the 0.5 to other num oso can haha
glm.prob5 <- predict(glm.def1, type="response")
glm.pred5.1 <- rep("Predicted No Default", 10000)
glm.pred5.1[glm.prob5> 0.5] <- "Predicted Default"
table(glm.pred5.1, default)


