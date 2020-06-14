#reference : http://rstudio-pubs-static.s3.amazonaws.com/74431_8cbd662559f6451f9cd411545f28107f.html
#importing the data
data = read.csv("D:/2020_Summer_Break/Microsoft Azure Virtual Hackathon/Microsoft-Azure-Hackathon/PottedML-traindata.csv")
#View(data)

#summary stats
summary(data)

#testing into train and test data
require(caTools)
set.seed(123)
sample = sample.split(data,SplitRatio = 0.8)
train =subset(data,sample ==TRUE)
test=subset(data, sample==FALSE)

# run the logistic regression model on training dataset
glm.model <- glm(IsHealthy~., data=train, family=binomial)
summary(glm.model)

library(tidyverse)
# Make predictions
probabilities <- glm.model %>% predict(test, type = "response")
predicted.classes <- ifelse(probabilities > 0.5, 1, 0)
predicted.classes

# Model accuracy
mean(predicted.classes == test$IsHealthy)

#Confusion Matrix
#reference: https://www.rdocumentation.org/packages/caret/versions/6.0-86/topics/confusionMatrix
data.prob = predict(glm.model, test, type="response")
data.pred = rep(0, dim(train)[1])
data.pred[data.prob > .5] = 1
table(data.pred, train$IsHealthy)





