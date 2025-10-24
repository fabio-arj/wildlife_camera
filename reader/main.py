from .ocr_extraction import run_ocr
from pathlib import Path
import pandas as pd
import os
import tkinter as tk
from tkinter import filedialog
from win11toast import toast

def choose_directory() -> Path | None:
    root = tk.Tk()
    root.withdraw()
    root.title("String Reader")              
    root.geometry("0x0")                                                 
    root.attributes("-topmost", True)         
    folder_selected = filedialog.askdirectory(title="Selecione a pasta com os vídeos", parent=root)
    root.destroy()                          
    return Path(folder_selected) if folder_selected else None 

def main():
    path = choose_directory()
    if not path:
        toast("Operação cancelada", "Nenhum diretório foi selecionado.")
        return

    toast("Processando vídeos...", "O reconhecimento de texto está em andamento, aguarde.")

    df = run_ocr(path)

    home_dir = os.path.expanduser("~")
    downloads_path = os.path.join(home_dir, "Downloads", "output.csv")
    df.to_csv(downloads_path, index=False)

    toast("Processo concluído!", f"Arquivo salvo na sua pasta de Downloads")

if __name__ == "__main__":
    main()
