import streamlit as st
import pandas as pd
from pathlib import Path
from reader.main import choose_directory, main

st.title("🎞️ String Reader - OCR de vídeos")

if st.button("Escolher pasta de vídeos"):
    selected_path = choose_directory()
    if selected_path:
        st.session_state["selected_path"] = str(selected_path)
        st.success(f"Pasta selecionada: {selected_path}")
    else:
        st.warning("Nenhuma pasta foi selecionada.")

if "selected_path" in st.session_state:
    if st.button("Executar OCR"):
        with st.spinner("Processando vídeos..."):
            output_file = main(Path(st.session_state["selected_path"]))
        st.success(f"✅ OCR finalizado! Arquivo salvo na sua pasta de Downloads")
