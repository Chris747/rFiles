counter <- read.csv(file="counter.csv",header=FALSE)

barplot(as.integer(counter$V2), 
  width = 5,
  names.arg = counter$V1,
  xlab = "Words", ylab = "Frequency", main = "Top 10 words in the abstracts")