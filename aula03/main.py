import flet as ft

def main(page: ft.Page):

    def add_task(e):
        print(new_task.value)

      # Adiciona um Checkbox na página com o texto digitado
        page.add(ft.Checkbox(label=new_task.value))
      
      # Limpa o campo de texto após adicionar a tarefa
        new_task.value = ''
      
      # Atualiza a interface para mostrar as mudanças
        page.update()

    new_task = ft.TextField(hint_text='Insira uma tarefa...')
    new_button = ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=add_task)

    
    page.add(new_task, new_button)
    
    
ft.app(target=main)
