# 🛒 Auditoría de Rentabilidad Retail: Saneamiento y Análisis de ROI

> **Nota de Portafolio:** Este proyecto aborda uno de los problemas más comunes en el análisis de datos: la "Entropía de Datos" en sistemas de venta manuales. El objetivo fue transformar una base de datos contaminada en una herramienta de decisión estratégica para la dirección comercial.

## 🎯 El Desafío de Negocio
Se detectó que el departamento de ventas registraba inconsistencias críticas: nombres de ciudades duplicados (ej. "bs as", "CABA", "Buenos Aires"), formatos de moneda tipo string y registros de fecha nulos. Sin sanear estos datos, el cálculo de rentabilidad real era imposible.

---

## 🏗️ Arquitectura de la Solución (Pipeline de Datos)

### 01 - Normalización y Saneamiento (SQL)
* **Data Wrangling:** Implementación de lógica `CASE WHEN` y `UPPER(TRIM())` para unificar la geografía de los puntos de venta.
* **Casteo de Tipos:** Transformación de datos sucios (strings con símbolos monetarios) a tipos `DECIMAL` para asegurar la precisión aritmética en los cálculos de margen.
* *Archivo:* `01- Limpieza_Ventas_Retail.sql`

### 02 - Enriquecimiento y ETL (Python)
* **Lógica de Negocio:** Automatización del cálculo del **ROI (Retorno de Inversión)** mediante Pandas, permitiendo identificar no solo cuánto se vende, sino qué tan eficiente es cada peso invertido por categoría.
* *Archivo:* `02- Limpieza_Ventas_Retail.py`

### 03 - Dataset de Auditoría (CSV)
* **Single Source of Truth:** Generación de un output estandarizado con métricas de rendimiento listas para el consumo de Business Intelligence.
* *Archivo:* `03_Reporte_Retail_Saneado.csv`

### 04 - Visualización Ejecutiva (Tableau)
* **Análisis de Proporción:** Uso de Treemaps para identificar jerarquías de margen por producto.
* **Diagnóstico Regional:** Gráficos de barras de ROI por ciudad que permiten detectar oportunidades de expansión o fallas en la distribución.
* *Visualización:* [**Ver Dashboard en Tableau Public**](https://public.tableau.com/app/profile/numa.cacho/viz/Libro1_17752683792050/Dashboard1)

---

## 🛠️ Stack Tecnológico
* **SQL:** Limpieza profunda de datos (Data Cleaning).
* **Python (Pandas):** Ingeniería de métricas de rentabilidad.
* **Tableau:** Visualización interactiva y dashboards de diagnóstico.

---
*Este proyecto cierra mi primer ciclo de especialización, demostrando capacidad técnica para limpiar, procesar y visualizar datos que impactan en el resultado económico de una empresa.*