import flet as ft
import calculator as cal


def main(page: ft.Page):
    page.title = "Calculator"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=330)

    num = 0
    tipo = ""
    total = 0

    def num_one(e):
        txt_number.value = int(txt_number.value)
        if txt_number.value == 0:
            txt_number.value = 1
        else:
            txt_number.value = str(txt_number.value)
            txt_number.value = txt_number.value + "1"
        page.update()

    def num_two(e):
        txt_number.value = int(txt_number.value)
        if txt_number.value == 0:
            txt_number.value = 2
        else:
            txt_number.value = str(txt_number.value)
            txt_number.value = txt_number.value + "2"
        page.update()

    def num_three(e):
        txt_number.value = int(txt_number.value)
        if txt_number.value == 0:
            txt_number.value = 3
        else:
            txt_number.value = str(txt_number.value)
            txt_number.value = txt_number.value + "3"
        page.update()

    def num_four(e):
        txt_number.value = int(txt_number.value)
        if txt_number.value == 0:
            txt_number.value = 4
        else:
            txt_number.value = str(txt_number.value)
            txt_number.value = txt_number.value + "4"
        page.update()

    def num_five(e):
        txt_number.value = int(txt_number.value)
        if txt_number.value == 0:
            txt_number.value = 5
        else:
            txt_number.value = str(txt_number.value)
            txt_number.value = txt_number.value + "5"
        page.update()

    def num_six(e):
        txt_number.value = int(txt_number.value)
        if txt_number.value == 0:
            txt_number.value = 6
        else:
            txt_number.value = str(txt_number.value)
            txt_number.value = txt_number.value + "6"
        page.update()

    def num_seven(e):
        txt_number.value = int(txt_number.value)
        if txt_number.value == 0:
            txt_number.value = 7
        else:
            txt_number.value = str(txt_number.value)
            txt_number.value = txt_number.value + "7"
        page.update()

    def num_eight(e):
        txt_number.value = int(txt_number.value)
        if txt_number.value == 0:
            txt_number.value = 8
        else:
            txt_number.value = str(txt_number.value)
            txt_number.value = txt_number.value + "8"
        page.update()

    def num_nine(e):
        txt_number.value = int(txt_number.value)
        if txt_number.value == 0:
            txt_number.value = 9
        else:
            txt_number.value = str(txt_number.value)
            txt_number.value = txt_number.value + "9"
        page.update()

    def num_zero(e):
        txt_number.value = int(txt_number.value)
        if txt_number.value == 0:
            txt_number.value = 0
        else:
            txt_number.value = str(txt_number.value)
            txt_number.value = txt_number.value + "0"
        page.update()

    def clearer(e):
        txt_number.value = int(txt_number.value)
        txt_number.value = 0
        txt_number.value = str(txt_number.value)
        page.update()

    def clear(e):
        txt_number.value = txt_number.value[:-1]
        page.update()

    def actadd(e):
        nonlocal num, tipo
        tipo = "so"
        txt_number.value = int(txt_number.value)
        num = int(txt_number.value)
        txt_number.value = 0
        txt_number.value = str(txt_number.value)
        page.update()

    def actsub(e):
        nonlocal num, tipo
        tipo = "su"
        txt_number.value = int(txt_number.value)
        num = int(txt_number.value)
        txt_number.value = 0
        txt_number.value = str(txt_number.value)
        page.update()

    def actmult(e):
        nonlocal num, tipo
        tipo = "mu"
        txt_number.value = int(txt_number.value)
        num = int(txt_number.value)
        txt_number.value = 0
        txt_number.value = str(txt_number.value)
        page.update()

    def actdiv(e):
        nonlocal num, tipo
        tipo = "di"
        txt_number.value = int(txt_number.value)
        num = int(txt_number.value)
        txt_number.value = 0
        txt_number.value = str(txt_number.value)
        page.update()

    def igual(e):
        nonlocal num, tipo, total
        num2 = float(txt_number.value)
        if tipo == "so":
            total = cal.add(num, num2)
        elif tipo == "su":
            total = cal.sub(num, num2)
        elif tipo == "mu":
            total = cal.multi(num, num2)
        elif tipo == "di":
            total = cal.div(num, num2)
        else:
            print("Operação desconhecida:", tipo)
        txt_number.value = str(total)
        page.update()

        num = total
        tipo = ""
        total = 0
        txt_number.value = 0

    page.add(
        ft.Row(
            [
                txt_number,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            [
                ft.FilledTonalButton(text="7", on_click=num_seven, width=75),
                ft.FilledTonalButton(text="8", on_click=num_eight, width=75),
                ft.FilledTonalButton(text="9", on_click=num_nine, width=75),
                ft.FilledTonalButton(text="C", on_click=clear, width=75),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            [
                ft.FilledTonalButton(text="4", on_click=num_four, width=75),
                ft.FilledTonalButton(text="5", on_click=num_five, width=75),
                ft.FilledTonalButton(text="6", on_click=num_six, width=75),
                ft.FilledTonalButton(text="+", on_click=actadd, width=75),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            [
                ft.FilledTonalButton(text="1", on_click=num_one, width=75),
                ft.FilledTonalButton(text="2", on_click=num_two, width=75),
                ft.FilledTonalButton(text="3", on_click=num_three, width=75),
                ft.FilledTonalButton(text="-", on_click=actsub, width=75),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            [
                ft.FilledTonalButton(text="0", on_click=num_zero, width=75),
                ft.FilledTonalButton(text="CA", on_click=clearer, width=75),
                ft.FilledTonalButton(text="/", on_click=actdiv, width=75),
                ft.FilledTonalButton(text="*", on_click=actmult, width=75),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            [
                ft.FilledTonalButton(text="=", on_click=igual, width=330),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )


ft.app(target=main)
