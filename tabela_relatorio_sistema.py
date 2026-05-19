from tabulate import tabulate
import banco_dados_projeto as bc
import balanceamento_energetico as be
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