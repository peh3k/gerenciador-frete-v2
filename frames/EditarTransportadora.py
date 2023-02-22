from frames.FramesDependences import *
from frames.Popus import AtualizadoSucessoPopup, ErroInesperadoPopup, DeletadoSucesso


class EditarTransportadoraScreen(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.CHOICE_COMBO_BOX = []

        trash_img = ImageTk.PhotoImage(Image.open(
            "images/trash.png").resize((15, 15)))

        NOMES_EMPRESAS = get_names_db(PATH_TRANSPORTADORA)

        def combobox_callback(choice):
            self.CHOICE_COMBO_BOX.clear()
            self.CHOICE_COMBO_BOX.append(choice)
            self.clear_all_entries()
            all_input_ids = self.get_all_inputs()
            dict_name = self.get_dict_from_name(PATH_TRANSPORTADORA, choice)
            dict_organized = organize_dict(dict_name[0], PADRAO_TRANSPORTADORA)
            itens = [item for item in dict_organized.values()]
            del itens[0]
            del itens[0]
            for i in range(len(all_input_ids)):
                all_input_ids[i].insert(0, itens[i])

        label_nome = customtkinter.CTkLabel(
            self, text="Empresa:").grid(row=0, column=0, pady=20, padx=10)
        combobox = customtkinter.CTkComboBox(
            self, values=NOMES_EMPRESAS, command=combobox_callback)
        combobox.grid(row=0, column=1)
        combobox.set('-')
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
            self, width=85, height=25, border_width=1, corner_radius=2, placeholder_text="Ex: 000000-00").grid(row=3, column=1)
        label_cepfinal = customtkinter.CTkLabel(
            self, text="Cep Final:").grid(row=4, column=0, pady=20, padx=10)
        self.cep_final = customtkinter.CTkEntry(
            self, width=85, height=25, border_width=1, corner_radius=2, placeholder_text="Ex: 000000-00").grid(row=4, column=1)
        label_prazo = customtkinter.CTkLabel(self, text="Prazo:").grid(
            row=5, column=0, pady=20, padx=10)
        self.prazo = customtkinter.CTkEntry(
            self, width=85, height=25, border_width=1, corner_radius=2, placeholder_text="Ex: 13").grid(row=5, column=1)
        label_estado = customtkinter.CTkLabel(
            self, text="Estado:").grid(row=0, column=2, pady=20, padx=10)
        self.estado = customtkinter.CTkEntry(
            self, width=85, height=25, border_width=1, corner_radius=2, placeholder_text="Ex: sp").grid(row=0, column=3)
        label_cidade = customtkinter.CTkLabel(
            self, text="Cidade:").grid(row=1, column=2, pady=20, padx=10)
        self.cidade = customtkinter.CTkEntry(
            self, width=85, height=25, border_width=1, corner_radius=2, placeholder_text="Ex: osasco").grid(row=1, column=3)
        label_regiao = customtkinter.CTkLabel(
            self, text="Região:").grid(row=2, column=2, pady=20, padx=10)
        self.regiao = customtkinter.CTkEntry(
            self, width=85, height=25, border_width=1, corner_radius=2, placeholder_text="Ex: sudeste").grid(row=2, column=3)
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
        button_excluir = customtkinter.CTkButton(
            self, text="Excluir", image=trash_img, corner_radius=7, height=30,  width=100, fg_color="#ff3333", hover_color="#ff1a1a", command=self.excluir_transportadora)
        button_excluir.grid(row=6, column=0, padx=25, pady=20)
        button_atualizar = customtkinter.CTkButton(
            self, text="Atualizar", corner_radius=7, height=30,  width=100, fg_color="#3d9336", hover_color="#51bc48", command=self.atualizar_transportadora)
        button_atualizar.grid(row=6, column=5, pady=20)

    def get_all_inputs(self):
        all_inputs = [child for child in self.winfo_children(
        ) if isinstance(child, customtkinter.CTkEntry)]

        return all_inputs

    def get_all_inputs_text(self):
        all_inputs = [child.get() for child in self.winfo_children(
        ) if isinstance(child, customtkinter.CTkEntry)]

        return all_inputs

    def clear_all_entries(self):
        for child in self.winfo_children():
            if isinstance(child, customtkinter.CTkEntry):
                child.delete(0, tk.END)

    def atualizar_transportadora(self):

        try:
            all_texts = self.get_all_inputs_text()
            path_name = self.get_path_by_name(
                PATH_TRANSPORTADORA, self.CHOICE_COMBO_BOX[0])
            
            new_texts = []
            new_texts.append(all_texts)
            dict = list_to_dict(new_texts, PADRAO_TRANSPORTADORA[2:])
            patch_db(
                f'{PATH_TRANSPORTADORA}/{path_name[1]}/{path_name[0]}', dict[0])
            AtualizadoSucessoPopup(self)
            self.clear_all_entries()
            
        except:
            logging.warning("Erro atualizar transportadora")
            ErroInesperadoPopup(self)

    def excluir_transportadora(self):
        
        path_name = self.get_path_by_name(
                PATH_TRANSPORTADORA, self.CHOICE_COMBO_BOX[0])
        
        try:
            delete_db(f'{PATH_TRANSPORTADORA}/{path_name[1]}/{path_name[0]}')
            DeletadoSucesso(self)
        except:
            logging.warning("Item não existente")

    def get_path_by_name(self,table, name):
        all_data = get_db(table)
        filtro = [all_data[item].remove(lista) for item in all_data for lista in all_data[item] if lista is None]
        path = []
        count = -1
        for item in all_data:
            count = -1
            for lista in all_data[item]:
                count += 1
                if lista['nome'] == name:
                    path.append(item)
                    break
        
        if len(path) == 0:
            logging.exception("item não existe")
            return count
        else:
            return count, path[0]

    
    def get_dict_from_name(self, table, name):
        all_data = get_db(table)
        filtro = [all_data[item].remove(lista) for item in all_data for lista in all_data[item] if lista is None]
        
        
        # Nova lista com nenhuma lista None para interferir
        same_name = [lista for key in all_data for lista in all_data[key] if lista['nome'] == name]
        
        return same_name
                
        