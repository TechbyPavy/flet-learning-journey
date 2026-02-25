import flet as ft

from custom_checkbox import Checkbox # importar a class Checkbox do arquivo custom_checkbox.py

def main(page: ft.Page):
    page.title = "Minhas Tarefas" # nome da pagina
    page.theme_mode = ft.ThemeMode.LIGHT

    page.bgcolor = "#BBD2EC"

    page.window.width = 400 # criar a largura
    page.window.height = 650 # criar a altura
    page.padding = ft.padding.only(top=20, left=20, right=20, bottom=20) # definir as bordas externas

    def add_task(e):
        print(new_task.value)
        task_list.controls.append(Checkbox(new_task.value))  # inserir as tarefas numa task_list tipo...
        new_task.value = ''
        page.update()


    new_task = ft.TextField(hint_text='Insira uma tarefa...', expand=True)
    new_button = ft.FloatingActionButton(icon="add", on_click=add_task)

    task_list = ft.Column()  # nova várivel vai ser :tipo colunas

    card = ft.Column(
        width=400,
            controls=[
                ft.Row(
                    controls=[
                        new_task,
                        new_button
                    ]
                ),
                task_list,
            ]
        )

    
    page.add(card) 
    
    

ft.app(target=main)