# 📊 End-to-End Data Analytics Pipelines

Bienvenido a este repositorio. Aquí se agrupan tres proyectos integrales de análisis de datos orientados a resolver problemas críticos de negocio en tres áreas clave: **Comercial, Operativa y Financiera**.

El objetivo principal de este repositorio es demostrar la capacidad de diseñar e implementar **flujos de trabajo completos (Pipelines ETL)**, abarcando desde la limpieza de registros transaccionales crudos hasta la creación de visualizaciones ejecutivas para la toma de decisiones.

---

## ⚙️ Arquitectura Estandarizada
Para garantizar la integridad del dato, la reproducibilidad y la trazabilidad, los tres proyectos operan bajo una metodología de 5 capas secuenciales:

1. **Extracción y Saneamiento (`.sql`):** Uso de bases de datos relacionales para limpieza inicial (Data Wrangling), estructuración mediante CTEs y Window Functions.
2. **Puente de Datos (`.csv`):** Exportación de datos limpios en formato de texto plano para evitar corrupciones de metadatos.
3. **Transformación y Lógica de Negocio (`.py`):** Ingesta mediante la librería Pandas en Python para aplicar cálculos de métricas, lógica condicional escalable y acumulaciones.
4. **Golden Record (`.csv`):** Generación del dataset final estandarizado (*Single Source of Truth*).
5. **Business Intelligence (`.twb`):** Consumo del dataset mediante Tableau para el desarrollo de Dashboards interactivos y analíticos.

---

## 📂 Contenido del Repositorio

### 1. [🛒 Auditoría de Rentabilidad Retail](https://github.com/WhiderNuma/Data-Analytics-Portfolio-2026/tree/main/01-%20Analisis%20Flujo%20De%20Caja)
**Enfoque: Saneamiento de Datos y Cálculo de ROI.**
Se aborda el problema de la "Entropía de Datos" en sistemas de venta manuales. El pipeline normaliza inconsistencias geográficas y formatos de moneda corruptos (`UPPER`, `TRIM`, Casteos) para automatizar el cálculo real del Retorno de Inversión (ROI) por categoría de producto.

### 2. [📦 Optimización de Inventario y Alertas Críticas](https://github.com/WhiderNuma/Data-Analytics-Portfolio-2026/tree/main/03-%20Optimización%20De%20Inventario)
**Enfoque: Lógica Transaccional y Mitigación de Riesgos.**
Diseñado para evitar pérdidas económicas por quiebres de stock. El flujo cruza inventarios físicos con volúmenes de venta y reemplaza los umbrales fijos por un algoritmo de **proporcionalidad de stock** en Python, disparando alertas operativas dinámicas (`URGENTE`, `ALERTA`).

### 3. [💰 Análisis de Flujo de Caja y Proyección](https://github.com/WhiderNuma/Data-Analytics-Portfolio-2026/tree/main/02-%20Limpieza%20De%20Ventas)
**Enfoque: Modelado Financiero y Series Temporales.**
Solución de ingeniería financiera para monitorizar la solvencia y capacidad de ahorro frente a un objetivo de capitalización. Destaca por el uso de **Window Functions** (`SUM OVER`) en SQL para el cálculo de saldos dinámicos sin perder la granularidad de los registros diarios.

---

## 🛠️ Stack Tecnológico Global
* **Bases de Datos:** SQL (MySQL)
* **Automatización y ETL:** Python (Pandas)
* **Inteligencia de Negocios:** Tableau
* **Control de Versiones:** Git / GitHub