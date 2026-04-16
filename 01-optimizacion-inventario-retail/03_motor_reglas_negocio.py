import pandas as pd

print("🚀 Iniciando Pipeline de Inventario: Fase de Alertas Críticas")

try:
    df_inv = pd.read_csv('02_Logica_Inventario_SQL.csv')
    print("✅ Datos de inventario extraídos con éxito.")
except FileNotFoundError:
    print("❌ Error: No se encontró el archivo '02_Logica_Inventario_SQL.csv'.")
    exit()

print("⚙️ Calculando Stock Remanente y Niveles de Criticidad...")

df_inv['Stock_Remanente'] = df_inv['Stock_Inicial'] - df_inv['Ventas_Mes']

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

df_inv['Estado_Inventario'] = df_inv.apply(calcular_estado, axis=1)

nombre_archivo_salida = '04_inventario_final.csv'
df_inv.to_csv(nombre_archivo_salida, index=False, sep=';')

print(f"📥 Pipeline Finalizado. Reporte de auditoría generado en: '{nombre_archivo_salida}'")