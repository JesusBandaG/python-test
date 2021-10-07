import pandas as pd

def extract_data():
  fileName = input("Ingrese la ruta del archivo en formato csv: ")
  print(f"Ha seleccionado el archivo '{fileName}'.")
  df = pd.read_csv(fileName, sep=';')
  return df

def transform_data(df):
  clientes = df[['A', 'C', 'D']].copy()

def load_data(df):
  print("Loading data...")

if __name__ == '__main__':
  df = extract_data()
  transform_data(df)
  load_data()