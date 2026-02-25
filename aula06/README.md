## Aula 6 

Baseado no YouTube – Curso “Flet do Zero ao Avançado”
Vídeo: [Aula 6](https://www.youtube.com/watch?v=B5af9vgnQiI&list=PLjEMBqp7RZOyz7d6JYdkvWBKkU8pH1AUo&index=6)

## O que aprendi

- Como criar um componente personalizado no Flet usando classes.
- Aprendi a criar cuma classe e a trabalhar com propriedades, visibilidades e ícones
- Como estruturar um arquivo separado (custom_checkbox.py)
- Como construir um checkbox personalizado contendo:
    - Texto exibido (Text)
    - Campo de edição oculto(TextField)
    - Botão de editar (IconButton)
    - Botão de salvar (IconButton)
    - Botão de deletar (IconButton)
    - Checkbox padrão do Flet

- Como montar todos esses elementos dentro de uma Row.
- Como importar e usar esse componente no main.py.
- Importância da indentação correta em Python(o instrutor corrige isso no final da aula).


## Código Utilizado

No custom_checkbox.py: 

- class Checkbox(ft.Row):

- self.text_view = ft.Text(text)

- self.text_edit = ft.TextField(value=text, visible=False)

- self.edit_button = ft.IconButton(icon=ft.icons.EDIT, on_click=self.edit)

- self.save_button = ft.IconButton(icon=ft.icons.SAVE, on_click=self.save, visible=False)

- self.delete_button = ft.IconButton(icon=ft.icons.DELETE, on_click=self.delete)

- self.controls = [ ft.Checkbox(), self.text_view, self.text_edit self.edit_button, self.save_button, self.delete_button ]

- def edit(self, e): pass

- def save(self, e): pass

- def delete(self, e): pass

No main.py: 

- from custom_checkbox import Checkbox
- task_list.controls.append(Checkbox(new_task.value))


## Impressões pessoais

- Esta aula ajudou-me a percber melhor como criar icones nas aplicações e como control~´a-los, esopecialmente os botões de delete,edit e add.

- Gostei de ver como podemos criar funcionalidades numa nova classe e depois importá-las para a aplicação, deixando o código mais limpo, organizado e modular.

- Tive de fazer algumas adpatações ao código, porque não estou a usar exatamnete a mesma versão do Flet que o professor utiliza no Youtube.

- O Copilot foi uma grande ajuda para a organizar a informações, esclarecer dúvidas e encontrar alternativas funcionais quando algo não correspondia ao que aparecia no video.
    

---
---

## Lesson 6

Based on Youtube : Course "Flet do Zero Avançado".
Video : [Aula 6](https://www.youtube.com/watch?v=B5af9vgnQiI&list=PLjEMBqp7RZOyz7d6JYdkvWBKkU8pH1AUo&index=6)

## What I learned

- How to create a custom component in Flet using classes.
- How to build a class and work with properties, visiblity settings and icons.
- How to structure a separete file(custom_checkbox-py) to keep the project organised.

- How to build a custom checkbox containing:
    - Displayed text (Text)
    - Hidden edit field (Text Field)
    - EditButton (IconButton)
    - Save button (IconButton)
    - Delete button (IconButton)
    - Standard Flet checkbox

- How to assbemle all these elements inside a "Row"
- How to import and use this component inside main.py.
- The importancve of correct indentation in Python(teh instructor fizes this at the end of the lesson)

## Code used

In *custom_checkbox.py*:
class Checkbox(ft.Row):

- self.text_view = ft.Text(text)

- self.text_edit = ft.TextField(value=text, visible=False)

- self.edit_button = ft.IconButton(icon=ft.icons.EDIT, on_click=self.edit)

- self.save_button = ft.IconButton(icon=ft.icons.SAVE, on_click=self.save, visible=False)

- self.delete_button = ft.IconButton(icon=ft.icons.DELETE, on_click=self.delete)

- self.controls = [ ft.Checkbox(), self.text_view, self.text_edit, self.edit_button, self.save_button, self.delete_button ]

- def edit(self, e): pass

- def save(self, e): pass

- def delete(self, e): pass

In *main.py*:
- from custom_checkbox import Checkbox

- task_list.controls.append(Checkbox(new_task.value))

## Personal impressions

- This lesson helped me better understand how to create icons in applications and how to control them, especially the delet, edit and buttons.

- I liked seeing how we can create functionality inside a new class and then import it into the application, keeping the code cleaner, more organised, and more modular.

- I had to make some adjustments to the code because I'm not using exactly the same version of Flet as the instrutor on Youtube.

- Copilot was a great help in organising the information, clarifying doubts, and finding functional alternatiuves when something didn´t match what appeared in the video. 



