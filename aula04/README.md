
## Aula 4- Componentização no Flet

Baseado no YouTube – Curso “Flet do Zero ao Avançado”
Vídeo: [Aula 4](https://www.youtube.com/watch?v=nKbNWg7K0wI)

## O que aprendi

- A importância de organizar a interface criando componenetes reutilizáveis
- Como evitar que o page.add() fique enorme e dificil de manter.
- Como criar um componente usando Column e Row.
- Como transformar esse compenente em uma variável (card) e adicioná.lo à página.
- Como usar propriedades como exppand=True para melhorar o layout.
- Como preparar o projeto para crescer de forma organizada.

## Código
O ficheiro main.py utiliza alguns componenetes básicos do Flet
- Column : organiza elementos na vertical.
- Row: organiza elemnetos na horizontal.
- RextFiled: campo onde o utilizador escrev texto
- FloatingActionButton: botão circular usado para ções rápida(ex: adicionar)
Também inclui:
- Criação da função
- Agrupamento dos controles num componente(card)
- Adição do componente à página com page.add(card)
- Execução da aplicação com ft.app(target=main)

## Impressões pessoais

- A compentização permite que o código, fique mais limpo e fácil de entender.
- O Flet permite criar a interface de forma modular, dividindo a aplicação em componentes independentes(como Column, Row, TextFiled e FloatingActionButton). Isso torna o código mis organizado, reutilizãvel e fácil de manter
- Já dá para perceber como isso vai facilitar o desenvolvimento das próximas funcionalidades
