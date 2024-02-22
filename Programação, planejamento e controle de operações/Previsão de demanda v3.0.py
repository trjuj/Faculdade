import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.preprocessing import StandardScaler
from math import sqrt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Carregando os dados
data = pd.read_csv('Amazon Sale Report.csv', low_memory=False)

# Verificando os nomes das colunas
print(data.columns)

# Garantindo que a coluna 'Date' exista
if 'Date' in data.columns:
    data['Date'] = pd.to_datetime(data['Date'], format='%m-%d-%y')
else:
    raise ValueError("Coluna 'Date' não encontrada no DataFrame")

# Tratando valores NaN
data = data.dropna(subset=['Date', 'Qty'])

# Agregando dados em nível diário
daily_data = data.groupby(data['Date'].dt.date)['Qty'].sum()

# Engenharia de características
daily_data = daily_data.reset_index()
daily_data['Year'] = pd.to_datetime(daily_data['Date']).dt.year
daily_data['Month'] = pd.to_datetime(daily_data['Date']).dt.month
daily_data['Day'] = pd.to_datetime(daily_data['Date']).dt.day

# Separando características e alvo
X = daily_data[['Year', 'Month', 'Day']]
y = daily_data['Qty']

# Normalizando características
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Separando os dados para as últimas 3 semanas
threshold_date = daily_data['Date'].max() - pd.Timedelta(weeks=3)
train_data = daily_data[daily_data['Date'] <= threshold_date]
test_data = daily_data[daily_data['Date'] > threshold_date]


X_train = scaler.transform(train_data[['Year', 'Month', 'Day']])
print(X_train)
y_train = train_data['Qty']
print(y_train)
X_test = scaler.transform(test_data[['Year', 'Month', 'Day']])
y_test = test_data['Qty']


# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=42)

# Modelos
knn = KNeighborsRegressor(n_neighbors=min(9, len(X_train)))
rf = RandomForestRegressor(n_estimators=150)

# Treinamento
knn.fit(X_train, y_train)
rf.fit(X_train, y_train)

# Previsões
y_pred_knn = knn.predict(X_test)
y_pred_rf = rf.predict(X_test)

# Avaliação
rmse_knn = sqrt(mean_squared_error(y_test, y_pred_knn))
rmse_rf = sqrt(mean_squared_error(y_test, y_pred_rf))
mae_knn = mean_absolute_error(y_test, y_pred_knn)
mae_rf = mean_absolute_error(y_test, y_pred_rf)
mape_knn = np.mean(np.abs((y_test - y_pred_knn) / y_test)) * 100
mape_rf = np.mean(np.abs((y_test - y_pred_rf) / y_test)) * 100
mse_knn = mean_squared_error(y_test, y_pred_knn)
mse_rf = mean_squared_error(y_test, y_pred_rf)

print(f'RMSE KNN: {rmse_knn}')
print(f'RMSE Floresta Aleatória: {rmse_rf}')
print(f'MAE KNN: {mae_knn}')
print(f'MAE Floresta Aleatória: {mae_rf}')
print(f'MAPE KNN: {mape_knn}%')
print(f'MAPE Floresta Aleatória: {mape_rf}%')
print(f'MSE KNN: {mse_knn}')
print(f'MSE Floresta Aleatória: {mse_rf}')

# Visualização
plt.figure(figsize=(18, 6))
model_names = ['KNN', 'Floresta Aleatória']
dates = mdates.date2num(pd.to_datetime(train_data['Date']))  # Convertendo datas para números

# Criando um plot para cada modelo
for i, model_predictions in enumerate([y_pred_knn, y_pred_rf]):
    plt.subplot(1, 2, i + 1)
    plt.scatter(dates, y_train, color='blue', alpha=0.7)
    test_dates_num = mdates.date2num(pd.to_datetime(test_data['Date']))  # Convertendo datas de teste para formato numérico
    plt.scatter(test_dates_num, model_predictions, color='green', label='Previsões Teste')
    plt.title(f'Quantidade de Vendas Diárias - Modelo {model_names[i]}')
    plt.xlabel('Data')
    plt.ylabel('Quantidade Vendida')
    plt.gca().xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)

plt.tight_layout()
plt.show()