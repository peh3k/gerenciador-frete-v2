from frames.FramesDependences import *

class Home(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Imagem da tela inicial
        img = ImageTk.PhotoImage(Image.open(
            "images/home.png"))
        label = customtkinter.CTkLabel(self, text='', image=img)
        label.pack()