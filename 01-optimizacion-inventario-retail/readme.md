# Módulo Analítico: Optimización de Inventario y Alertas Críticas (PoC)

Este directorio contiene la implementación técnica de una **Prueba de Concepto (PoC)** orientada a la cadena de suministro retail. El sistema transforma datos transaccionales crudos en alertas de reabastecimiento en tiempo real, mitigando riesgos operativos y lucro cesante por quiebre de stock.

## 🎯 Objetivo del Módulo
Diseñar y desplegar un pipeline de datos capaz de calcular la criticidad del inventario basándose en un modelo de umbrales proporcionales (20% y 40% respecto al stock inicial), en lugar de topes estáticos. 

## 🏗️ Arquitectura Desacoplada
El flujo de datos está diseñado bajo una arquitectura modular multi-lenguaje. Esto garantiza el desacoplamiento entre la extracción, el procesamiento de reglas de negocio y la capa semántica de visualización.

### 01. Capa de Extracción (Base de Datos)
* **Archivo:** `01_extracccion_base_datos.sql`
* **Salida:** `02_dataset_raw.csv`
* **Lógica:** Consultas relacionales (CTEs y cruces transaccionales) para consolidar el inventario físico inicial con el volumen de salidas. Actúa como el punto de ingesta para obtener el dataset en crudo (Raw).

### 02. Motor de Lógica de Negocio (Procesamiento ETL)
* **Archivo:** `03_motor_reglas_negocio.py`
* **Salida:** `04_dataset_gold.csv`
* **Lógica:** Script de Python (Pandas) que procesa el dataset Raw en memoria. Calcula remanentes, aplica la vectorización de alertas dinámicas y exporta un dataset certificado ("Gold") estandarizado y listo para consumo en herramientas de Business Intelligence.

### 03. Capa de Inteligencia de Negocios (Visualización)
* **Archivo:** `05_dashboard_ejecutivo.twb`
* **Lógica:** Tablero de control en Tableau conectado directamente al dataset Gold. Optimizado para la lectura gerencial, permitiendo al departamento de compras identificar productos en estado "🔴 URGENTE" o "🟡 ALERTA" de manera inmediata.

## 🛠️ Stack Tecnológico Implementado
* **Extracción y Modelado:** SQL.
* **Transformación y Reglas (ETL):** Python (Pandas).
* **Consumo y Decisión:** Tableau.

---
*Nota de Arquitectura: La división en capas (SQL -> Python -> BI) garantiza que la lógica de alertas pueda escalar a millones de SKUs o integrarse con bases de datos en producción sin alterar la capa de visualización.*