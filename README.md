🚀 Sistema Inteligente da Colônia Aurora

Projeto acadêmico desenvolvido em Python para simulação inteligente de uma colônia em Marte, utilizando análise energética, lógica de decisão, regressão linear e visualização gráfica.

📚 Sobre o Projeto

O sistema representa o funcionamento inteligente da **Colônia Aurora**, realizando:

* Monitoramento energético da colônia
* Controle de consumo dos módulos
* Análise automática de risco energético
* Desligamento inteligente de módulos não essenciais
* Previsão de geração de energia eólica
* Visualização gráfica dos dados
* Organização hierárquica dos sistemas da colônia


🧠 Funcionalidades

✅ Estruturação de Dados

O sistema utiliza:

* dicionários hierárquicos
* listas
* estruturas organizadas por módulos

Exemplo:

* energia e clima
* suporte à vida
* laboratório científico
* alojamento

✅ Lógica de Decisão

O sistema analisa automaticamente:

* geração energética
* consumo total
* prioridade dos módulos

Exemplo:

 Se o consumo for maior que a geração:

  * módulos menos importantes são desligados
  * suporte à vida é priorizado


✅ Modelagem e Previsão

Foi implementada regressão linear para prever:

* geração futura de energia eólica
* comportamento energético baseado no vento

Biblioteca utilizada:

* Scikit-Learn

✅ Visualização Gráfica

O projeto utiliza:

* Matplotlib
* gráficos personalizados
* visual futurista da colônia


# 🗂️ Estrutura do Projeto

```text
Projeto-FIAP-Colonia-Aurora/
│
├── main.py
├── dados_colonia.py
├── banco_dados_projeto.py
├── tabela_relatorio_sistema.py
├── balanceamento_energetico.py
├── regressao.py
├── grafico_previsao_eolica.py
│
├── README.md
└── requirements.txt
```

⚙️ Tecnologias Utilizadas

* Python
* Matplotlib
* NumPy
* Scikit-Learn
* Tabulate


▶️ Como Executar

 1. Clone o repositório

```bash
git clone https://github.com/PedroGesini/Projeto-FIAP---A-Aurora-Estabelece-os-Primeiros-Sistemas-da-Col-nia.git
```

---

2. Entre na pasta

```bash
cd Projeto-FIAP---A-Aurora-Estabelece-os-Primeiros-Sistemas-da-Col-nia
```


3. Instale as dependências

```bash
pip install -r requirements.txt
```

4. Execute o projeto

```bash
python main.py
```

📊 Exemplo de Funcionalidades

## Sistema de Balanceamento Energético

Entrada:

```text
Energia total = 40 kW
Consumo = 70 kW
```

Saída:

```text
ALERTA: consumo maior que geração
Módulo de alojamento desligado
```

Previsão Eólica

Entrada:

```text
Vento atual = 11 km/h
```

Saída prevista:

```text
≈ 27 kW
```


🎯 Objetivos do Projeto

* Aplicar conceitos de programação
* Estruturar dados de forma eficiente
* Automatizar decisões
* Criar sistemas preditivos
* Simular ambientes inteligentes
