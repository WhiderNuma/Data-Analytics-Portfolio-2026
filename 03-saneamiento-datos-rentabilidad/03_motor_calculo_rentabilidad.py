import pandas as pd

print("🚀 Iniciando Pipeline ETL: Fase de Transformación")

try:
    df_crudo = pd.read_csv('02_Data_Limpiada_SQL.csv')
    print("✅ Datos leídos con éxito desde el CSV.")
except FileNotFoundError:
    print("❌ Error: No se encontró el archivo. Asegúrate de estar en la carpeta correcta.")
    exit()

print("⚙️ Calculando Ingresos, Margen y ROI...")
df_crudo = df_crudo.rename(columns={'Cantidad_Vendida': 'Ventas'})

df_crudo['Ingresos'] = df_crudo['Precio_Unitario'] * df_crudo['Ventas']
df_crudo['Margen_Ganancia'] = (df_crudo['Precio_Unitario'] - df_crudo['Costo_Unitario']) * df_crudo['Ventas']
df_crudo['ROI_Porcentaje'] = (df_crudo['Margen_Ganancia'] / (df_crudo['Ingresos'] - df_crudo['Margen_Ganancia'])) * 100

columnas_finales = ['Producto', 'Ciudad', 'Ingresos', 'Margen_Ganancia', 'Ventas', 'ROI_Porcentaje']
df_retail = df_crudo[columnas_finales]

nombre_archivo_salida = '04- Reporte_Retail_Saneado.csv'

df_retail.to_csv(nombre_archivo_salida, index=False, sep=';')

print(f"📥 Pipeline Finalizado. Archivo generado: {nombre_archivo_salida}")