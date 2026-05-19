def balanceamento_energetico(estado_colonia, energia_total, consumo_total):
#logica que mostra como esta o funcionamento do balanceamento energetico da colonia
    if energia_total >= consumo_total:
        print('A produção está suprindo o consumo corretamente')

    else:
        consumo_total = (
            consumo_total -
            estado_colonia['alojamento']['consumo_kw']
        )

        print('A energia não supre o consumo, módulo de alojamento desligado')

        estado_colonia['alojamento']['status'] = 'OFF'

        if energia_total >= consumo_total:
            print('A energia agora está suprindo o consumo')

        else:
            consumo_total = (
                consumo_total -
                estado_colonia['laboratorio_cientifico']['consumo_kw']
            )

            print('A energia não supre o consumo, módulo de laboratório científico desligado')

            estado_colonia['laboratorio_cientifico']['status'] = 'OFF'

            if energia_total >= consumo_total:
                print('A energia agora supre o consumo')

            else:
                print('Energia em estado crítico, todos os módulos desligados')

                estado_colonia['suporte_vida']['status'] = 'OFF'