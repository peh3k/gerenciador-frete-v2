from frames.FramesDependences import *
from frames.Popus import *


class EditarProdutoScreen(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        trash_img = ImageTk.PhotoImage(Image.open(
            "images/trash.png").resize((15, 15)))

        search_image = ImageTk.PhotoImage(Image.open(
            "images/search.png").resize((15, 15)), Image.ANTIALIAS)

        label_id = customtkinter.CTkLabel(
            self, text="Buscar ID:").grid(row=0, column=0, padx=20, pady=50)
        self.codigo_interno = customtkinter.CTkEntry(
            self, width=85, height=25, border_width=1, corner_radius=2, placeholder_text="ex: 2").grid(row=0, column=1, pady=30)
        button_cada = customtkinter.CTkButton(self, image=search_image, text="", corner_radius=7,
                                              height=30,  width=20, fg_color="#808080", hover_color="#666666", command=self.is_id_exists).grid(row=0, column=2, padx=15)

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
            self, text="Comprimento:").grid(row=0, column=3, padx=20, pady=30)
        self.comprimento = customtkinter.CTkEntry(
            self, width=85, height=25, border_width=1, corner_radius=2, placeholder_text="ex: 4").grid(row=0, column=4, pady=30)
        label_largura = customtkinter.CTkLabel(
            self, text="largura:").grid(row=1, column=3, padx=20, pady=30)
        self.largura = customtkinter.CTkEntry(
            self, width=85, height=25, border_width=1, corner_radius=2, placeholder_text="ex: 12").grid(row=1, column=4, pady=30)
        label_altura = customtkinter.CTkLabel(
            self, text="Altura:").grid(row=2, column=3, padx=20, pady=30)
        self.altura = customtkinter.CTkEntry(
            self, width=85, height=25, border_width=1, corner_radius=2, placeholder_text="ex: 54").grid(row=2, column=4, pady=30)
        label_descricao = customtkinter.CTkLabel(
            self, text="Descrição:").grid(row=3, column=3, padx=20, pady=30)
        self.descricao = customtkinter.CTkEntry(
            self, width=230, height=25, border_width=1, corner_radius=2, placeholder_text="ex: Rosca sextavada 1/2' alumínio").grid(row=3, column=4, pady=30)
        button_atualizar = customtkinter.CTkButton(self, text="Atualziar", corner_radius=7, height=30,
                                                   width=100, fg_color="#3d9336", hover_color="#51bc48", command=self.atualizar_produto).grid(row=6, column=4)

        button_excluir = customtkinter.CTkButton(
            self, text="Excluir", image=trash_img, corner_radius=7, height=30,  width=100, fg_color="#ff3333", hover_color="#ff1a1a", command=self.deletar_produto)
        button_excluir.grid(row=6, column=0, padx=25, pady=20)

    def get_all_inputs_text(self):
        all_inputs = [child.get() for child in self.winfo_children(
        ) if isinstance(child, customtkinter.CTkEntry)]

        return all_inputs

    # Zerar todos os inputs
    def clear_all_entries(self):
        for child in self.winfo_children():
            if isinstance(child, customtkinter.CTkEntry):
                child.delete(0, tk.END)

    def get_all_inputs(self):
        all_inputs = [child for child in self.winfo_children(
        ) if isinstance(child, customtkinter.CTkEntry)]

        return all_inputs

    def is_id_exists(self):
        texts = self.get_all_inputs_text()
        all_data = get_db(PATH_PRODUTO)
        filtro = [all_data[item].remove(
            lista) for item in all_data for lista in all_data[item] if lista is None]
        only_ids = [lista['ID'] for key in all_data for lista in all_data[key] if str(
            lista['ID']) == texts[0]]
        if len(only_ids) > 0:
            self.preencher_inputs()

    def preencher_inputs(self):
        all_data = get_db(PATH_PRODUTO)
        filtro = [all_data[item].remove(
            lista) for item in all_data for lista in all_data[item] if lista is None]
        all_inputs = self.get_all_inputs()
        id_text = self.get_all_inputs_text()[0]
        dict = [list(lista.values())
                for key in all_data for lista in all_data[key] if lista['ID'] == int(id_text)]
        del dict[0][2]
        dict_organized = []
        dict_organized.append(dict[0][0])
        dict_organized.append(dict[0][6])
        dict_organized.append(dict[0][7])
        dict_organized.append(dict[0][5])
        dict_organized.append(dict[0][2])
        dict_organized.append(dict[0][4])
        dict_organized.append(dict[0][1])
        dict_organized.append(dict[0][3])
        self.clear_all_entries()
        for item in range(len(dict_organized)):
            all_inputs[item].insert(0, dict_organized[item])

    def atualizar_produto(self):

        try:
            all_texts = self.get_all_inputs_text()
            path_name = self.get_path_by_id(
                PATH_PRODUTO, all_texts[0])

            new_texts = []
            new_texts.append(all_texts[1:])

            padrao = PADRAO_PRODUTO[2:]
            new_padrao = []

            # Ordem dos inputs na mesma ordem das chaves dos dicionarios
            new_padrao.append(padrao[1])
            new_padrao.append(padrao[2])
            new_padrao.append(padrao[3])
            new_padrao.append(padrao[4])
            new_padrao.append(padrao[5])
            new_padrao.append(padrao[6])
            new_padrao.append(padrao[0])

            dict = list_to_dict(new_texts, new_padrao)

            patch_db(
                f'{PATH_PRODUTO}/{path_name[1]}/{path_name[0]}', dict[0])
            AtualizadoSucessoPopup(self)
            self.clear_all_entries()

        except:
            logging.warning("Erro atualizar transportadora")
            ErroInesperadoPopup(self)

    def get_path_by_id(self, table, id):
        all_data = get_db(table)
        filtro = [all_data[item].remove(
            lista) for item in all_data for lista in all_data[item] if lista is None]
        path = []
        position = []
        count = -1
        for item in all_data:
            count = -1
            for lista in all_data[item]:
                count += 1
                if lista['ID'] == int(id):
                    path.append(item)
                    position.append(count)
                    break

        if len(path) == 0:
            logging.exception("item não existe")
            return count
        else:
            return count, path[0]
    
    def deletar_produto(self):
        text_id = self.get_all_inputs_text()[0]
        
        path_name = self.get_path_by_id(
                PATH_PRODUTO, text_id)
        
        try:
            delete_db(f'{PATH_PRODUTO}/{path_name[1]}/{path_name[0]}')
            DeletadoSucesso(self)
        except:
            logging.warning("Item não existente")

    