import flet as ft

def main(page: ft.Page):

    def add_task(e):
        print(new_task.value)
        page.add(ft.Checkbox(label=new_task.value)) #inserir as tarefas numa task_list tipo
        new_task.value = ''
        page.update()


    new_task = ft.TextField(hint_text='Insira uma tarefa...', expand=True)  #expandir o campo de texto para ocupar todo o espaço disponivel
    new_button = ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=add_task) 


#criar um card(nome do componente) para agrupar os elementos

    card = ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        new_task,
                        new_button
                    ]
                )
            ]
        )



    page.add(card) #adicionar o card na pagina
    
    
ft.app(target=main)