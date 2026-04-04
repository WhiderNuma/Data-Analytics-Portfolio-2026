# 💰 Análisis de Flujo de Caja y Proyección de Ahorro Estratégico

> **Nota de Portafolio:** Este proyecto presenta una solución de ingeniería financiera diseñada para monitorizar la solvencia y capacidad de ahorro en proyectos de relocalización. Representa un ejemplo real de cómo transformo registros transaccionales en indicadores de viabilidad económica.

## 🎯 Objetivo del Proyecto
El cliente requería una herramienta de control financiero para determinar el horizonte temporal necesario para alcanzar un capital de reserva de **$1,000,000 ARS**. Se implementó un pipeline que consolida ingresos y egresos, calculando el ahorro neto mensual y proyectando el cumplimiento de hitos financieros.

---

## 🏗️ Arquitectura de la Solución
La solución se despliega en 4 capas técnicas que aseguran la precisión del flujo de caja:

### 01 - Modelado de Datos y Lógica de Ventana (SQL)
Fase de estructuración en el motor de base de datos.
* **Ingeniería de Datos:** Creación de tablas transaccionales con tipado estricto para ingresos y egresos.
* **Análisis Avanzado:** Implementación de **Window Functions** (`SUM OVER`) para generar el ahorro acumulado dinámico, permitiendo un seguimiento histórico sin redundancia de datos.
* *Archivo:* `01- Analisis_Flujo_Caja.sql`

### 02 - Automatización y ETL (Python)
Desarrollo de la lógica de procesamiento para la estandarización de reportes mensuales.
* **Procesamiento:** El script actúa como capa de transformación (ETL), consolidando categorías y calculando los saldos netos operativos.
* **Sincronización:** Generación de un output optimizado que garantiza la coherencia numérica entre la base de datos y la capa de visualización.
* *Archivo:* `02- Analisis Flujo De Caja.py`

### 03 - Dataset Estructurado (CSV)
Fuente de verdad única (Single Source of Truth) resultante del proceso de ingeniería. Contiene la serie temporal depurada y lista para auditoría financiera o consumo de BI.
* *Archivo:* `03- Flujo_Caja_Final.csv`

### 04 - Business Intelligence y Dashboards (Tableau)
Capa de visualización orientada a la toma de decisiones ejecutivas.
* **Visualización de Impacto:** Diseño de un gráfico de eje doble (Dual Axis) que permite comparar el flujo neto mensual contra la curva de crecimiento del ahorro total.
* **Análisis de Metas:** Inclusión de una línea de referencia dinámica que identifica el mes exacto de cumplimiento del objetivo financiero ("LISTO PARA MUDARSE").
* *Visualización:* [**Acceder al Dashboard Interactivo aquí**](https://public.tableau.com/app/profile/numa.cacho/viz/Analisis_Flujo_Caja/Hoja2?publish=yes)

---

## 🛠️ Stack Tecnológico
* **SQL:** Análisis transaccional y funciones de agregación avanzada.
* **Python (Pandas):** Automatización de ETL y lógica de saldos.
* **Tableau:** Visualización estratégica y seguimiento de KPIs financieros.

---
*Este proyecto demuestra la capacidad de traducir datos financieros crudos en una hoja de ruta clara para el cumplimiento de objetivos económicos de mediano plazo.*