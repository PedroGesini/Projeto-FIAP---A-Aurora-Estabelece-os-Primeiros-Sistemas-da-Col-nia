import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


# grafico que mostra dados da previsão da energia eolica da colonia
# (usa o regressao.py)

def criar_grafico_previsao(
    historico_vento,
    historico_eolica,
    vento_atual,
    previsao
):

    # Carregar imagem
    imagem_fundo = mpimg.imread(
        "assets/image.png"
    )

    # Criar gráfico
    fig, ax = plt.subplots(figsize=(11, 6))

    # Fundo com imagem
    ax.imshow(
        imagem_fundo,
        extent=[
            min(historico_vento) - 2,
            max(historico_vento) + 2,
            min(historico_eolica) - 5,
            max(historico_eolica) + 10
        ],
        aspect="auto",
        alpha=0.95
    )

    # Criando linha contínua da regressão
    x_linha = np.linspace(
        min(historico_vento) - 2,
        max(historico_vento) + 2,
        100
    )

    # Fórmula da reta
    coeficiente_angular = (
        (historico_eolica[-1] - historico_eolica[0]) /
        (historico_vento[-1] - historico_vento[0])
    )

    intercepto = historico_eolica[0] - (
        coeficiente_angular * historico_vento[0]
    )

    y_linha = coeficiente_angular * x_linha + intercepto

    # Linha completa da regressão
    ax.plot(
        x_linha,
        y_linha,
        color="purple",
        linewidth=4,
        label="Linha de previsão"
    )

    # Pontos do histórico
    ax.scatter(
        historico_vento,
        historico_eolica,
        color="white",
        s=100,
        edgecolors="purple",
        linewidths=2,
        label="Dados históricos"
    )

    # Ponto da previsão
    ax.scatter(
        vento_atual,
        previsao,
        color="cyan",
        s=150,
        edgecolors="white",
        linewidths=3,
        label=f"Energia prevista: {previsao:.2f} kW"
    )

    # Texto da previsão
    ax.text(
        vento_atual,
        previsao + 1,
        f"{previsao:.2f} kW",
        color="cyan",
        fontsize=12,
        fontweight="bold"
    )

    # Título
    ax.set_title(
        "PREVISÃO DE ENERGIA EÓLICA",
        color="white",
        fontsize=18,
        fontweight="bold"
    )

    # Eixo X
    ax.set_xlabel(
        "Velocidade do vento (km/h)",
        color="white",
        fontsize=12
    )

    # Eixo Y
    ax.set_ylabel(
        "Previsão energia gerada (kW)",
        color="white",
        fontsize=12
    )

    # Cor dos números
    ax.tick_params(colors="white")

    # Grade
    ax.grid(
        True,
        color="white",
        linestyle="--",
        linewidth=0.9,
        alpha=0.7
    )

    # Legenda
    legenda = ax.legend(
        facecolor="black",
        edgecolor="black"
    )

    for texto in legenda.get_texts():
        texto.set_color("white")

    # Fundo externo
    fig.patch.set_facecolor("black")

    plt.show()