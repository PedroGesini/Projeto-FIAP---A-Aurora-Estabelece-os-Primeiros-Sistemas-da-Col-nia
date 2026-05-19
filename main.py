import random
from tabulate import tabulate
import balanceamento_energetico as be
import grafico_previsão_eolica as gpe
import banco_dados_projeto as bd
from regressao import prever_energia_eolica

#variaveis da colonia
estado_colonia = {
    "energia_clima": {
        "geracao_solar_kw": random.randint(10, 40),
        "capacidade_bateria_kwh": random.randint(30, 80),
        "nivel_bateria_pct": random.randint(10, 30),
        "vento_atual_kmh": random.randint(6, 12),
        "historico_vento": [8.0, 10.0, 12.0, 14.0, 16.0],
        "historico_eolica": [20.0, 25.0, 30.0, 35.0, 40.0],
    },

    "suporte_vida": {
        "status": "ON",
        "consumo_kw": random.randint(15, 25),
        "recursos_vitais_pct": random.randint(65, 75),
    },

    "laboratorio_cientifico": {
        "status": "ON",
        "consumo_kw": random.randint(15, 20),
        "experimento_critico": random.randint(0,1),
    },

    "alojamento": {
        "status": "ON",
        "consumo_kw": random.randint(1, 15),
        "taxa_conforto_pct": random.randint(50, 100),
    },
}

while True:
    #calculo da geração eolica
    geracao_eolica = estado_colonia["energia_clima"]["vento_atual_kmh"] * 2.5
    geracao_solar = estado_colonia["energia_clima"]["geracao_solar_kw"]

    bateria = estado_colonia["energia_clima"]["nivel_bateria_pct"]
    capacidade_bateria = estado_colonia["energia_clima"]["capacidade_bateria_kwh"]

    energia_bateria = capacidade_bateria * (bateria / 100)
    energia_total = geracao_eolica + geracao_solar + energia_bateria

    consumo_total = (
        estado_colonia["suporte_vida"]["consumo_kw"]
        + estado_colonia["laboratorio_cientifico"]["consumo_kw"]
        + estado_colonia["alojamento"]["consumo_kw"]
    )
    #escolha do usuario
    try:
        opcao = int(input(
            "\nEscolha uma das opções abaixo:\n\n"
            "1 - Exibir relatório do sistema\n"
            "2 - Exibir dados do balanceamento energético da colônia\n"
            "3 - Exibir previsão eolica:\n"
            "0 - Encerrar sistema\n\n"
            "DIGITE A OPÇÃO: "
        ))

    except ValueError:
        print("\n Opção inválida")
        continue

    match opcao:
        case 1:
            bd.banco_dados(estado_colonia)  #banco_dados_projeto.py
            input("Pressione ENTER para voltar para o menu:")
        case 2:
            # tabela de dados de energia
            dados_energia = [
                ["Geração eólica", f"{geracao_eolica:.2f} kW"],
                ["Geração solar", f"{geracao_solar:.2f} kW"],
                ["Energia da bateria", f"{energia_bateria:.2f} kW"],
                ["Energia total disponível", f"{energia_total:.2f} kW"],
                ["Consumo total dos módulos", f"{consumo_total:.2f} kW"],
            ]

            print("\n--- DADOS DE ENERGIA ---")
            print(tabulate(
                dados_energia,
                headers=["Descrição", "Valor"],
                tablefmt="fancy_grid"
            ))

            be.balanceamento_energetico(estado_colonia,energia_total,consumo_total) #balanceamento_energetico.py
        case 3:
            previsao = prever_energia_eolica(estado_colonia) #regressão.py

            historico_vento = estado_colonia["energia_clima"]["historico_vento"]
            historico_eolica = estado_colonia["energia_clima"]["historico_eolica"]
            vento_atual = estado_colonia["energia_clima"]["vento_atual_kmh"]

            print("\n--- PREVISÃO DE ENERGIA EÓLICA ---")
            print(f"Vento atual: {vento_atual} km/h")
            print(f"Previsão estimada de energia eólica: {previsao:.2f} kW")

            input("\nPressione ENTER para exibir o gráfico:")

            gpe.criar_grafico_previsao(historico_vento,historico_eolica,vento_atual,previsao) #grafico_previsão_eolica.py

        case 0:
            print("\nSISTEMA ENCERRADO!")
            break