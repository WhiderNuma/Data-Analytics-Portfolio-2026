# Módulo Analítico: Flujo de Caja y Proyección de Capital (PoC)

Este directorio contiene la implementación técnica de un modelo de viabilidad financiera. El sistema procesa un historial de ingresos y egresos para calcular el flujo de caja neto mensual y proyectar el ahorro acumulado, determinando el horizonte temporal exacto para alcanzar una meta de capitalización estratégica.

## 🎯 Objetivo del Módulo
Transformar registros transaccionales aislados en un modelo de proyección temporal. La solución permite monitorear la salud financiera del proyecto mes a mes y evalúa dinámicamente si la meta de capital ha sido `ALCANZADA` o sigue `EN PROGRESO`.

## 🏗️ Arquitectura Desacoplada
El flujo de datos está estructurado en un pipeline modular de 3 capas, separando la ingesta transaccional del cálculo analítico avanzado.

### 01. Capa de Extracción y Modelado (Base de Datos)
* **Archivo:** `01_extraccion_transacciones.sql`
* **Salida:** `02_dataset_raw.csv`
* **Lógica:** Consultas relacionales para la agregación de categorías de ingresos y egresos a nivel mensual. Actúa como el punto de consolidación del P&L (Profit & Loss) básico.

### 02. Motor de Proyección Financiera (Procesamiento ETL)
* **Archivo:** `03_motor_proyeccion_financiera.py`
* **Salida:** `04_dataset_gold.csv`
* **Lógica:** Script de Python (Pandas) encargado de la lógica matemática compleja. Aplica cálculos de sumas acumuladas (`cumsum()`) para generar la curva de ahorro histórico y cruza el resultado con el threshold de la meta financiera para emitir el estado de viabilidad. 

### 03. Capa de Inteligencia de Negocios (Visualización)
* **Archivo:** `05_dashboard_financiero.twb`
* **Lógica:** Tablero interactivo en Tableau conectado al dataset Gold. Diseñado para ofrecer una visión ejecutiva del "Runway" financiero, mostrando la evolución del capital a lo largo del tiempo hasta cruzar la línea de meta.

## 🛠️ Stack Tecnológico Implementado
* **SQL:** Consolidación de ingresos y egresos.
* **Python (Pandas):** Cálculos de ventana (Running Totals) y evaluación de metas.
* **Tableau:** Inteligencia financiera y visualización de tendencias.

---
*Nota de Arquitectura: La externalización del cálculo de sumas acumuladas a la capa de Python permite que el motor de reglas sea fácilmente adaptable ante cambios en la meta de capital, sin necesidad de reestructurar las consultas a la base de datos transaccional.*