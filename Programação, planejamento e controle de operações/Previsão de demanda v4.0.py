import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Carregue os dados da sua base de dados
# Substitua 'seu_arquivo.csv' pelo nome do seu arquivo CSV ou o formato que estiver usando
data = pd.read_csv('Amazon Sale Report.csv', sep=',')

# print("Nomes das Colunas:", data.columns)

# Selecionando as colunas relevantes para treinamento
features = data[['Sales Channel ', 'ship-service-level', 'Style', 'Category', 'Size', 'ASIN']]
target = data['Qty']

# Convertemos variáveis categóricas em variáveis dummy
features = pd.get_dummies(features)

# Divida os dados em conjuntos de treinamento (11 semanas) e teste (3 semanas)
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=3, shuffle=False)

# KNN
knn_model = KNeighborsRegressor()
knn_model.fit(X_train, y_train)
knn_predictions = knn_model.predict(X_test)

# Random Forest
rf_model = RandomForestRegressor()
rf_model.fit(X_train, y_train)
rf_predictions = rf_model.predict(X_test)

# Avalie o desempenho usando o erro médio quadrático (MSE)
knn_mse = mean_squared_error(y_test, knn_predictions)
rf_mse = mean_squared_error(y_test, rf_predictions)

# Crie gráficos
plt.figure(figsize=(10, 5))

# Gráfico para KNN
plt.subplot(1, 2, 1)
plt.plot(y_test.index, y_test, label='Real')
plt.plot(y_test.index, knn_predictions, label='KNN Predictions')
plt.title(f'KNN - MSE: {knn_mse:.2f}')
plt.legend()

# Gráfico para Random Forest
plt.subplot(1, 2, 2)
plt.plot(y_test.index, y_test, label='Real')
plt.plot(y_test.index, rf_predictions, label='Random Forest Predictions')
plt.title(f'Random Forest - MSE: {rf_mse:.2f}')
plt.legend()

plt.tight_layout()
plt.show()
