import pandas as pd
from google.colab import files

# SIMULACIÓN DE EXTRACCIÓN: 
# Este dataframe representa el RESULTADO de ejecutar la consulta SQL 
# en el servidor de base de datos de la empresa.

data_resultado_sql = {
    'Producto_ID': [101, 102, 103, 104],
    'Nombre_Producto': ['Smartphone X', 'Laptop Gaming', 'Auriculares BT', 'Monitor 4K'],
    'Stock_Inicial': [100, 50, 200, 30], 
    'Ventas_Mes': [85, 35, 120, 5]       
}

df_inventario = pd.DataFrame(data_resultado_sql)

df_inventario['Stock_Remanente'] = df_inventario['Stock_Inicial'] - df_inventario['Ventas_Mes']

def calcular_estado(row):
    remanente = row['Stock_Remanente']
    inicial = row['Stock_Inicial']
    porcentaje = remanente / inicial
    
    if porcentaje <= 0.2:
        return '🔴 URGENTE: REABASTECER'
    elif porcentaje <= 0.4:
        return '🟡 ALERTA: STOCK BAJO'
    else:
        return '🟢 STOCK SUFICIENTE'

df_inventario['Estado_Inventario'] = df_inventario.apply(calcular_estado, axis=1)

df_inventario.to_csv('Reporte_Inventario_Final.csv', index=False, sep=';', encoding='utf-8-sig')

files.download('Reporte_Inventario_Final.csv')

print("✅ Reporte generado con éxito y coherencia total con SQL.")
print(df_inventario[['Nombre_Producto', 'Stock_Remanente', 'Estado_Inventario']])