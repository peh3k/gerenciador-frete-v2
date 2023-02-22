from frames.FramesDependences import *

class ErroScreenTabela(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Imagem da tela inicial
        img = ImageTk.PhotoImage(Image.open(
            "images/ops_img_2.png"))
        label = customtkinter.CTkLabel(self, text='', image=img)
        label.pack()