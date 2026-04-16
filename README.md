# Strategic Data Analytics Portfolio: Laboratorio de Arquitectura y Pruebas de Concepto (PoC)

Bienvenido a mi repositorio central. Este espacio funciona como un **Laboratorio de Datos** donde diseño y valido Pruebas de Concepto (PoC) orientadas a resolver problemas críticos en las áreas Comercial, Operativa y Financiera.

El objetivo de este repositorio no es el procesamiento bruto de Big Data, sino la demostración de **fundamentos arquitectónicos sólidos**. Aquí expongo mi capacidad para estructurar lógica de negocio, diseñar pipelines modulares y traducir requerimientos entre diferentes lenguajes (SQL a Python) en entornos controlados, antes de su escalado a producción.

---

## ⚙️ Metodología: Arquitectura Desacoplada
Para garantizar que estas pruebas de concepto sean escalables en el mundo real, todos los proyectos evitan el acoplamiento rígido y se estructuran en un pipeline modular de **5 Capas**:

1. **Capa de Extracción (SQL):** Interacción directa con motores relacionales para el saneamiento inicial (*Data Wrangling*) y consolidación del esquema.
2. **Capa de Datos Crudos (CSV - Raw):** Exportación de datasets base para aislar la base de datos transaccional del entorno analítico.
3. **Motor de Lógica de Negocio (Python):** Uso de la librería Pandas para procesar en memoria algoritmos complejos, cálculos vectoriales y alertas dinámicas que serían ineficientes en SQL.
4. **Capa de Certificación (CSV - Gold):** Generación de la "Única Fuente de Verdad" (*Single Source of Truth*), un dataset depurado y optimizado.
5. **Capa de Inteligencia Ejecutiva (Tableau):** Despliegue de tableros orientados a la rápida asimilación de KPIs por parte de la gerencia.

---

## 📂 Portafolio de Pruebas de Concepto (PoCs)

### 1. [🛒 PoC: Optimización de Inventario y Alertas Críticas](./01-optimizacion-inventario-retail)
**Foco: Traducción Lógica y Mitigación de Riesgos.** Laboratorio diseñado para validar un sistema de alertas dinámicas basado en la proporcionalidad del stock. Demuestra cómo una regla de negocio (reabastecimiento al 20% de capacidad) puede ser extraída con SQL y vectorizada en Python para mayor escalabilidad.

### 2. [💰 PoC: Análisis de Flujo de Caja y Proyección de Capital](./02-proyeccion-flujo-caja)
**Foco: Ingeniería Financiera y Series Temporales.** Entorno de pruebas que procesa ingresos y egresos para validar el cálculo de ahorro acumulado (*Running Totals*). El modelo determina matemáticamente el horizonte temporal exacto para el cumplimiento de una meta de capitalización estratégica.

### 3. [📊 PoC: Saneamiento de Datos y Auditoría de Rentabilidad](./03-saneamiento-datos-rentabilidad)
**Foco: Data Quality y Análisis de ROI.** Simulación orientada a resolver la "Entropía de Datos" en sistemas manuales. El pipeline valida técnicas de normalización extrema (limpieza de monedas, estandarización geográfica y nulos) para luego inyectar esos datos en un motor Python que audita el margen neto y el ROI.

---

## 🛠️ Stack Tecnológico
* **SQL:** Modelado, CTEs, Window Functions y normalización de cadenas.
* **Python (Pandas):** Automatización de reglas de negocio y procesamiento escalar.
* **Tableau:** Visualización estratégica y validación visual de los modelos.

---
*Como analista, utilizo estos entornos de laboratorio para garantizar que la lógica matemática y estructural sea perfecta antes de comprometer los recursos y servidores de una operación a gran escala.*