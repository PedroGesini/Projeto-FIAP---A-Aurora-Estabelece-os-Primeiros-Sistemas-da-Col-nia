Sistema Inteligente da Colônia Aurora

Projeto acadêmico desenvolvido em Python com foco em automação, análise energética e tomada de decisão inteligente em uma colônia espacial simulada em Marte.

O sistema integra monitoramento energético, previsão de geração eólica, controle inteligente dos módulos da colônia e análise automática de risco operacional.


Visão Geral

A proposta do projeto é representar o funcionamento de uma colônia autônoma em Marte, capaz de monitorar seus recursos energéticos e tomar decisões automaticamente para garantir estabilidade e sobrevivência dos módulos essenciais.

Durante a execução, o sistema realiza:

* análise do consumo energético;
* monitoramento climático;
* previsão de energia eólica;
* desligamento inteligente de módulos;
* geração de relatórios;
* visualização gráfica dos dados da colônia.

O projeto foi estruturado utilizando conceitos fundamentais de programação, organização hierárquica de dados e modelagem preditiva.


Principais Funcionalidades

Gerenciamento Energético Inteligente

O sistema compara automaticamente:

* geração total de energia;
* consumo total da colônia;
* prioridade dos módulos.

Caso o consumo ultrapasse a geração disponível, módulos secundários são desligados automaticamente para preservar os sistemas críticos.

Exemplo:

* alojamento pode ser desativado;
* laboratório científico pode entrar em modo OFF;
* suporte à vida permanece ativo como prioridade máxima.


Previsão de Energia Eólica

Utilizando regressão linear com Scikit-Learn, o sistema estima a geração futura de energia baseada na velocidade atual do vento.

Exemplo:

| Vento Atual | Energia Prevista |
| ----------- | ---------------- |
| 8 km/h      | 20 kW            |
| 12 km/h     | 30 kW            |
| 16 km/h     | 40 kW            |

Visualização Gráfica

O projeto utiliza gráficos personalizados com Matplotlib para representar:

* produção energética;
* previsão eólica;
* níveis de bateria;
* comportamento energético da colônia.

Os gráficos possuem identidade visual inspirada em sistemas futuristas e monitoramento espacial.



Organização Hierárquica de Dados

A estrutura da colônia foi organizada utilizando:

* dicionários;
* listas;
* módulos hierárquicos;
* estruturas separadas por setores.

Exemplo da arquitetura:

```python
estado_colonia = {
    "energia_clima": {},
    "suporte_vida": {},
    "laboratorio_cientifico": {},
    "alojamento": {}
}
```

---

# Estrutura do Projeto

```bash
Projeto-FIAP-Colonia-Aurora/
│
├── main.py
├── balanceamento_energetico.py
├── banco_dados_projeto.py
├── regressao.py
├── grafico_previsão_eolica.py
├── tabela_relatorio_sistema.py
│
├── README.md
└── requirements.txt
```

Tecnologias Utilizadas

* Python
* Matplotlib
* NumPy
* Scikit-Learn
* Tabulate

---

Execução do Projeto

Clonar o Repositório

```bash
git clone https://github.com/PedroGesini/Projeto-FIAP---A-Aurora-Estabelece-os-Primeiros-Sistemas-da-Col-nia.git
```

---

Entrar na Pasta do Projeto

```bash
cd Projeto-FIAP---A-Aurora-Estabelece-os-Primeiros-Sistemas-da-Col-nia
```


Instalar as Dependências

```bash
pip install -r requirements.txt
```

Executar o Sistema

```bash
python main.py
```

---

Simulação do Sistema

Cenário Energético

Entrada

```python
Energia Total = 40 kW
Consumo Total = 70 kW
```

Resultado

```python
ALERTA ENERGÉTICO
Consumo superior à geração disponível.

→ Módulo de alojamento desligado.
→ Sistema de suporte à vida preservado.
```

---

Objetivos do Projeto

Este projeto foi desenvolvido com o objetivo de:

* aplicar conceitos de programação em Python;
* praticar estruturação hierárquica de dados;
* desenvolver lógica computacional;
* criar sistemas automatizados de decisão;
* implementar modelagem preditiva;
* simular ambientes inteligentes e autônomos.


Desenvolvimento

Projeto desenvolvido como atividade acadêmica da FIAP, integrando conceitos de:

* lógica de programação;
* automação;
* análise de dados;
* inteligência computacional;
* sistemas inteligentes.


# Possíveis Melhorias Futuras

* integração com banco de dados real;
* sistema de alertas em tempo real;
* dashboard web interativo;
* inteligência artificial para tomada de decisão;
* monitoramento via API;
* sistema completo de telemetria espacial.

Licença

Projeto desenvolvido para fins acadêmicos e educacionais.
