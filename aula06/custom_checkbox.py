import flet as ft

class Checkbox(ft.Row): # Definir a class Checkbox e as propriedades dela
    def __init__(self, text):
        super().__init__()  # Chamar o construtor da classe pai (ft.Row)
        self.text_view = ft.Text(text)  # Criar um componente de texto 
        self.text_edit = ft.TextField(value=text, visible=False) # Componente de edição de texto e receber o text
        self.edit_button = ft.IconButton(icon="edit", on_click=self.edit)  # Botão de edição
        self.save_button = ft.IconButton(icon="save", on_click=self.save, visible=False)  # Botão de salvar, só aparece ao editar

        self.delete_button = ft.IconButton(icon="delete", on_click=self.delete)

        self.controls = [  # Adicionar os controles ao Row
            ft.Checkbox(),
            self.text_view,
            self.text_edit,
            self.edit_button,
            self.save_button,
            self.delete_button,

            
        ]
        
    def edit(self, e): # editar a tarefa
        
        self.page.update()


    def save(self, e): # salvar a tarefa
        
        self.page.update()
        

    def delete(self, e): # deletar a tarefa
        
        self.page.update()
        

