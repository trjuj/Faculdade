# Joao Lucas Mota Nogueira da Costa

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf
import matplotlib.dates as mdates
import statsmodels.api as sm

petr = yf.download("PETR4.SA", start="2023-01-01", end="2023-11-09")
pd.DataFrame.to_csv(petr, "PETR4.csv")
pbDF = pd.read_csv("PETR4.csv", sep=',')
dates = mdates.date2num(pd.to_datetime(pbDF['Date']))
close_val = pbDF['Close']

tam_media = 10
media_movel = close_val.rolling(window=tam_media).mean()

train_size = int(len(pbDF) * 0.94)
train, test = pbDF[:train_size], pbDF[train_size:]
order = (2, 0, 0)
seasonal_order = (1, 1, 1, 12)
model = sm.tsa.SARIMAX(train['Close'], order=order, seasonal_order=seasonal_order)
results = model.fit()

prev = results.forecast(steps=len(test))

plt.figure(figsize=(18,12))

plt.subplot(2,1,1)
plt.gca().xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=mdates.SU,interval=1))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m'))
plt.ylabel("Valor fechado no dia")
plt.grid(True)
plt.xticks(rotation=45)
plt.plot(dates, close_val, c='green', label='Dados')
plt.legend()
plt.title("Base de dados valores PETR4 01/01 a 09/11")

plt.subplot(2,1,2)
plt.plot(train.index, train['Close'], label='Treinamento')
plt.plot(test.index, test['Close'], label='Teste')
plt.plot(test.index, prev, label='Previsões', color='red')
plt.xlabel('Data')
plt.ylabel('Preço de Fechamento')
plt.legend()

plt.show()