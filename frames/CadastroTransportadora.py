from frames.FramesDependences import *
from frames.Popus import *




class CadastroTransportadoraScreen(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        upload_img = ImageTk.PhotoImage(Image.open(
            "images/upload.png").resize((20, 20)))

        # Widgets da tela

        label_nome = customtkinter.CTkLabel(self, text="Nome:").grid(
            row=0, column=0, pady=20, padx=10)
        self.nome = customtkinter.CTkEntry(
            self, width=140, height=25, border_width=1, corner_radius=2, placeholder_text="ex: America Trans").grid(row=0, column=1)
        label_pinicial = customtkinter.CTkLabel(
            self, text="Peso Inicial:").grid(row=1, column=0, pady=20, padx=10)
        self.peso_inicial = customtkinter.CTkEntry(
            self, width=85, height=25, border_width=1, corner_radius=2, placeholder_text="Gramas").grid(row=1, column=1)
        label_pfinal = customtkinter.CTkLabel(
            self, text="Peso Final:").grid(row=2, column=0, pady=20, padx=10)
        self.peso_final = customtkinter.CTkEntry(
            self, width=85, height=25, border_width=1, corner_radius=2, placeholder_text="Gramas").grid(row=2, column=1)
        label_cepinicial = customtkinter.CTkLabel(
            self, text="Cep Inicial:").grid(row=3, column=0, pady=20, padx=10)
        self.cep_inicial = customtkinter.CTkEntry(
            self, width=85, height=25, border_width=1, corner_radius=2, placeholder_text="ex: 000000-00").grid(row=3, column=1)
        label_cepfinal = customtkinter.CTkLabel(
            self, text="Cep Final:").grid(row=4, column=0, pady=20, padx=10)
        self.cep_final = customtkinter.CTkEntry(
            self, width=85, height=25, border_width=1, corner_radius=2, placeholder_text="ex: 000000-00").grid(row=4, column=1)
        label_prazo = customtkinter.CTkLabel(self, text="Prazo:").grid(
            row=5, column=0, pady=20, padx=10)
        self.prazo = customtkinter.CTkEntry(
            self, width=85, height=25, border_width=1, corner_radius=2, placeholder_text="ex: 13").grid(row=5, column=1)
        label_estado = customtkinter.CTkLabel(
            self, text="Estado:").grid(row=0, column=2, pady=20, padx=10)
        self.estado = customtkinter.CTkEntry(
            self, width=85, height=25, border_width=1, corner_radius=2, placeholder_text="ex: sp").grid(row=0, column=3)
        label_cidade = customtkinter.CTkLabel(
            self, text="Cidade:").grid(row=1, column=2, pady=20, padx=10)
        self.cidade = customtkinter.CTkEntry(
            self, width=85, height=25, border_width=1, corner_radius=2, placeholder_text="ex: osasco").grid(row=1, column=3)
        label_regiao = customtkinter.CTkLabel(
            self, text="Região:").grid(row=2, column=2, pady=20, padx=10)
        self.regiao = customtkinter.CTkEntry(
            self, width=85, height=25, border_width=1, corner_radius=2, placeholder_text="ex: sudeste").grid(row=2, column=3)
        label_vfrete = customtkinter.CTkLabel(
            self, text="Valor Frete:").grid(row=3, column=2, pady=20, padx=10)
        self.valor_frete = customtkinter.CTkEntry(
            self, width=85, height=25, border_width=1, corner_radius=2, placeholder_text="R$").grid(row=3, column=3)
        label_fretemin = customtkinter.CTkLabel(
            self, text="Frete Mín:").grid(row=4, column=2, pady=20, padx=10)
        self.frete_min = customtkinter.CTkEntry(
            self, width=85, height=25, border_width=1, corner_radius=2, placeholder_text="R$").grid(row=4, column=3)
        label_tac = customtkinter.CTkLabel(self, text="Tac:").grid(
            row=5, column=2, pady=20, padx=10)
        self.tac = customtkinter.CTkEntry(
            self, width=85, height=25, border_width=1, corner_radius=2, placeholder_text="R$").grid(row=5, column=3)
        label_gris = customtkinter.CTkLabel(self, text="Gris:").grid(
            row=0, column=4, pady=20, padx=10)
        self.gris = customtkinter.CTkEntry(
            self, width=85, height=25, border_width=1, corner_radius=2, placeholder_text="%").grid(row=0, column=5)
        label_advalorem = customtkinter.CTkLabel(
            self, text="Advalorem:").grid(row=1, column=4, pady=20, padx=10)
        self.advalorem = customtkinter.CTkEntry(
            self, width=85, height=25, border_width=1, corner_radius=2, placeholder_text="%").grid(row=1, column=5)
        label_pedagio = customtkinter.CTkLabel(
            self, text="Pedágio:").grid(row=2, column=4, pady=20, padx=10)
        self.pedagio = customtkinter.CTkEntry(
            self, width=85, height=25, border_width=1, corner_radius=2, placeholder_text="R$").grid(row=2, column=5)
        label_tas = customtkinter.CTkLabel(self, text="Tas:").grid(
            row=3, column=4, pady=20, padx=10)
        self.tas = customtkinter.CTkEntry(
            self, width=85, height=25, border_width=1, corner_radius=2, placeholder_text="R$").grid(row=3, column=5)
        label_icms = customtkinter.CTkLabel(self, text="Icms:").grid(
            row=4, column=4, pady=20, padx=10)
        self.icms = customtkinter.CTkEntry(
            self, width=85, height=25, border_width=1, corner_radius=2, placeholder_text="%").grid(row=4, column=5)
        label_outros = customtkinter.CTkLabel(
            self, text="Outros:").grid(row=5, column=4, pady=20, padx=10)
        self.outros = customtkinter.CTkEntry(
            self, width=140, height=25, border_width=1, corner_radius=2).grid(row=5, column=5)
        button_importar = customtkinter.CTkButton(
            self, text="Importar", image=upload_img, corner_radius=7, height=30,  width=100, fg_color="#df8110", hover_color="#ce770f", command=self.importar_transportadoras_from_excel)
        button_importar.grid(row=6, column=0, padx=25, pady=20)
        button_cadastrar = customtkinter.CTkButton(
            self, text="Cadastrar", corner_radius=7, height=30,  width=100, fg_color="#3d9336", hover_color="#51bc48", command=self.cadastrar_transportadora_from_inputs)
        button_cadastrar.grid(row=6, column=5, pady=20)
        # Fim dos widgets

    # Métodos da tela de cadastro de transportadoras

    # Pegar todos os textos dos inputs desse frame
    def get_all_inputs_text(self):
        all_inputs = [child.get() for child in self.winfo_children(
        ) if isinstance(child, customtkinter.CTkEntry)]

        return all_inputs

    # Zerar todos os inputs
    def clear_all_entries(self):
        for child in self.winfo_children():
            if isinstance(child, customtkinter.CTkEntry):
                child.delete(0, tk.END)

    def importar_transportadoras_from_excel(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Arquivos de excel", "*.xlsx")])
        try:

            # Retorna os dados iguais e os dados únicos
            upload_returned = self.upload_massivo_transportadora(file_path)

            # Caso tenha dados únicos exibe o popup de cadastro concluído, caso contrario exibe a tabela de duplicatas
            if len(upload_returned[0]) > 0:
                TabelaTransportadoraDuplicatasPopup(
                    self, header=upload_returned[0])
            if len(upload_returned[1]) > 0:
                CadastroSucessoPopup(self)
            if len(upload_returned[1]) == 0:
                logging.warning(
                    'nao foi preciso o cadastro de nenhuma transportadora')
        except:
            logging.warning("Erro ao importar dados transportadora")
            ErroInesperadoPopup(self)

    def cadastrar_transportadora_from_inputs(self):
        try:
            text_entries = self.get_all_inputs_text()

            # Gera um loggin caso o usuario não digite o nome da empresa
            if len(text_entries[0]) <= 0:
                logging.warning('empresa sem nome')

            # Cadastra a transportadora
            else:
                new_text_entries = []
                new_text_entries.append(text_entries)
                dados_insert = list_to_dict(
                    new_text_entries, PADRAO_TRANSPORTADORA[1:])
                
                dados_insert[0]['ID'] = get_last_id_db(PATH_TRANSPORTADORA) + 1

                post_dados = self.post_db(
                    dados_insert, search_same=new_text_entries)
                self.clear_all_entries()

                if post_dados is not False:
                    CadastroSucessoPopup(self)
                else:
                    ItemExistente(self)

        except:
            logging.warning('Cadastro manual transportadora')
            ErroInesperadoPopup(self)

    def upload_massivo_transportadora(self, file):

        rows_excel = get_excel_rows(file)

        chaves_padrao = PADRAO_TRANSPORTADORA
        try:
            ids_repetidos = self.ids_repetidos_db(
                rows_excel, PATH_TRANSPORTADORA)
            if len(ids_repetidos[1]) > 0:
                dict = list_to_dict(ids_repetidos[1], chaves_padrao)
                self.post_db(dict)
                
                return ids_repetidos[0], ids_repetidos[1]
            if len(ids_repetidos[0]) > 0:

                return ids_repetidos[0], ids_repetidos[1]
        except:

            dict = list_to_dict(rows_excel, chaves_padrao)
            self.post_db(dict)
            return [], rows_excel

    def ids_repetidos_db(self, lista, table):
        all_data = get_db(table)
        filtro = [dict for key in all_data for dict in all_data[key] if dict is not None]
        only_ids = [item['ID'] for item in filtro]
        
        lista_repetidos = [lista for lista in lista if lista[0] in only_ids]
        lista_unicos = [lista for lista in lista if lista[0] not in only_ids]
        
        return lista_repetidos, lista_unicos
        
        
    def post_db(self, dados, search_same=[]):

        try:
            same_names = self.nomes_repetidos_input_to_db(
                search_same, PATH_TRANSPORTADORA)
            if len(same_names[0]) > 0:
                logging.warning("Nome já em uso")

                return False
            else:
                requisicao = requests.post(
                    f'{DbLink().URL_DB}/{PATH_TRANSPORTADORA}/.json', data=json.dumps(dados))
                return True
        except:

            requisicao = requests.post(
                f'{DbLink().URL_DB}/{PATH_TRANSPORTADORA}/.json', data=json.dumps(dados))
            return True

    
    def nomes_repetidos_input_to_db(self, list_values, table):
        todos_valores = get_db(table)
        filtro = [todos_valores[item].remove(lista) for item in todos_valores for lista in todos_valores[item] if lista is None]
        values = [todos_valores[value] for value in todos_valores]
        only_names = [item['nome'] for lista in values for item in lista]
        same_values = [row for row in list_values if row[0] in only_names], [row for row in list_values if row[1] not in only_names]
        
        return same_values