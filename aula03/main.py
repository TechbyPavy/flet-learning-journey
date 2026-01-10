import flet as ft

def main(page: ft.Page):

  # Função chamada ao clicar no botão
    def add_task(e):
        print(new_task.value)
      
  # Campo de texto para inserir tarefas
    new_task = ft.TextField(hint_text='Insira uma tarefa...')

  # Botão flutuante para adicionar tarefas
    new_button = ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=add_task) # Liga o clique à função add_task

  # Adiciona os componenetes à página
    page.add(new_task, new_button)

# Inicializa alicação
ft.app(target=main)
