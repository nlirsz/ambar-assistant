import customtkinter as ctk

# Renomeamos a classe principal para refletir o nome do app
class AmbarApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Ambar - Configurações")
        self.geometry("500x400")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        label = ctk.CTkLabel(self, text="Interface de configurações do Ambar.")
        label.grid(row=0, column=0, padx=20, pady=20)