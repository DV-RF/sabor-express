# 🛎️ Sabor Express - Sistema de Gestão de Restaurantes

![Status](https://img.shields.io/badge/Status-Concluído-success)
![Python](https://img.shields.io/badge/Python-3.x-blue)

O **Sabor Express** é uma aplicação de terminal (CLI) em Python para o gerenciamento de restaurantes. O projeto base foi desenvolvido durante o curso "Crie sua primeira aplicação em Python" da **Alura**. 

No entanto, **este repositório vai além do escopo original do curso**. O código foi expandido e aprimorado com validações de segurança (Cyber-aware) e sanitização de dados, garantindo que o sistema não quebre com inputs maliciosos ou incorretos.

## 🚀 Funcionalidades

* **Cadastro Seguro de Restaurantes:** * Bloqueio de caracteres especiais e números (`.isalpha()`).
  * Validação de tamanho de string (mínimo de 2 e máximo de 30 caracteres).
  * Prevenção contra colisão de dados (impede o cadastro de nomes duplicados).
  * Sanitização invisível de inputs (uso de `.strip()` e `.replace()`).
* **Listagem Dinâmica:** Exibição dos restaurantes em formato de tabela alinhada.
* **Filtro de Busca:** Capacidade de filtrar os restaurantes listados pela sua categoria.
* **Alternância de Estado:** Ativar ou desativar o status operacional do restaurante de forma interativa.
* **Menu Persistente:** O sistema roda em um loop contínuo e limpa o terminal a cada ação para melhor visualização (`os.system('cls')`).

## 🛠️ Tecnologias e Conceitos Utilizados

* **Python 3**
* **Estruturas de Dados:** Dicionários e Listas.
* **Controle de Fluxo:** Loops (`for`, `while True`) e Condicionais.
* **Clean Code:** Funções modulares com responsabilidades únicas e `docstrings` documentando Entradas (Inputs) e Saídas (Outputs).
* **Tratamento de Exceções:** Uso de `try-except` para evitar quebras no menu principal.

## 💻 Como rodar o projeto localmente

1. Clone este repositório em sua máquina:
  git clone https://github.com/DV-RF/sabor-express.git
