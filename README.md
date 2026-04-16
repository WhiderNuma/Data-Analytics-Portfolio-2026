# Strategic Data Analytics Portfolio: End-to-End Business Solutions

Bienvenido a mi repositorio central de ingeniería y análisis de datos. Este espacio compendia soluciones integrales diseñadas para transformar datos transaccionales crudos en activos estratégicos. Cada proyecto aquí contenido aborda una problemática crítica de negocio en las áreas **Comercial, Operativa o Financiera**, utilizando un enfoque de "Socio Estratégico".

---

## ⚙️ Metodología y Arquitectura de Datos
Para garantizar la integridad, trazabilidad y escalabilidad de las soluciones, todos los proyectos se rigen bajo una arquitectura de **Pipeline Desacoplado en 5 Capas**:

1. **Capa de Extracción y Normalización (SQL):** Interacción directa con motores relacionales para el saneamiento inicial (*Data Wrangling*) y estructuración de esquemas.
2. **Capa de Datos Crudos (CSV - Raw):** Exportación de datasets saneados que actúan como punto de control de integridad.
3. **Capa de Transformación y Lógica de Negocio (Python):** Uso de la librería Pandas para la aplicación de algoritmos complejos, cálculos vectoriales y lógica de negocio dinámica.
4. **Capa de Certificación (CSV - Gold):** Generación de la "Única Fuente de Verdad" (*Single Source of Truth*), un dataset depurado y optimizado.
5. **Capa de Inteligencia Ejecutiva (Tableau):** Despliegue de dashboards interactivos orientados a reducir el tiempo de toma de decisiones gerenciales.

---

## 📂 Portafolio de Proyectos

### 1. [🛒 Optimización de Inventario y Alertas Críticas](https://github.com/WhiderNuma/portfolio-analisis-datos-estrategico/tree/main/01-optimizacion-inventario-retail)
**Foco: Eficiencia Operativa y Mitigación de Riesgos.** Desarrollo de un sistema de alertas dinámicas basado en proporcionalidad de stock. Sustituye los umbrales estáticos por un motor de reglas en Python que detecta riesgos de quiebre de stock en tiempo real, optimizando el ciclo de reabastecimiento.

### 2. [💰 Análisis de Flujo de Caja y Proyección de Capital](https://github.com/WhiderNuma/portfolio-analisis-datos-estrategico/tree/main/02-proyeccion-flujo-caja)
**Foco: Ingeniería Financiera y Solvencia.** Modelo de monitoreo financiero que procesa ingresos y egresos para proyectar el ahorro acumulado (*Running Totals*). Determina el horizonte temporal de solvencia y el cumplimiento de metas de capitalización estratégica mediante análisis de series temporales.

### 3. [📊 Saneamiento de Datos y Auditoría de Rentabilidad](https://github.com/WhiderNuma/portfolio-analisis-datos-estrategico/tree/main/03-saneamiento-datos-rentabilidad)
**Foco: Calidad de Datos y Análisis de ROI.** Solución orientada a resolver la "Entropía de Datos" en sistemas transaccionales. Normaliza inconsistencias críticas (monedas, geografía, nulos) para ejecutar una auditoría de rentabilidad precisa, calculando el ROI y margen neto por unidad de negocio.

---

## 🛠️ Stack Tecnológico
* **SQL:** Modelado, CTEs, Window Functions y normalización.
* **Python (Pandas):** Automatización de ETL, lógica de negocio y procesamiento escalar.
* **Tableau:** Visualización estratégica y dashboards ejecutivos de alto impacto.

---
*Como analista especializado en soluciones estratégicas, mi enfoque combina el rigor técnico de la ingeniería de datos con una visión clara del impacto financiero y operativo de cada decisión.*