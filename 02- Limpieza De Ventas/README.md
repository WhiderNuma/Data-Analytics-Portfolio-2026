# 📊 Optimización de Inventario y Alertas Críticas (Retail)

> **Nota de Portafolio:** Este proyecto es una solución funcional diseñada para la gestión de activos y mitigación de riesgos operativos. El objetivo es demostrar la arquitectura técnica y la lógica de negocio aplicada al control de stock.

## 🎯 Objetivo del Proyecto
El cliente presentaba ineficiencias en la cadena de suministro y pérdidas económicas por quiebres de stock no detectados. Se diseñó un **pipeline de datos** que automatiza la monitorización de niveles de inventario, permitiendo al departamento de compras ejecutar reposiciones proactivas mediante un sistema de alertas dinámicas.

---

## 🏗️ Arquitectura de la Solución (Pipeline 1-5)

La solución se estructura en 5 fases técnicas integradas que garantizan la trazabilidad de la información:

### 01 - Extracción y Modelado (SQL)
* **Lógica de Negocio:** Implementación de consultas avanzadas mediante **CTEs** para la consolidación de inventario físico y ventas transaccionales.
* **Inteligencia de Datos:** El sistema aplica una lógica de **proporcionalidad sobre el stock inicial** para disparar estados de criticidad (`URGENTE`, `ALERTA`, `SUFICIENTE`).
* *Archivo:* `01- optimizacion_inventario.sql`

### 02 - Puente de Datos SQL (CSV)
* **Interoperabilidad:** Exportación de los datos saneados desde el motor SQL para su procesamiento en la capa analítica de Python.
* *Archivo:* `02_Logica_Inventario_SQL.csv`

### 03 - Automatización y ETL (Python)
* **Procesamiento:** Script de transformación que ingiere el CSV de SQL y aplica reglas de limpieza para asegurar la integridad de los cálculos de stock remanente.
* **Estandarización:** Formateo automático del dataset para garantizar compatibilidad con herramientas de BI.
* *Archivo:* `03- optimizacion_inventario.py`

### 04 - Dataset de Salida (CSV Final)
* **Single Source of Truth:** Producto final del proceso ETL. Es un archivo normalizado, depurado y listo para ser consumido por gerencia.
* *Archivo:* `04- inventario_final.csv`

### 05 - Business Intelligence y Toma de Decisiones (Tableau)
* **Funcionalidad:** Dashboard interactivo que resalta visualmente los productos con mayor riesgo de quiebre.
* **UX/UI:** Implementación de tooltips personalizados y filtros por estado de criticidad para agilizar la respuesta operativa.
* *Visualización:* [**Acceder al Dashboard Interactivo aquí**](https://public.tableau.com/app/profile/numa.cacho/viz/Libro1_17752683792050/Dashboard1)

---

## 🛠️ Stack Tecnológico
* **SQL:** Modelado de datos y lógica transaccional.
* **Python (Pandas):** Automatización de procesos y transformación de datos (ETL).
* **Tableau:** Inteligencia de negocios y visualización estratégica.

---
*Este proyecto refleja una competencia sólida en el manejo del ciclo de vida del dato, desde su almacenamiento en crudo hasta su transformación en una herramienta de decisión empresarial.*