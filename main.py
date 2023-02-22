from frames.FramesDependences import *
from frames.MainFrame import MainFrame
from frames.CadastroTransportadora import CadastroTransportadoraScreen
from frames.Home import Home
from frames.TelaErro import ErroScreen
from frames.TelaErro2 import ErroScreenTabela
from frames.EditarTransportadora import EditarTransportadoraScreen
from frames.PainelLateral import PainelLateral
from frames.TabelaTransportadora import TabelaTransportadora
from frames.CadastroProduto import CadastroProdutoScreen
from frames.EditarProduto import EditarProdutoScreen
from frames.TabelaProduto import TabelaProduto



class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Configurações gerais da janela
        customtkinter.set_appearance_mode("dark")
        self.title("Calculadora de Frete")
        self.geometry("950x540")
        self.resizable(False, False)

        """
            /// PAINEL LATERAL ///

        """
        self.painel_lateral = PainelLateral(self)
        self.painel_lateral.pack(side='left')
        truck_image = ImageTk.PhotoImage(Image.open(
            "images/truck.png").resize((20, 20)), Image.ANTIALIAS)
        pencil_image = ImageTk.PhotoImage(Image.open(
            "images/pencil.png").resize((20, 20)), Image.ANTIALIAS)
        eye_image = ImageTk.PhotoImage(Image.open(
            "images/eye.png").resize((20, 20)), Image.ANTIALIAS)
        bag_image = ImageTk.PhotoImage(Image.open(
            "images/bag.png").resize((20, 20)), Image.ANTIALIAS)
        house_image = ImageTk.PhotoImage(Image.open(
            "images/house.png").resize((15, 15)), Image.ANTIALIAS)
        home_button = customtkinter.CTkButton(self.painel_lateral, text="Home", corner_radius=0, height=60,
                                              command=self.home_screen, fg_color="#1a1a1a", hover_color="#272727", anchor="center", image=house_image).pack()
        label_transp = customtkinter.CTkLabel(
            self.painel_lateral, text="Transportadora", height=45).pack()
        cadastrar_transp = customtkinter.CTkButton(self.painel_lateral, text="Cadastrar", corner_radius=0, command=self.cadastro_transportadora_screen,
                                                   height=60, fg_color="#333333", hover_color="#272727", anchor="center", image=truck_image).pack()
        visualizar_transp = customtkinter.CTkButton(self.painel_lateral, text="Visualizar", corner_radius=0,
                                                    height=50, fg_color="#333333", hover_color="#272727", image=eye_image, anchor="center", command=self.tabela_transportadora_screen).pack()
        editar_transp = customtkinter.CTkButton(self.painel_lateral, text="Editar", corner_radius=0,
                                                height=60, fg_color="#333333", hover_color="#272727", anchor="center", image=pencil_image, command=self.edicao_transportadora_screen).pack()
        produto_label = customtkinter.CTkLabel(
            self.painel_lateral, text="Produto", height=35).pack()
        cadastrar_produto = customtkinter.CTkButton(self.painel_lateral, text="Cadastrar", corner_radius=0,
                                                    height=50, fg_color="#333333", hover_color="#272727", image=bag_image, anchor="center", command=self.cadastrar_produto_screen).pack()
        visualizar_produto = customtkinter.CTkButton(self.painel_lateral, text="Visualizar", corner_radius=0, command=self.tabela_produto_screen,
                                                     height=50, fg_color="#333333", hover_color="#272727", image=eye_image, anchor="center").pack()
        editar_produto = customtkinter.CTkButton(self.painel_lateral, text="Editar", corner_radius=0,
                                                 height=50, fg_color="#333333", hover_color="#272727", image=pencil_image, anchor="center", command=self.editar_produto_screen).pack()
        calculo_label = customtkinter.CTkLabel(
            self.painel_lateral, text="Calculo Frete", height=35).pack()
        calcular_frete = customtkinter.CTkButton(self.painel_lateral, text="Calcular", corner_radius=0,
                                                 height=50, fg_color="#333333", hover_color="#272727", image=eye_image, anchor="center").pack()

        # Frame Principal
        self.MAIN_FRAME = MainFrame(self)
        self.MAIN_FRAME.pack(pady=30)
        self.MAIN_FRAME.pack_propagate(False)

        # Home de Entrada
        self.MAIN_HOME_SCREEN = Home(self.MAIN_FRAME)
        self.MAIN_HOME_SCREEN.pack()

    def delete_pages(self):
        for frame in self.MAIN_FRAME.winfo_children():
            frame.destroy()

    def home_screen(self):
        self.delete_pages()
        home_screen = Home(self.MAIN_FRAME)
        home_screen.pack()

    def cadastro_transportadora_screen(self):
        self.delete_pages()
        cadastro_transportadora_screen = CadastroTransportadoraScreen(
            self.MAIN_FRAME)
        cadastro_transportadora_screen.pack(ipadx=30, ipady=20)

    def edicao_transportadora_screen(self):
        self.delete_pages()

        try:
            edicao_transportadora_screen = EditarTransportadoraScreen(
                self.MAIN_FRAME)
            edicao_transportadora_screen.pack(ipadx=30, ipady=20)
        except:
            erro_screen = ErroScreen(self.MAIN_FRAME)
            erro_screen.pack()
    
    def tabela_transportadora_screen(self):
        is_table_exisits = get_db(PATH_TRANSPORTADORA)
        if is_table_exisits is not None:
            tabela_transportadora_screen = TabelaTransportadora(
                self.MAIN_FRAME)
        else:
            self.delete_pages()
        
            erro_screen = ErroScreenTabela(self.MAIN_FRAME)
            erro_screen.pack()

    
    def cadastrar_produto_screen(self):
        self.delete_pages()
        cadastro_produto_screen = CadastroProdutoScreen(
            self.MAIN_FRAME)
        cadastro_produto_screen.pack(ipadx=30, ipady=30, side="bottom")
        
    def editar_produto_screen(self):
        
        
        is_table_exisits = get_db(PATH_PRODUTO)
        if is_table_exisits is not None:
            self.delete_pages()
            
            editar_produto_screen = EditarProdutoScreen(
                self.MAIN_FRAME)
            editar_produto_screen.pack(ipadx=30, ipady=30, side="bottom")
        else:
            self.delete_pages()
        
            erro_screen = ErroScreen(self.MAIN_FRAME)
            erro_screen.pack()

        
    def tabela_produto_screen(self):
        is_table_exisits = get_db(PATH_PRODUTO)
        if is_table_exisits is not None:
            tabela_produto_screen = TabelaProduto(
                self.MAIN_FRAME)
        else:
            self.delete_pages()
        
            erro_screen = ErroScreenTabela(self.MAIN_FRAME)
            erro_screen.pack()
        
            
            
        
if __name__ == "__main__":
    app = App()
    app.mainloop()
