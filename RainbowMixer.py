import flet as ft

def main (page: ft.Page):
    rgbt= ft.Text("RGB(0, 0, 0)", size=35)

    def colors(e):
        r=int(redSlider.value)
        g=int(greenSlider.value)
        b=int(blueSlider.value)

        page.bgcolor=f"#{r:02x}{g:02x}{b:02x}"
        rgbt.value= f"RGB({r}, {g}, {b})"
        page.update()

    redSlider=ft.Slider(min=0, max=255, value=0, on_change=colors)
    greenSlider=ft.Slider(min=0, max=255, value=0, on_change=colors)
    blueSlider=ft.Slider(min=0, max=255, value=0, on_change=colors)

    page.add(rgbt, ft.Text("Red"), redSlider, ft.Text("Green"), greenSlider, ft.Text("Blue"), blueSlider)

ft.run(main=main)