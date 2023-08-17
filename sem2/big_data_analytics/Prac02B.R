# Apriori
# Data Preprocessing
install.packages('arules')
install.packages("RColorBrewer")
library(arules)
library(RColorBrewer)
dataset = read.csv('D:\\Market_Basket_Optimisation.csv', header = FALSE)
dataset = read.transactions('D:\\Market_Basket_Optimisation.csv', sep = ',', rm.duplicates = TRUE)
summary(dataset)
# Training Apriori on the dataset
rules = apriori(data = dataset, parameter = list(support = 0.004, confidence = 0.2))
# Visualising the results
inspect(sort(rules, by = 'lift')[1:10])
itemFrequencyPlot(dataset, topN = 10,
                  col = brewer.pal(8, 'Pastel2'),
                  main = 'Relative Item Frequency Plot',
                  type = "relative",
                  ylab = "Item Frequency (Relative)")
itemsets = apriori(dataset, parameter = list(minlen=2, maxlen=2,support=0.02, target="frequent itemsets"))
summary(itemsets)
# using inspect() function
inspect(itemsets[1:10])
itemsets_3 = apriori(dataset, parameter = list(minlen=3, maxlen=3,support=0.02, target="frequent itemsets"))
summary(itemsets_3)
print ("Candidate list with 3 itemsets is not possible for this dataset")