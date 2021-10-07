import pandas as pd
from datetime import datetime
from datetime import date

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
  df = df.applymap(lambda value: value.upper() if type(value) == str else value)
  df["prioridad"] = df['prioridad'].astype(pd.Int64Dtype())

  return df

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def define_age_group(age):
  bins= [0, 20, 30, 40, 50, 60, 110]
  labels = [1, 2, 3, 4, 5, 6]
  age_group_df = pd.cut(age, bins=bins, labels=labels)
  return age_group_df

def transform_data(df):
  # Clients table
  age = df['fecha_nacimiento'].apply(calculate_age)
  clients = df.iloc[:, :8].copy()
  clients.insert(5, "age", age)
  age_group = define_age_group(clients['age'])
  clients.insert(6, "age_group", age_group)
  delinquency = (datetime.today() - clients['fecha_vencimiento']).dt.days
  clients.insert(8, "delinquency", delinquency)
  new_clients_names = {'fecha_nacimiento': 'birth_date', 'fecha_vencimiento': 'due_date', 'deuda': 'due_balance', 'direccion': 'address'}
  clients = clients.rename(columns=new_clients_names)

  # Emails table
  emails_cols = ['fiscal_id', 'correo', 'estatus_contacto', 'prioridad']
  emails = df[emails_cols].copy()
  new_emails_names = {'correo': 'email', 'estatus_contacto': 'status', 'prioridad': 'priority'}
  emails = emails.rename(columns=new_emails_names)

  # Phones table
  phones_cols = ['fiscal_id', 'telefono', 'estatus_contacto', 'prioridad']
  phones = df[phones_cols].copy()
  new_phones_names = {'telefono': 'phone', 'estatus_contacto': 'status', 'prioridad': 'priority'}
  phones = phones.rename(columns=new_phones_names)

  # Saving tables in Excel files
  clients.to_excel('clientes.xlsx', index=False)
  emails.to_excel('emails.xlsx', index=False)
  phones.to_excel('phones.xlsx', index=False)

def load_data(df):
  print("Loading data...")

if __name__ == '__main__':
  df = extract_data()
  transform_data(df)
  load_data()