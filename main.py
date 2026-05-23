from tabulate import tabulate
from src import regressao as rg
from src import banco_dados_projeto as bd
from src import balanceamento_energetico as be
from src import grafico_previsão_eolica as gpe
#cria tabela mostrando o relatorio do sistema da colonia
def tabela_relatorio_sistema(
        estado_colonia,
        geracao_eolica,
        geracao_solar,
        energia_bateria,
        energia_total,
        consumo_total
):

    bc.banco_dados(estado_colonia)

    dados_energia = [

        ["Geração eólica", f"{geracao_eolica:.2f} kW"],
        ["Geração solar", f"{geracao_solar:.2f} kW"],
        ["Energia da bateria", f"{energia_bateria:.2f} kW"],
        ["Energia total disponível", f"{energia_total:.2f} kW"],
        ["Consumo total dos módulos", f"{consumo_total:.2f} kW"],
    ]

    print("\n------| DADOS DE ENERGIA |------\n")

    print(tabulate(
        dados_energia,
        headers=["Sistema", "Valor"],
        tablefmt="fancy_grid"
    ))

    be.balanceamento_energetico(
        estado_colonia,
        energia_total,
        consumo_total
    )

    input("\nPressione ENTER para voltar ao menu:")
#variaveis da colonia
estado_colonia = bd.variaveis_colonia()

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
            previsao = rg.prever_energia_eolica(estado_colonia) #regressão.py

            historico_vento = estado_colonia["energia_clima"]["historico_vento"]
            historico_eolica = estado_colonia["energia_clima"]["historico_eolica"]
            vento_atual = estado_colonia["energia_clima"]["vento_atual_kmh"]
            dados_previsao = [
                ["Histórico do vento", historico_vento],
                ["Histórico eólico", historico_eolica],
                ["Vento atual", f"{vento_atual} km/h"]
            ]
            historico_vento = estado_colonia["energia_clima"]["historico_vento"]

            dados_vento = [
                historico_vento
            ]
            print("\n--- HISTORICO DO VENTO ---")
            print(tabulate(
                dados_vento,
                headers=[
                    "Verficação 1","Verficação 2","Verficação 3","Verficação 4","Verficação 5"
                ],
                tablefmt="fancy_grid"
            ))

            print("\n--- PREVISÃO DE ENERGIA EÓLICA ---")
            print(f"Vento atual: {vento_atual} km/h")
            print(f"Previsão estimada de energia eólica: {previsao:.2f} kW")
            input("\nPressione ENTER para exibir o gráfico:")

            gpe.criar_grafico_previsao(historico_vento,historico_eolica,vento_atual,previsao) #grafico_previsão_eolica.py

        case 0:
            print("\nSISTEMA ENCERRADO!")
            break
