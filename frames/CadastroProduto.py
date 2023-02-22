from frames.FramesDependences import *
from frames.Popus import *


class CadastroProdutoScreen(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        upload_img = ImageTk.PhotoImage(Image.open(
            "images/upload.png").resize((20, 20)))

        label_codigo = customtkinter.CTkLabel(
            self, text="Código Interno:").grid(row=0, column=0, padx=20, pady=50)
        self.codigo_interno = customtkinter.CTkEntry(
            self, width=85, height=25, border_width=1, corner_radius=2, placeholder_text="ex: 8888888").grid(row=0, column=1, pady=30)
        label_descricao = customtkinter.CTkLabel(
            self, text="Descrição:").grid(row=3, column=2, padx=20, pady=30)
        self.descricao = customtkinter.CTkEntry(
            self, width=230, height=25, border_width=1, corner_radius=2, placeholder_text="ex: Rosca sextavada 1/2' alumínio").grid(row=3, column=3, pady=30)
        label_unidade = customtkinter.CTkLabel(
            self, text="Unidade:").grid(row=1, column=0, padx=20, pady=30)
        self.unidade = customtkinter.CTkEntry(
            self, width=85, height=25, border_width=1, corner_radius=2, placeholder_text="ex: PCA").grid(row=1, column=1, pady=30)
        label_valor_venda = customtkinter.CTkLabel(
            self, text="Valor Venda:").grid(row=2, column=0, padx=20, pady=30)
        self.valor_venda = customtkinter.CTkEntry(
            self, width=85, height=25, border_width=1, corner_radius=2, placeholder_text="R$").grid(row=2, column=1, pady=30)
        label_peso = customtkinter.CTkLabel(self, text="Peso:").grid(
            row=3, column=0, padx=20, pady=30)
        self.peso = customtkinter.CTkEntry(
            self, width=85, height=25, border_width=1, corner_radius=2, placeholder_text="ex: 0,43").grid(row=3, column=1, pady=30)
        label_comprimento = customtkinter.CTkLabel(
            self, text="Comprimento:").grid(row=0, column=2, padx=20, pady=30)
        self.comprimento = customtkinter.CTkEntry(
            self, width=85, height=25, border_width=1, corner_radius=2, placeholder_text="ex: 4").grid(row=0, column=3, pady=30)
        label_largura = customtkinter.CTkLabel(
            self, text="largura:").grid(row=1, column=2, padx=20, pady=30)
        self.largura = customtkinter.CTkEntry(
            self, width=85, height=25, border_width=1, corner_radius=2, placeholder_text="ex: 12").grid(row=1, column=3, pady=30)
        label_altura = customtkinter.CTkLabel(
            self, text="Altura:").grid(row=2, column=2, padx=20, pady=30)
        self.altura = customtkinter.CTkEntry(
            self, width=85, height=25, border_width=1, corner_radius=2, placeholder_text="ex: 54").grid(row=2, column=3, pady=30)
        

        button_cadastrar = customtkinter.CTkButton(self, text="Cadastrar", corner_radius=7, height=30,
                                                   width=100, fg_color="#3d9336", hover_color="#51bc48", command=self.cadastrar_produto).grid(row=6, column=4)

        button_importar = customtkinter.CTkButton(self, text="Importar", corner_radius=7, height=30, image=upload_img,
                                                  width=100, fg_color="#df8110", hover_color="#ce770f", command=self.importar_dados_produto_from_excel).grid(row=6, column=0, padx=25, pady=20)

    def get_all_inputs_text(self):
        all_inputs = [child.get() for child in self.winfo_children(
        ) if isinstance(child, customtkinter.CTkEntry)]

        return all_inputs

    # Zerar todos os inputs
    def clear_all_entries(self):
        for child in self.winfo_children():
            if isinstance(child, customtkinter.CTkEntry):
                child.delete(0, tk.END)
                
    def cadastrar_produto(self):
        all_text = self.get_all_inputs_text()
        
        
        if len(all_text[0]) <= 0:
            logging.warning("Produto sem código")
            
        else:
            new_text_entries = []
            new_text_entries.append(all_text)
            dados_insert = list_to_dict(
                new_text_entries, PADRAO_PRODUTO[1:])
            dados_insert[0]['ID'] = self.get_last_id(PATH_PRODUTO) + 1
            post_dados = self.post_db(
            dados_insert, search_same=new_text_entries)
            self.clear_all_entries()
            
            if post_dados is not False:
                    CadastroSucessoPopup(self)
            else:
                ItemExistente(self)

    def importar_dados_produto_from_excel(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Arquivos de excel", "*.xlsx")])
        try:

            # Retorna os dados iguais e os dados únicos
            upload_returned = self.upload_massivo_produto(file_path)

            # Caso tenha dados únicos exibe o popup de cadastro concluído, caso contrario exibe a tabela de duplicatas
            if len(upload_returned[0]) > 0:
                TabelaProdutoDuplicatasPopup(
                    self, header=upload_returned[0])
                
            if len(upload_returned[1]) > 0:
                CadastroSucessoPopup(self)
            if len(upload_returned[1]) == 0:
                logging.warning(
                    'nao foi preciso o cadastro de nenhuma transportadora')
        except:
            logging.warning("Erro ao importar dados transportadora")
            ErroInesperadoPopup(self)
        
    
    
    def post_db(self, dados, search_same=[]):

        try:
            same_names = self.codigo_interno_repetido(
                search_same)
            if len(same_names[0]) > 0:
                logging.warning("Nome já em uso")

                return False
            else:
                requisicao = requests.post(
                    f'{DbLink().URL_DB}/{PATH_PRODUTO}/.json', data=json.dumps(dados))
                return True
        except:

            requisicao = requests.post(
                f'{DbLink().URL_DB}/{PATH_PRODUTO}/.json', data=json.dumps(dados))
            return True
    
    def codigo_interno_repetido(self, list_values):
        all_data = get_db(PATH_PRODUTO)
        filtro = [all_data[item].remove(lista) for item in all_data for lista in all_data[item] if lista is None]
        values = [all_data[value] for value in all_data]
        only_code = [str(item['codigo interno']) for lista in values for item in lista]
        same_values = [row for row in list_values if row[0] in only_code], [row for row in list_values if row[1] not in only_code]
        
        return same_values
    
    def upload_massivo_produto(self, file):

        rows_excel = get_excel_rows(file)
        chaves_padrao = PADRAO_PRODUTO
        try:
            ids_repetidos = self.ids_repetidos_db(
                rows_excel, PATH_PRODUTO)
            
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
        todos_valores = get_db(table)
        jsons = {}
        for key in todos_valores:
            new_list = remover_nones(todos_valores[key])
            jsons[key] = new_list
        only_ids = [lista['ID'] for key in jsons for lista in jsons[key]]
        
        lista_repetidos = [lista for lista in lista if lista[0] in only_ids]
        lista_unicos = [lista for lista in lista if lista[0] not in only_ids]
        
        return lista_repetidos, lista_unicos
    
    def get_last_id(self, table):
        all_data = get_db(table)
        
        try:
            jsons = {}
            for key in all_data:
                new_list = remover_nones(all_data[key])
                jsons[key] = new_list
            ids = [lista['ID'] for key in jsons for lista in jsons[key]]
            
            return ids[-1]
        except:
            return 0