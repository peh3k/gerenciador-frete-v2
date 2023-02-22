from frames.FramesDependences import *


class DeletadoSucesso(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.geometry("300x140")
  
        # definir a posição da janela

        self.title("Aviso")
        self.label = customtkinter.CTkLabel(
            self, text="Excluído com Sucesso!")
        self.label.pack(padx=20, pady=20)

        ok_button = customtkinter.CTkButton(self, text="OK", corner_radius=7, width=70,
                                            height=30, fg_color="#3d9336", hover_color="#51bc48",
                                            command=self.fechar_janela)
        ok_button.pack(padx=5, pady=5)

    def fechar_janela(self):
        self.destroy()

        
class BaixadoSucesso(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.geometry("200x130")
  

        # definir a posição da janela

        self.title("Aviso")
        self.label = customtkinter.CTkLabel(
            self, text="Baixado com Sucesso!")
        self.label.pack(padx=20, pady=20)

        ok_button = customtkinter.CTkButton(self, text="OK", corner_radius=7, width=70,
                                            height=30, fg_color="#3d9336", hover_color="#51bc48",
                                            command=self.fechar_janela)
        ok_button.pack(padx=5, pady=5)

    def fechar_janela(self):
        self.destroy()

class AtualizadoSucessoPopup(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("200x130")
        self.title("Aviso")
        header_label = customtkinter.CTkLabel(
            self, text="Atualizado com Sucesso!").pack(padx=20, pady=20)
        ok_button = customtkinter.CTkButton(self, text="OK", corner_radius=7, width=70, height=30,
                                            fg_color="#3d9336", hover_color="#51bc48", command=self.fechar_janela).pack(padx=5, pady=5)

    def fechar_janela(self):
        self.destroy()


class CadastroSucessoPopup(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("200x130")
        self.title("Aviso")
        header_label = customtkinter.CTkLabel(
            self, text="Cadastrado com Sucesso!").pack(padx=20, pady=20)
        ok_button = customtkinter.CTkButton(self, text="OK", corner_radius=7, width=70, height=30,
                                            fg_color="#3d9336", hover_color="#51bc48", command=self.fechar_janela).pack(padx=5, pady=5)

    def fechar_janela(self):
        self.destroy()


class ErroInesperadoPopup(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("200x130")
        self.title("Aviso")
        header_label = customtkinter.CTkLabel(
            self, text="Erro Inesperado!").pack(padx=20, pady=20)
        ok_button = customtkinter.CTkButton(self, text="OK", corner_radius=7, width=70, height=30,
                                            fg_color="#3d9336", hover_color="#51bc48", command=self.fechar_janela).pack(padx=5, pady=5)

    def fechar_janela(self):
        self.destroy()


class ItemExistente(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("200x130")
        self.title("Aviso")
        header_label = customtkinter.CTkLabel(
            self, text="Item Já Existente!").pack(padx=20, pady=20)
        ok_button = customtkinter.CTkButton(self, text="OK", corner_radius=7, width=70, height=30,
                                            fg_color="#3d9336", hover_color="#51bc48", command=self.fechar_janela).pack(padx=5, pady=5)

    def fechar_janela(self):
        self.destroy()

class TabelaInexistente(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("200x130")
        self.title("Aviso")
        header_label = customtkinter.CTkLabel(
            self, text="Tabela não existe!").pack(padx=20, pady=20)
        ok_button = customtkinter.CTkButton(self, text="OK", corner_radius=7, width=70, height=30,
                                            fg_color="#3d9336", hover_color="#51bc48", command=self.fechar_janela).pack(padx=5, pady=5)

    def fechar_janela(self):
        self.destroy()
        
class TabelaTransportadoraDuplicatasPopup(customtkinter.CTkToplevel):
    def __init__(self, *args, header=[], **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("600x400")
        self.title("Itens Ignorados (Duplicaatas)")
        criar_tabela(self, PADRAO_TRANSPORTADORA, header)
        
        
class TabelaProdutoDuplicatasPopup(customtkinter.CTkToplevel):
    def __init__(self, *args, header=[], **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("600x400")
        self.title("Itens Ignorados (Duplicaatas)")
        criar_tabela(self, PADRAO_PRODUTO, header)
        

class TabelaTransportadora(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        width = 650
        height = 400
        try:
            # obter as dimensões da tela
            screen_width = self.winfo_screenwidth()
            screen_height = self.winfo_screenheight()

            downloadimage = ImageTk.PhotoImage(Image.open(
                "images/download.png").resize((15, 15)), Image.ANTIALIAS)
            

            self.baixado_screen = None
            self.baixado_fail = None


            # calcular as coordenadas x e y da janela
            x = (screen_width // 2) - (width // 2) + 60
            y = (screen_height // 2) - (height // 2) - 25

            # definir a posição da janela
            self.geometry("{}x{}+{}+{}".format(width, height, x, y))
            self.title("Transportadoras")
            
            todos_valores = get_db(PATH_TRANSPORTADORA)
            filtro = [todos_valores[item].remove(lista) for item in todos_valores for lista in todos_valores[item] if lista is None]

            self.all_dicts = [list(lista.values()) for key in todos_valores for lista in todos_valores[key]]
            
            self.keys_padrao = ['ID', 'advalorem', 'cep final', 'cep inicial', 'cidade', 'estado', 'frete min', 'gris', 'icms', 'nome', 'outros', 'pedagio', 'peso final', 'peso inicial', 'prazo', 'regiao', 'tac', 'tas', 'valor frete']

            button = customtkinter.CTkButton(
                self, text='Baixar', image=downloadimage, width=30, command=self.baixar_tabela)
            button.pack(side="bottom", pady=10)
            
            criar_tabela(self, self.keys_padrao, self.all_dicts)
        except:
            self.geometry("200x130")
            self.title("Aviso")
            header_label = customtkinter.CTkLabel(
                self, text="Tabela não existe!").pack(padx=20, pady=20)
            ok_button = customtkinter.CTkButton(self, text="OK", corner_radius=7, width=70, height=30,
                                                fg_color="#3d9336", hover_color="#51bc48", command=self.fechar_janela).pack(padx=5, pady=5)
            logging.warning('Tabela não existe')
            
    def fechar_janela(self):
        self.destroy()
    
    def baixar_tabela(self):
        try:
            dados = get_db('Transportadora')
            filtro = [dados[item].remove(lista) for item in dados for lista in dados[item] if lista is None]

          
            criar_tabela_excel(self.keys_padrao, self.all_dicts,
                               'Tabela_Transportadoras.xlsx')
            if self.baixado_screen is None or not self.baixado_screen.winfo_exists():
                # create window if its None or destroyed
                self.baixado_screen = BaixadoSucesso(self)
        except:
            if self.baixado_fail is None or not self.baixado_fail.winfo_exists():
                # create window if its None or destroyed
                self.baixado_fail = ErroInesperadoPopup(self)

class TabelaProduto(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        width = 650
        height = 400
        try:
            # obter as dimensões da tela
            screen_width = self.winfo_screenwidth()
            screen_height = self.winfo_screenheight()

            downloadimage = ImageTk.PhotoImage(Image.open(
                "images/download.png").resize((15, 15)), Image.ANTIALIAS)
            

            self.baixado_screen = None
            self.baixado_fail = None


            # calcular as coordenadas x e y da janela
            x = (screen_width // 2) - (width // 2) + 60
            y = (screen_height // 2) - (height // 2) - 25

            # definir a posição da janela
            self.geometry("{}x{}+{}+{}".format(width, height, x, y))
            self.title("Produtos")
        
            todos_valores = get_db(PATH_PRODUTO)
            filtro = [todos_valores[item].remove(lista) for item in todos_valores for lista in todos_valores[item] if lista is None]

            self.all_dicts = [list(lista.values()) for key in todos_valores for lista in todos_valores[key]]
            
            self.keys_padrao = ['ID', 'altura', 'codigo interno', 'comprimento', 'descricao', 'largura', 'peso', 'unidade', 'valor venda']
            button = customtkinter.CTkButton(
                self, text='Baixar', image=downloadimage, width=30, command=self.baixar_tabela)
            button.pack(side="bottom", pady=10)
        
            criar_tabela(self, self.keys_padrao, self.all_dicts)
        except:
            
            self.geometry("200x130")
            self.title("Aviso")
            header_label = customtkinter.CTkLabel(
                self, text="Tabela não existe!").pack(padx=20, pady=20)
            ok_button = customtkinter.CTkButton(self, text="OK", corner_radius=7, width=70, height=30,
                                                fg_color="#3d9336", hover_color="#51bc48", command=self.fechar_janela).pack(padx=5, pady=5)
            logging.warning('Tabela não existe')
    def fechar_janela(self):
        self.destroy()
            
            

    
    def baixar_tabela(self):
        try:
            dados = get_db(PATH_PRODUTO)
            filtro = [dados[item].remove(lista) for item in dados for lista in dados[item] if lista is None]

          
            criar_tabela_excel(self.keys_padrao, self.all_dicts,
                               'Tabela_Produtos.xlsx')
            if self.baixado_screen is None or not self.baixado_screen.winfo_exists():
                # create window if its None or destroyed
                self.baixado_screen = BaixadoSucesso(self)
        except:
            if self.baixado_fail is None or not self.baixado_fail.winfo_exists():
                # create window if its None or destroyed
                self.baixado_fail = ErroInesperadoPopup(self)


    
    

  