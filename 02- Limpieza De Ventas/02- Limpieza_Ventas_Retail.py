import pandas as pd
from google.colab import files

data_auditoria = {
    'Producto': ['SMARTPHONE PRO', 'TELEVISOR 4K', 'AURICULARES BT', 'SMARTPHONE PRO', 'TELEVISOR 4K'],
    'Ciudad': ['Bariloche', 'Buenos Aires', 'Buenos Aires', 'Bariloche', 'Buenos Aires'],
    'Ingresos': [3600.0, 5000.0, 2000.0, 9600.0, 2500.0],
    'Margen_Ganancia': [1200.0, 1500.0, 1250.0, 3200.0, 750.0],
    'Ventas': [3, 10, 25, 8, 5]
}

df_retail = pd.DataFrame(data_auditoria)

df_retail['ROI_Porcentaje'] = (df_retail['Margen_Ganancia'] / (df_retail['Ingresos'] - df_retail['Margen_Ganancia'])) * 100

df_retail.to_csv('03_Reporte_Retail_Saneado.csv', index=False, sep=';')
files.download('03_Reporte_Retail_Saneado.csv')

print("✅ Pipeline Retail: Dataset generado para BI.")