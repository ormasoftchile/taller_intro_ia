# Data Preprocessing

# Importing the dataset
#dataset = read.csv('C:/Users/juanp/OneDrive - UNIVERSIDAD ANDRES BELLO/4.Clases_JPV/4.Fundamentos Ciencia Datos MCC 601 - JPV/Code-ML-Python-UNIDAD2/Part 1 - Data Preprocessing/R')

library(readr)
dataset = read_csv("C:/Users/juanp/OneDrive - UNIVERSIDAD ANDRES BELLO/4.Clases_JPV/4.Fundamentos Ciencia Datos MCC 601 - JPV/Code-ML-Python-UNIDAD2/Part 1 - Data Preprocessing/R/Data.csv")
View(Data)

# Taking care of missing data
dataset$Age = ifelse(is.na(dataset$Age),
                     ave(dataset$Age, FUN = function(x) mean(x, na.rm = TRUE)),
                     dataset$Age)
dataset$Salary = ifelse(is.na(dataset$Salary),
                        ave(dataset$Salary, FUN = function(x) mean(x, na.rm = TRUE)),
                        dataset$Salary)
