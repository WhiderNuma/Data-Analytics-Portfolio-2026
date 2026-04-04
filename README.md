# Numa Cacho | Data Analyst Portafolio 🚀

**📍 Ubicación:** Argentina (Disponibilidad de relocalización a Buenos Aires)
**✉️ Contacto:** [numacacho@gmail.com](mailto:numacacho@gmail.com) | **[https://www.linkedin.com/in/numa-cacho-162a48325/]** | **[https://www.hackerrank.com/profile/numajulian]**

---

### 🌐 Executive Summary
> *Data Analyst focused on transforming high-entropy datasets into strategic business assets. Specialized in designing end-to-end data pipelines (ETL) and leveraging Python and SQL to optimize operational and financial decision-making.*

---

## 🎯 Filosofía Analítica
Mi enfoque se centra en la **rentabilidad del dato**. No me limito a limpiar bases de datos "por si acaso"; diseño flujos de trabajo estructurados que traducen la entropía de los datos transaccionales en respuestas directas a problemas de negocio. Si una métrica no ayuda a tomar una decisión, es solo ruido.

## 🛠️ Stack Tecnológico Principal
* **Bases de Datos & Extracción:** SQL (MySQL, BigQuery) | *HackerRank SQL Intermediate Certified 🏆*
* **Procesamiento & Data Wrangling (ETL):** Python (Pandas, NumPy, Regex)
* **Inteligencia de Negocios (BI):** Tableau, Excel Avanzado / Google Sheets
* **Ingeniería Analítica:** CTEs, Window Functions, Modelado Relacional.

---

## 📂 Proyectos Destacados (End-to-End Pipelines)

Los siguientes proyectos han sido desarrollados bajo una arquitectura de datos estandarizada: 
`Extracción Cruda (SQL)` ➔ `Puente de Datos (CSV Plano)` ➔ `Lógica de Negocio (Python)` ➔ `Dataset Saneado` ➔ `Visualización (Tableau)`.

### 1. [🛒 Auditoría de Rentabilidad Retail (Data Wrangling & ROI)](https://github.com/WhiderNuma/Data-Analytics-Portfolio-2026/tree/main/02-%20Limpieza%20De%20Ventas)
**Problema:** Inconsistencias geográficas y formatos de moneda corruptos (Entropía de Datos) que impedían el cálculo real de ganancias.
* **Capa SQL:** Normalización de strings (`TRIM`, `UPPER`) y estandarización de tipos de datos transaccionales.
* **Capa Python:** Ingesta del dataset limpio mediante Pandas para la automatización del cálculo de **Retorno de Inversión (ROI)** por categoría de producto.
* **Impacto:** Generación de un *Single Source of Truth* que permite a la gerencia identificar qué productos sostienen la rentabilidad regional y cuáles generan pérdidas operativas.

### 2. [📊 Optimización de Inventario (Alertas Dinámicas Operativas)](https://github.com/WhiderNuma/Data-Analytics-Portfolio-2026/tree/main/03-%20Optimización%20De%20Inventario)
**Problema:** Quiebres de stock continuos debido a un monitoreo deficiente entre las ventas y el almacenamiento físico.
* **Capa SQL:** Uso intensivo de **Common Table Expressions (CTEs)** para cruzar tablas relacionales de inventario inicial vs. flujo de ventas.
* **Capa Python:** Desarrollo de un algoritmo que no utiliza umbrales fijos, sino que calcula la **proporcionalidad del stock remanente**, disparando alertas de criticidad (`URGENTE`, `ALERTA`) basadas en porcentajes de consumo.
* **Impacto:** Sistema de alertas escalable que mitiga el riesgo de pérdida de facturación por desabastecimiento.

### 3. [💰 Proyección de Flujo de Caja (Modelado Financiero temporal)](https://github.com/WhiderNuma/Data-Analytics-Portfolio-2026/tree/main/01-%20Analisis%20Flujo%20De%20Caja)
**Problema:** Necesidad de trackear la solvencia económica para alcanzar un hito de capitalización específico ($1,000,000 ARS).
* **Capa SQL:** Implementación avanzada de **Window Functions** (`SUM() OVER`) para calcular el crecimiento del ahorro acumulado sin perder la granularidad de los registros diarios.
* **Capa Python:** Aplicación de métodos acumulativos de series temporales para etiquetar automáticamente el estado de la meta financiera.
* **Impacto:** Dashboard ejecutivo en Tableau de doble eje (Dual Axis) que cruza el flujo neto mensual contra la curva de acumulación, identificando el mes exacto de viabilidad del proyecto.

---

## ⚙️ Metodología de Trabajo y Calidad de Código
Todos los repositorios incluyen:
1. **Documentación técnica detallada** sobre la arquitectura de la solución.
2. **Archivos numerados** que garantizan la reproducibilidad del pipeline (`01_sql`, `02_csv`, `03_py`, etc.).
3. **Manejo de excepciones** en Python para asegurar la integridad en la lectura de archivos locales.