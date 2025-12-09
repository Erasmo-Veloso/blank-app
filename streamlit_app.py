import streamlit as st
import pandas as pd
import json

def main():
    st.title("Conversor Excel → JSON com Filtro de Colunas")

    uploaded_file = st.file_uploader("Carregue um arquivo Excel", type=["xlsx", "xls"])

    if uploaded_file:
        # Ler todas as sheets do Excel
        xls = pd.ExcelFile(uploaded_file)
        sheets = xls.sheet_names

        st.subheader("Selecione o livro (sheet) para converter")
        sheet_selecionada = st.selectbox("Escolha o livro", sheets)

        # Carregar a sheet selecionada
        df = pd.read_excel(uploaded_file, sheet_name=sheet_selecionada)
        st.subheader("Pré-visualização dos dados")
        st.dataframe(df)

        st.subheader("Selecione as colunas que deseja manter")
        colunas = df.columns.tolist()
        colunas_selecionadas = st.multiselect("Colunas para manter", colunas, default=colunas)

        if st.button("Converter para JSON"):
            df_filtrado = df[colunas_selecionadas]
            json_resultado = df_filtrado.to_json(orient="records", force_ascii=False, indent=2)

            st.subheader("Resultado em JSON")
            st.code(json_resultado, language="json")

            # Download
            st.download_button(
                "Baixar JSON",
                data=json_resultado,
                file_name="resultado.json",
                mime="application/json"
            )

if __name__ == "__main__":
    main()
