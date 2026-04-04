# 📊 Optimización de Inventario y Alertas Críticas (Retail)

> **Nota de Portafolio:** Este proyecto es una versión funcional y anonimizada de los flujos de trabajo que implemento para clientes reales. El objetivo es demostrar la arquitectura técnica y la lógica de negocio aplicada a la gestión de activos y mitigación de riesgos operativos.

## 🎯 Objetivo del Proyecto
El cliente presentaba ineficiencias en la cadena de suministro y pérdidas económicas por quiebres de stock no detectados. Se diseñó un **pipeline de datos** que automatiza la monitorización de niveles de inventario, permitiendo al departamento de compras ejecutar reposiciones proactivas mediante un sistema de alertas dinámicas.

---

## 🏗️ Arquitectura de la Solución
La solución se estructura en 4 fases técnicas integradas que garantizan la trazabilidad y veracidad de la información:

### 01 - Extracción y Modelado (SQL)
Fase de interacción con el motor de base de datos relacional.
* **Lógica de Negocio:** Implementación de consultas avanzadas mediante **CTEs** para la consolidación de inventario físico y ventas transaccionales.
* **Inteligencia de Datos:** El sistema no utiliza umbrales fijos; aplica una lógica de **proporcionalidad sobre el stock inicial** para disparar estados de criticidad (`URGENTE`, `ALERTA`, `SUFICIENTE`).
* *Archivo:* `01_logica_inventario.sql`

### 03 - Automatización y ETL (Python)
Desarrollo de un script de procesamiento intermedio para asegurar la escalabilidad del reporte.
* **Middleware:** Simulación de extracción de base de datos y aplicación de reglas de limpieza para asegurar la integridad de los cálculos de stock remanente.
* **Estandarización:** Formateo automático del dataset para garantizar compatibilidad regional con herramientas de Business Intelligence (BI).
* *Archivo:* `03_generador_reporte.py`

### 04 - Dataset de Salida (CSV)
Producto final del proceso de transformación (ETL). Es un archivo normalizado, depurado y listo para ser consumido por departamentos financieros o herramientas de visualización.
* *Archivo:* `04_reporte_inventario_final.csv`

### 05 - Business Intelligence y Toma de Decisiones (Tableau)
Capa final de visualización orientada a usuarios finales y gerencia.
* **Funcionalidad:** Dashboard interactivo que resalta visualmente los productos con mayor riesgo de quiebre.
* **UX/UI:** Implementación de tooltips personalizados y filtros por estado de criticidad para agilizar la respuesta operativa.
* *Visualización:* [**Acceder al Dashboard Interactivo aquí**](https://public.tableau.com/app/profile/numa.cacho/viz/Optimizacion_Inventario/Hoja2)

---

## 🛠️ Stack Tecnológico
* **SQL:** Modelado de datos y lógica transaccional.
* **Python (Pandas):** Automatización de procesos y transformación de datos (ETL).
* **Tableau:** Inteligencia de negocios y visualización de datos.

---
*Este proyecto refleja una competencia sólida en el manejo del ciclo de vida del dato, desde su almacenamiento en crudo hasta su transformación en un activo estratégico para la empresa.*