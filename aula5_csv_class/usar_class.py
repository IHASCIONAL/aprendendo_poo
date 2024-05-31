from csv_class_test import CsvProcessor

arquivo = "exemplo.csv"
colunas_filtro = ["estado", "preço"]
atributos = ["SP", "100.50"]

arquivoCSV = CsvProcessor(arquivo)
arquivoCSV.get_file()
df_filtrado = arquivoCSV.filtra_por(colunas_filtro, atributos)

print(df_filtrado)
