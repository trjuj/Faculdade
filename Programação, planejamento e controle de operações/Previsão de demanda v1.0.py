import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
from math import sqrt

# Carregando os dados
data = pd.read_csv('Amazon Sale Report.csv', low_memory=False)

# Verificando os nomes das colunas
print(data.columns)

# Garantindo que a coluna 'Date' exista e esteja corretamente nomeada
if 'Date' in data.columns:
    data['Date'] = pd.to_datetime(data['Date'], format='%m-%d-%y')
else:
    raise ValueError("Coluna 'Date' não encontrada no DataFrame")

# Tratando valores NaN
data = data.dropna(subset=['Date', 'Qty'])

# Agregando dados em nível diário
daily_data = data.groupby(data['Date'].dt.date)['Qty'].sum()

# Engenharia de características: Extrair ano, mês, dia da data
daily_data = daily_data.reset_index()
daily_data['Year'] = pd.to_datetime(daily_data['Date']).dt.year
daily_data['Month'] = pd.to_datetime(daily_data['Date']).dt.month
daily_data['Day'] = pd.to_datetime(daily_data['Date']).dt.day

# Usando Ano, Mês e Dia como características
X = daily_data[['Year', 'Month', 'Day']]
y = daily_data['Qty']

# Normalizando características
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Dividindo os dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Invertendo a normalização para o conjunto de treinamento
X_train_inverted = scaler.inverse_transform(X_train)

# Convertendo os valores invertidos de volta para datas
X_train_dates = pd.to_datetime({'year': X_train_inverted[:, 0].astype(int),
                                'month': X_train_inverted[:, 1].astype(int),
                                'day': X_train_inverted[:, 2].astype(int)})





# Inicializando modelos
knn = KNeighborsRegressor(n_neighbors=min(3, len(X_train)))
rf = RandomForestRegressor(n_estimators=150)


# Treinando modelos
knn.fit(X_train, y_train)
rf.fit(X_train, y_train)


# Previsões
y_pred_knn = knn.predict(X_test)
y_pred_rf = rf.predict(X_test)


# Avaliando modelos
rmse_knn = sqrt(mean_squared_error(y_test, y_pred_knn))
rmse_rf = sqrt(mean_squared_error(y_test, y_pred_rf))


print(f'RMSE KNN: {rmse_knn}')
print(f'RMSE Floresta Aleatória: {rmse_rf}')



# Última data no conjunto de dados
last_date = daily_data['Date'].max()

# Criando a data para o próximo dia
next_day = last_date + pd.Timedelta(days=1)

# Preparando as características para a previsão do próximo dia
next_day_features = np.array([[next_day.year, next_day.month, next_day.day]])

# Normalizando as características
next_day_features_scaled = scaler.transform(next_day_features)

# Realizando previsões com cada modelo
next_day_pred_knn = knn.predict(next_day_features_scaled)
next_day_pred_rf = rf.predict(next_day_features_scaled)


# Imprimindo as previsões
print(f'Previsão de demanda para o próximo dia com KNN: {next_day_pred_knn[0]}')
print(f'Previsão de demanda para o próximo dia com Floresta Aleatória: {next_day_pred_rf[0]}')


# Previsões de vendas para o próximo dia para cada modelo
# Calculando datas para as próximas três semanas
future_dates = [last_date + pd.Timedelta(days=x) for x in range(1, 22)]

# Preparando as características para as previsões futuras
future_features = np.array([[date.year, date.month, date.day] for date in future_dates])

# Normalizando as características
future_features_scaled = scaler.transform(future_features)

# Realizando previsões com cada modelo
future_preds_knn = knn.predict(future_features_scaled)
future_preds_rf = rf.predict(future_features_scaled)


# Visualização com linha de tendência e previsões para as próximas três semanas
plt.figure(figsize=(18, 6))
model_names = ['KNN', 'Floresta Aleatória']
dates = mdates.date2num(pd.to_datetime(daily_data['Date']))  # Convertendo datas para números

# Calculando a linha de tendência
z = np.polyfit(dates, y, 1)
p = np.poly1d(z)

# Criando um plot para cada modelo
plt.scatter(X_scaled, y, color='blue', alpha=0.7)
future_dates_num = mdates.date2num(future_dates)  # Convertendo futuras datas para formato numérico
plt.title('Quantidade de Vendas Diárias')
plt.xlabel('Data')
plt.ylabel('Quantidade Vendida')
plt.gca().xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()