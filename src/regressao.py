
#calculo da previsão da energia eolica da colonia
def prever_energia_eolica(estado_colonia):
    from sklearn.linear_model import LinearRegression
    import numpy as np
    historico_vento = estado_colonia["energia_clima"]["historico_vento"]
    historico_eolica = estado_colonia["energia_clima"]["historico_eolica"]

    vento_atual = estado_colonia["energia_clima"]["vento_atual_kmh"]

    # Transformando listas em arrays
    X = np.array(historico_vento).reshape(-1, 1)
    y = np.array(historico_eolica)

    # Criando modelo
    modelo = LinearRegression()

    # Treinando modelo
    modelo.fit(X, y)

    # Fazendo previsão
    previsao = modelo.predict([[vento_atual]])

    return round(previsao[0], 2)