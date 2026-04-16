import pandas as pd


try:
    df_flujo = pd.read_csv('02_Flujo_Caja_SQL.csv')
    print("✅ Datos extraídos de SQL.")
except FileNotFoundError:
    print("❌ Error: No se encuentra el archivo 02.")
    exit()

df_flujo = df_flujo.sort_values(by='Mes_ID')
df_flujo['Ahorro_Acumulado'] = df_flujo['Monto_Neto'].cumsum()
META = 1000000
df_flujo['Estado_Meta'] = df_flujo['Ahorro_Acumulado'].apply(lambda x: 'ALCANZADA' if x >= META else 'EN PROGRESO')

nombre_salida = '04_Flujo_Caja_Final.csv'
df_flujo.to_csv(nombre_salida, index=False, sep=';')
print(f"✅ Archivo {nombre_salida} generado con éxito.")