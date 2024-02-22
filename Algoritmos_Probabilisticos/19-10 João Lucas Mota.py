# Joao Lucas Mota Nogueira da Costa

import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

phi1 = 0.7
phi2 = -0.3
n = 100
X = np.random.normal(0, 1, n)
for t in range(2, n):
    X[t] = phi1 * X[t-1] + phi2 * X[t-2] + np.random.normal(0, 1)

max_lag = 99
acf, confint = sm.tsa.acf(X, nlags=max_lag, fft=False, alpha=0.05)

order = (2, 0, 0)
model = sm.tsa.ARIMA(X, order=order)
results = model.fit()

print("========================== Resultados da serie AR2 ===========================\n")
print(results.summary())

plt.figure(figsize = [15, 8])

plt.subplot(2, 1, 1)
plt.title('Serie Autoregressiva Gerada')
plt.plot(range(max_lag + 1), X, c='green')

plt.subplot(2, 1, 2)
plt.bar(range(max_lag + 1), acf)
plt.title('Função de Autocorrelação (ACF)')

plt.show()

print("\nDe acordo com os resultados dos testes apresentados acima, eh possivel concluir que a serie X gerada, eh sim uma serie autoregressiva de AR 2.")
print("==============================================================================================================================================")