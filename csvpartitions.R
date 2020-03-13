admission_data <- read.csv("Admission_Predict.csv")
# install.packages("caret")
# install.packages("lattice")
library(caret)
library(lattice)
inTrain <- createDataPartition(y=admission_data$Chance.of.Admit, p=0.6,list=FALSE)
training <- admission_data[inTrain,]
test_and_cv <- admission_data[-inTrain,]
inCV <- createDataPartition(y=test_and_cv$Chance.of.Admit, p=0.5,list=FALSE)
cross_v <- test_and_cv[inCV,]
test <- test_and_cv[-inCV,]

write.csv(training,"adamission_training.csv", row.names=F)
write.csv(test,"admission_test.csv",row.names=F)
write.csv(cross_v,"admission_cv.csv",row.names=F)
