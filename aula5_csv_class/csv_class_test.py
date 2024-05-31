import pandas as pd
from pathlib import Path

class CsvProcessor:
    def __init__(self, filepath: Path):
        self.filepath = filepath
        self.df = None
    
    def get_file(self):
        self.df = pd.read_csv(self.filepath)
        return self.df
    
    def filtra_por(self, coluna, atributo):
        return self.df[self.df[coluna] == atributo]

