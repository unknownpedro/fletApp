import flet as ft
import calculator as cal

num = 0
type = str
def main(page: ft.Page):
    page.title = "Calculator"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=280)

    def num_one(e):
        txt_number.value = int(txt_number.value)
        if (txt_number.value == 0):
            txt_number.value = 1
        else:
            txt_number.value = str(txt_number.value)
            txt_number.value = txt_number.value + "1"
        page.update()

    def num_two(e):
        txt_number.value = int(txt_number.value)
        if (txt_number.value == 0):
            txt_number.value = 2
        else:
            txt_number.value = str(txt_number.value)
            txt_number.value = txt_number.value + "2"
        page.update()

    def num_three(e):
        txt_number.value = int(txt_number.value)
        if (txt_number.value == 0):
            txt_number.value = 3
        else:
            txt_number.value = str(txt_number.value)
            txt_number.value = txt_number.value + "3"
        page.update()

    def num_four(e):
        txt_number.value = int(txt_number.value)
        if (txt_number.value == 0):
            txt_number.value = 4
        else:
            txt_number.value = str(txt_number.value)
            txt_number.value = txt_number.value + "4"
        page.update()

    def num_five(e):
        txt_number.value = int(txt_number.value)
        if (txt_number.value == 0):
            txt_number.value = 5
        else:
            txt_number.value = str(txt_number.value)
            txt_number.value = txt_number.value + "5"
        page.update()

    def num_six(e):
        txt_number.value = int(txt_number.value)
        if (txt_number.value == 0):
            txt_number.value = 6
        else:
            txt_number.value = str(txt_number.value)
            txt_number.value = txt_number.value + "6"
        page.update()

    def num_seven(e):
        txt_number.value = int(txt_number.value)
        if (txt_number.value == 0):
            txt_number.value = 7
        else:
            txt_number.value = str(txt_number.value)
            txt_number.value = txt_number.value + "7"
        page.update()

    def num_eight(e):
        txt_number.value = int(txt_number.value)
        if (txt_number.value == 0):
            txt_number.value = 8
        else:
            txt_number.value = str(txt_number.value)
            txt_number.value = txt_number.value + "8"
        page.update()

    def num_nine(e):
        txt_number.value = int(txt_number.value)
        if (txt_number.value == 0):
            txt_number.value = 9
        else:
            txt_number.value = str(txt_number.value)
            txt_number.value = txt_number.value + "9"
        page.update()

    def num_zero(e):
        txt_number.value = int(txt_number.value)
        if (txt_number.value == 0):
            txt_number.value = 0
        else:
            txt_number.value = str(txt_number.value)
            txt_number.value = txt_number.value + "0"
        page.update()

    def clearall(e):
        txt_number.value = int(txt_number.value)
        txt_number.value = 0
        txt_number.value = str(txt_number.value)
        page.update()

    def clear(e):
        txt_number.value = txt_number.value[:-1]
        page.update()

    def actionadd(e):
        type = "so"
        txt_number.value = int(txt_number.value)
        num = int(txt_number.value)
        txt_number.value = 0
        txt_number.value = str(txt_number.value)
        page.update()

    def actionsub(e):
        type = "su"
        txt_number.value = int(txt_number.value)
        num = int(txt_number.value)
        txt_number.value = 0
        txt_number.value = str(txt_number.value)
        page.update()

    def actionmult(e):
        type = "mu"
        txt_number.value = int(txt_number.value)
        num = int(txt_number.value)
        txt_number.value = 0
        txt_number.value = str(txt_number.value)
        page.update()

    def actiondiv(e):
        type = "di"
        txt_number.value = int(txt_number.value)
        num = int(txt_number.value)
        txt_number.value = 0
        txt_number.value = str(txt_number.value)
        page.update()

    def rotina():

        page.update()

    page.add(
        ft.Row(
            [
                txt_number,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            [
                ft.FilledTonalButton(text="7", on_click=num_seven),
                ft.FilledTonalButton(text="8", on_click=num_eight),
                ft.FilledTonalButton(text="9", on_click=num_nine),
                ft.FilledTonalButton(text="C", on_click=clear),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            [
                ft.FilledTonalButton(text="4", on_click=num_four),
                ft.FilledTonalButton(text="5", on_click=num_five),
                ft.FilledTonalButton(text="6", on_click=num_six),
                ft.FilledTonalButton(text="+", on_click=actionadd),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            [
                ft.FilledTonalButton(text="1", on_click=num_one),
                ft.FilledTonalButton(text="2", on_click=num_two),
                ft.FilledTonalButton(text="3", on_click=num_three),
                ft.FilledTonalButton(text="-", on_click=actionsub),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
    ft.Row(
        [
            ft.FilledTonalButton(text="0", on_click=num_zero),
            ft.FilledTonalButton(text="CA", on_click=clearall),
            ft.FilledTonalButton(text="/", on_click=actiondiv),
            ft.FilledTonalButton(text="*", on_click=actionmult),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        ),
    ft.Row(
        [
            ft.FilledTonalButton(text="=", on_click=None),
        ],
        alignment = ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(target=main)