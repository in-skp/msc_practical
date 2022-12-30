#' Created on Fri Dec 30
#' 
#' author: Santosh Parse
#' program name: Program to retrieve different types of attributes

library(readr)
library(tibble)
Base = "C:/VKHCG"
FileName = paste0(Base, '/01-Vermeulen/00-RawData/IP_DATA_ALL.csv')
IP_DATA_ALL <- read_csv(FileName)
spec(IP_DATA_ALL)
view(IP_DATA_ALL)
IP_DATA_ALL_FIX = set_tidy_names(IP_DATA_ALL, syntactic = TRUE, quiet = FALSE)
IP_DATA_ALL_with_ID = rowid_to_column(IP_DATA_ALL_FIX, var = "RowID")
Base=getwd()
FileName = paste0(Base, '/IP_DATA_ALL_with_ID.csv')
write.csv(IP_DATA_ALL_with_ID, FileName)

