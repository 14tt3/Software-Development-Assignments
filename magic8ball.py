import flet as ft
import random 

def main (page: ft.Page):
    
    def question(e):
        response = random.choice (responses)
        answer.value = response
        if response in positiveresponses:
            answer.color = "green"
        elif response in negativeresponses:
            answer.color = "red"
        elif response in neutralresponses:
            answer.color = "purple"
        page.update()

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    textbox= ft.TextField(label= "Enter a yes or no question: ", text_size= 20)

    positiveresponses = ["Yes", "As I see it yes", " Most likely", "It is certain", "Without a doubt", "Go girl"]
    negativeresponses = ["No", "I doubt it", "Very doubtful", "My reply is no", "Don't count on it", "Seek help"]
    neutralresponses = ["Maybe", "Ask again later", " Better not tell you now", "Cannot predict now", "You should see for yourself"]

    responses = positiveresponses +  negativeresponses + neutralresponses
    answer = ft.Text(size= 20)
    rollbutton = ft.TextButton (content= "Ask Magic 8 Ball", on_click=question)

    page.add (textbox, rollbutton, answer)

ft.run(main= main)