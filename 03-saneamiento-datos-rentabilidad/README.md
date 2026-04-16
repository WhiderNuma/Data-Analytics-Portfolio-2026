# Módulo Analítico: Saneamiento de Datos y Auditoría de Rentabilidad (PoC)

Este directorio contiene una **Prueba de Concepto (PoC)** centrada en el proceso de *Data Quality* e Ingeniería Financiera. Resuelve el desafío de consolidar bases de datos transaccionales con formatos inconsistentes (monedas, fechas, strings sucios y errores de carga manual) para transformarlas en un modelo analítico confiable que permita auditar el Retorno de Inversión (ROI) y los márgenes comerciales.

## 🎯 Objetivo del Módulo
Garantizar la veracidad de los datos financieros (Single Source of Truth) mediante la normalización de campos críticos. A partir del dato limpio, el pipeline calcula KPIs de rentabilidad a nivel de producto y región, permitiendo identificar qué segmentos sostienen operativamente a la empresa.

## 🏗️ Arquitectura Desacoplada
El flujo se divide en un pipeline de 3 capas, separando el *Data Wrangling* transaccional del cálculo financiero vectorial.

### 01. Capa de Normalización (Base de Datos)
* **Archivo:** `01_extraccion_y_normalizacion.sql`
* **Salida:** `02_dataset_raw.csv`
* **Lógica:** Consultas SQL avanzadas para la limpieza y tipado de datos en crudo. Implementa funciones de manipulación de cadenas (`TRIM`, `UPPER`, `REPLACE`), casteo de variables monetarias y estandarización geoespacial (`CASE` para homologar sucursales inconsistentes como 'CABA' y 'bs as'). 

### 02. Motor de Rentabilidad (Procesamiento ETL)
* **Archivo:** `03_motor_calculo_rentabilidad.py`
* **Salida:** `04_dataset_gold.csv`
* **Lógica:** Script de Python (Pandas) que ingiere los datos normalizados y actúa como motor financiero. Computa variables de negocio calculadas: Ingresos Brutos, Margen de Ganancia Neto y Porcentaje de ROI, exportando el dataset final ("Gold") optimizado para lectura.

### 03. Capa de Inteligencia de Negocios (Visualización)
* **Archivo:** `05_dashboard_auditoria.twb`
* **Lógica:** Tablero de control en Tableau diseñado para auditoría ejecutiva. Cruza el volumen de ventas con el ROI_Porcentaje, permitiendo detectar rápidamente productos de alta rotación pero bajo margen, o viceversa.

## 🛠️ Stack Tecnológico Implementado
* **SQL:** *Data Wrangling*, control de nulos (`COALESCE`) y estandarización de formatos.
* **Python (Pandas):** Vectorización de fórmulas financieras (Margen y ROI).
* **Tableau:** Auditoría visual y segmentación de rentabilidad.

---
*Nota de Arquitectura: La delegación de la limpieza profunda de strings al motor SQL asegura que el procesamiento en memoria de Python se dedique exclusivamente al cálculo matemático, optimizando el uso de recursos ante el escalado del dataset.*