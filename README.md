````markdown
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



Relatórios Inteligentes do Sistema

O sistema gera tabelas organizadas automaticamente utilizando a biblioteca Tabulate.

Relatório Geral da Colônia

Exemplo:

╒══════════════════════════╤══════════╤══════════╤══════════════════════════╕
│ Sistema                 │ Status   │ Valor    │ Indicador Operacional   │
╞══════════════════════════╪══════════╪══════════╪══════════════════════════╡
│ Energia solar           │ ON       │ 35       │ Geração solar           │
│ Bateria                 │ ON       │ 60       │ 25%                     │
│ Vento atual             │ ON       │ 12       │ km/h                    │
│ Suporte de vida         │ ON       │ 20       │ 72%                     │
│ Laboratório científico  │ ON       │ 18       │ 1                       │
│ Alojamento              │ ON       │ 10       │ 85%                     │
╘══════════════════════════╧══════════╧══════════╧══════════════════════════╛
````


 Tabela de Dados Energéticos

O sistema também exibe relatórios completos da geração e consumo energético da colônia.

Exemplo:

```text
╒══════════════════════════╤══════════════╕
│ Descrição               │ Valor        │
╞══════════════════════════╪══════════════╡
│ Geração eólica          │ 30.00 kW     │
│ Geração solar           │ 35.00 kW     │
│ Energia da bateria      │ 15.00 kW     │
│ Energia total disponível│ 80.00 kW     │
│ Consumo total módulos   │ 48.00 kW     │
╘══════════════════════════╧══════════════╛
```



 Histórico Climático e Energético

O sistema exibe tabelas contendo o histórico do vento e da geração de energia da colônia.

Exemplo:

```text
╒══════════╤══════════╤══════════╤══════════╤══════════╕
│ Vento 1  │ Vento 2  │ Vento 3  │ Vento 4  │ Vento 5  │
╞══════════╪══════════╪══════════╪══════════╪══════════╡
│ 8.0      │ 10.0     │ 12.0     │ 14.0     │ 16.0     │
╘══════════╧══════════╧══════════╧══════════╧══════════╛
```


Visualização Gráfica

O projeto utiliza gráficos personalizados com Matplotlib para representar:

* produção energética;
* previsão eólica;
* níveis de bateria;
* comportamento energético da colônia;
* análise preditiva da geração eólica.

Os gráficos possuem identidade visual futurista inspirada em sistemas espaciais e monitoramento inteligente de Marte.

O sistema também utiliza:

* fundo gráfico temático;
* visual escuro futurista;
* pontos históricos de energia;
* linha de regressão linear;
* previsão automática da geração energética.


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

Estrutura do Projeto

```bash
📁 Projeto-FIAP-Colonia-Aurora
│
├── 📁 assets
│   └── 🖼️ image.png
│
├── 📁 src
│   ├── 📄 **init**.py
│   ├── 📄 balanceamento_energetico.py
│   ├── 📄 banco_dados_projeto.py
│   ├── 📄 grafico_previsao_eolica.py
│   ├── 📄 regressao.py
│   └── 📄 tabela_relatorio_sistema.py
│
├── 📄 .gitignore
├── 📄 README.md
├── 📄 main.py
└── 📄 requirements.txt

```


Tecnologias Utilizadas

* Python
* Matplotlib
* NumPy
* Scikit-Learn
* Tabulate



 Execução do Projeto

## Clonar o Repositório

```bash
git clone https://github.com/PedroGesini/Projeto-FIAP---A-Aurora-Estabelece-os-Primeiros-Sistemas-da-Col-nia.git
```

---

## Entrar na Pasta do Projeto

```bash
cd Projeto-FIAP---A-Aurora-Estabelece-os-Primeiros-Sistemas-da-Col-nia
```

---

## Instalar as Dependências

```bash
pip install -r requirements.txt
```

---

## Executar o Sistema

```bash
python main.py
```


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


Licença

Projeto desenvolvido para fins acadêmicos e educacionais.


