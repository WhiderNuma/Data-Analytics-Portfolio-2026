import pandas as pd
from google.colab import files

data = [
    {'Mes_ID': 1, 'Mes_Nombre': '01-Enero', 'Categoria': 'Ayuda Familiar', 'Tipo': 'Ingreso', 'Monto': 150000},
    {'Mes_ID': 2, 'Mes_Nombre': '02-Febrero', 'Categoria': 'Ayuda Familiar', 'Tipo': 'Ingreso', 'Monto': 150000},
    {'Mes_ID': 3, 'Mes_Nombre': '03-Marzo', 'Categoria': 'Ayuda Familiar', 'Tipo': 'Ingreso', 'Monto': 150000},
    {'Mes_ID': 4, 'Mes_Nombre': '04-Abril', 'Categoria': 'Sueldo Junior (Est)', 'Tipo': 'Ingreso', 'Monto': 800000},
    {'Mes_ID': 4, 'Mes_Nombre': '04-Abril', 'Categoria': 'Gastos Fijos', 'Tipo': 'Egreso', 'Monto': 250000},
    {'Mes_ID': 5, 'Mes_Nombre': '05-Mayo', 'Categoria': 'Sueldo Junior (Est)', 'Tipo': 'Ingreso', 'Monto': 800000},
    {'Mes_ID': 5, 'Mes_Nombre': '05-Mayo', 'Categoria': 'Gastos Fijos', 'Tipo': 'Egreso', 'Monto': 250000},
    {'Mes_ID': 6, 'Mes_Nombre': '06-Junio', 'Categoria': 'Sueldo Junior (Est)', 'Tipo': 'Ingreso', 'Monto': 850000},
    {'Mes_ID': 6, 'Mes_Nombre': '06-Junio', 'Categoria': 'Gastos Fijos', 'Tipo': 'Egreso', 'Monto': 280000}
]

df_flujo = pd.DataFrame(data)

df_flujo['Monto_Neto'] = df_flujo.apply(lambda x: x['Monto'] if x['Tipo'] == 'Ingreso' else -x['Monto'], axis=1)

df_resumen = df_flujo.groupby(['Mes_ID', 'Mes_Nombre'])['Monto_Neto'].sum().reset_index()
df_resumen['Ahorro_Acumulado'] = df_resumen['Monto_Neto'].cumsum()

df_resumen.to_csv('Flujo_Caja_Final.csv', index=False, sep=';')
files.download('Flujo_Caja_Final.csv')

print("✅ ETL de Flujo de Caja completado con éxito.")