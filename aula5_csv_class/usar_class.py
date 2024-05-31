from csv_class_test import CsvProcessor

arquivo = "exemplo.csv"
coluna_filtro = "estado"
atributo = "SP"

arquivoCSV = CsvProcessor(arquivo)
arquivoCSV.get_file()
df_filtrado = arquivoCSV.filtra_por(coluna_filtro, atributo)

print(df_filtrado)
