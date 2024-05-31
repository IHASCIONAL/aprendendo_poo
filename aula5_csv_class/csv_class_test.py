import pandas as pd
from pathlib import Path

class CsvProcessor:
    def __init__(self, filepath: Path):
        self.filepath = filepath
        self.df = None
        self.df_filtrado = None
    
    def get_file(self):
        self.df = pd.read_csv(self.filepath)
        return self.df
    
    def filtra_por(self, colunas, atributos):
        if len(colunas) != len(atributos):
            raise ValueError("Não tem o mesmo número de colunas e atributos")
        
        elif len(colunas) == 0:
            return self.df
        
        coluna_atual = colunas[0]
        atributo_atual = atributos[0]

        df_filtrado = self.df[self.df[coluna_atual] == atributo_atual]

        if len(colunas) == 1:
            return df_filtrado
        else:
            return self.filtra_por(colunas[1:], atributos[1:])


        

