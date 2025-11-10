import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

df = pd.read_csv("/home/CIN/lfvs2/Documents/DATA (1).csv")  #import/ leitura dos dados ***É necessário mudar o caminho do dataset quando baixar!***

print(df.head())    #Teste de impressão das primeiras linhas

df.info()       #informações gerais do dataset

print(df.isnull().sum())    #conta valores ausentes

print(df.describe())        #estatisticas descritivas
print(df.dtypes)

X = df.drop(columns=['STUDENT ID', 'GRADE'])    #vou separar as entradas das saídas
y = df['GRADE']

#normalização das variaveis, deixando cada valor com o mesmo peso
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X= pd.DataFrame(X_scaled, columns=X.columns)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.2, random_state= 42)

print("Tamanho do treino:", X_train.shape)
print("Tamanho do teste:", X_test.shape)
print("Exemplo de entrada:")
print(X_train.head())


    