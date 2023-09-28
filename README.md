# Projeto Python ProFiler! :plate_with_cutlery:
Projeto desenvolvido por mim durante o curso de Desenvolvimento Web na Trybe. Divulgado aqui como portfólio de aprendizado.

<details>
<summary><strong>Objetivos do projeto:</strong></summary>
 
  * Trabalhar com uma aplicação com uma interface de linha de comando (CLI) que recebe como entrada um caminho (diretório ou arquivo) e gera um relatório com informações sobre o caminho informado.
  * Corrigir os bugs e implementar os testes para garantir que a aplicação funcione corretamente.
  * Verificar se sou capaz de:
    * Encontrar bugs no código de uma aplicação escrita em Python.
    * Corrigir bugs no código de uma aplicação escrita em Python.
    * Criar testes para uma aplicação escrita em Python.
    * Utilizar o pytest para criar testes automatizados em uma aplicação escrita em Python.
</details>
<details>
<summary><strong> Requisitos do projeto:</strong></summary>

  *  Implementar testes para a classe `Ingredient`, que se encontra no módulo `src/models/ingredient.py`.
  *  Implementar testes para a classe `Dish`, que se encontra no módulo `src/models/dish.py`.
  *  Implementar a classe `MenuData` que fará todo o mapeamento de pratos e ingredientes baseado nos arquivo csv disponibilizado. Ela se encontra no módulo `src/services/menu_data.py`.
  *  Implementar o método `get_main_menu` dentro da classe `MenuBuilder`, que gera um `DataFrame` com os cardápios. Ele se encontra no arquivo `src/services/menu_builder.py`.
</details>
  
## Rodando o projeto localmente

Para rodar o projeto em sua máquina, abra seu terminal, crie um diretório no local de sua preferência com o comando `mkdir` e acesse o diretório criado com o comando `cd`:

```bash
mkdir meu-diretorio &&
cd meu-diretorio
```

Clone o projeto com o comando `git clone`:

```bash
git clone git@github.com:marcosadrianoti/tb-restaurant-orders.git
```

Acesse o diretório do projeto com o comando `cd`:

```bash
cd tb-restaurant-orders
```

crie o ambiente virtual:
```bash
python3 -m venv .venv
```

Ative o ambiente virtual:
```bash
source .venv/bin/activate
```

Instale as dependências no ambiente virtual:
```bash
python3 -m pip install -r dev-requirements.txt
```
