from tabulate import tabulate
import random

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

def variaveis_colonia():
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
            "experimento_critico": random.randint(0, 1),
        },

        "alojamento": {
            "status": "ON",
            "consumo_kw": random.randint(1, 15),
            "taxa_conforto_pct": random.randint(50, 100),
        },
    }
    return estado_colonia