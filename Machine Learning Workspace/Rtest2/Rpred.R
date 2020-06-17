load("glm.model.rda")
data.prob = predict(glm.model, test, type="response")
data.pred = rep(0, dim(train)[1])
data.pred[data.prob > .5] = 1