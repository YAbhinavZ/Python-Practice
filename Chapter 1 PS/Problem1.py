# import cowsay
# cowsay.cow("Hello, Abhinav")

# from rich import print
# print("[bold green]Hello, world! 🚀[/]")
# print("[bold red]Python is fun![/]")

import pyttsx3

engine = pyttsx3.init()
engine.say("Hello! Welcome to Python programming.")
engine.runAndWait()