my_data <- read.csv(file = "/home/chao/Desktop/Ironhack/Projects/Project-Week-5-Your-Own-Project/data/table_anova.csv", header=TRUE, sep=",")


aov1 <- aov(total_time ~ morning_afternoon + month, data = my_data)
summary(aov1)