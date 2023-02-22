import customtkinter
from PIL import ImageTk, Image
from tkinter import filedialog
from func import *
import tkinter as tk

global PADRAO_TRANSPORTADORA, PADRAO_PRODUTO, PATH_PRODUTO, PATH_TRANSPORTADORA

PATH_TRANSPORTADORA = DbLink().PATHS[0]
PADRAO_TRANSPORTADORA = DbLink().PADRAO_DADOS[0]
PATH_PRODUTO = DbLink().PATHS[1]
PADRAO_PRODUTO = DbLink().PADRAO_DADOS[1]