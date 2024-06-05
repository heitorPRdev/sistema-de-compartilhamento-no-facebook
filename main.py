import flet as ft

def main(page: ft.Page):
    def closeBunner(e):
        page.banner.open = False
        page.update()
    
    
    page.banner  = ft.Banner(
        bgcolor='blue',
        leading=ft.Icon(ft.icons.CHECK_CIRCLE_OUTLINE, color=ft.colors.BLUE_200,size=40),
        content = ft.Text(
            'Você enviou com sucesso a sua mensagem para as pessoas'
        ),
        actions=[
            ft.TextButton("Ok",on_click=closeBunner),
        ],
    )
    def funbtn_enviar(e):
        #usar o selenium aqui
        
        page.banner.open = True
        page.update()

    page.title = 'Compartilhamento no facebook'
    text_info1 = ft.Text('Coloque a mensagem aqui:',size=16)
    texto_compar_input = ft.TextField()
    btn_enviar = ft.ElevatedButton('Enviar',bgcolor='green',color='black', on_click=funbtn_enviar)

    page.add(
        text_info1,
        texto_compar_input,
        btn_enviar
    )

ft.app(target=main)