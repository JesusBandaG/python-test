import pandas as pd

def extract_data():
  fileName = input("Ingrese la ruta del archivo en formato csv: ")
  print(f"Ha seleccionado el archivo '{fileName}'.")
  dtypes = {
    'fiscal_id': 'str',
    'first_name': 'str',
    'last_name': 'str',
    'gender': 'str',
    'fecha_nacimiento': 'str',
    'fecha_vencimiento': 'str',
    'deuda': 'int16',
    'direccion': 'str',
    'altura': 'int16',
    'peso': 'int16',
    'correo': 'str',
    'estatus_contacto': 'str',
    'prioridad': 'float',
    'telefono': 'str'
    }
  parse_dates = ['fecha_nacimiento', 'fecha_vencimiento']
  df = pd.read_csv(fileName, sep=';', dtype=dtypes, parse_dates=parse_dates)
  df["prioridad"] = df['prioridad'].astype(pd.Int16Dtype())
  return df

def transform_data(df):
  clientes = df[['A', 'C', 'D']].copy()

def load_data(df):
  print("Loading data...")

if __name__ == '__main__':
  df = extract_data()
  transform_data(df)
  load_data()