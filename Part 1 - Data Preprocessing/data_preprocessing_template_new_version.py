# Plantilla de Pre Procesado

# Importar las librerias en Python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importar el Data set
dataset = pd.read_csv("Data2.csv")
X = dataset.iloc[:, :-1].values #iloc localiza elemetos por posición
y = dataset.iloc[:, 4].values 

# %%

# Tratamiento de los NAs
from sklearn.impute import SimpleImputer 
imputer = SimpleImputer(missing_values = np.nan, strategy = "mean", verbose=0)  #creo objeto imputer desde clase  SimpleImputer
imputer = imputer.fit(X[:,1:4])                                                 #Fit the imputer on X
X[:, 1:4] = imputer.transform(X[:,1:4])                                         #Fit to data, then transform it.

# %%

# Codificar datos categoricos
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer

labelencoder_X = LabelEncoder()
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])                                 # Creo etiquetas numericas en columna cero (paises)

ct = ColumnTransformer(
    [('one_hot_encoder', OneHotEncoder(categories='auto'), [0])],               # Transformo etiquetas numericas - one hot encoding 
    remainder='passthrough'                        
)

X = np.array(ct.fit_transform(X), dtype=np.float)
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)
#%%

# Dividir el data set en conjunto de entrenamiento y en conjunto de testing
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size = 0.2, random_state = 0)

# Escalado de variables
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)