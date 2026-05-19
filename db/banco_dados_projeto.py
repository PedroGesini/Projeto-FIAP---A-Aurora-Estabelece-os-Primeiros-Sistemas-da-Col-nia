from tabulate import tabulate


def banco_dados(estado_colonia):

    dados_modulos = [

        [
            "Energia solar",
            "ON",
            estado_colonia["energia_clima"]["geracao_solar_kw"],
            "Geração solar"
        ],

        [
            "Bateria",
            "ON",
            estado_colonia["energia_clima"]["capacidade_bateria_kwh"],
            f'{estado_colonia["energia_clima"]["nivel_bateria_pct"]}%'
        ],

        [
            "Vento atual",
            "ON",
            estado_colonia["energia_clima"]["vento_atual_kmh"],
            "km/h"
        ],

        [
            "Suporte de vida",
            estado_colonia["suporte_vida"]["status"],
            estado_colonia["suporte_vida"]["consumo_kw"],
            f'{estado_colonia["suporte_vida"]["recursos_vitais_pct"]}%'
        ],

        [
            "Laboratório científico",
            estado_colonia["laboratorio_cientifico"]["status"],
            estado_colonia["laboratorio_cientifico"]["consumo_kw"],
            estado_colonia["laboratorio_cientifico"]["experimento_critico"]
        ],

        [
            "Alojamento",
            estado_colonia["alojamento"]["status"],
            estado_colonia["alojamento"]["consumo_kw"],
            f'{estado_colonia["alojamento"]["taxa_conforto_pct"]}%'
        ]
    ]

    print("\n--- RELATÓRIO GERAL DA COLÔNIA ---\n")

    print(tabulate(
        dados_modulos,
        headers=[
            "Sistema",
            "Status",
            "Valor",
            "Indicador Operacional"
        ],
        tablefmt="fancy_grid"
    ))