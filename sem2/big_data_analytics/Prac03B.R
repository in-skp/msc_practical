# install.packages("InformationValue")
# install.packages("devtools")
devtools::install_github("selva86/InformationValue")
library(ISLR)
library(InformationValue)
data <- ISLR::Default
print(head(ISLR::Default))
summary(data)
nrow(data)
set.seed(1)
sample <- sample(c(TRUE, FALSE), nrow(data), replace=TRUE, prob=c(0.7,0.3))
print(sample)
train <- data[sample, ]
test <- data[!sample, ]
nrow(train)
nrow(test)
model <- glm(default~student+balance+income, family = "binomial" , data = train)
summary(model)


predicted <- predict(model,test,type="response")
confusionMatrix(test$default,predicted)