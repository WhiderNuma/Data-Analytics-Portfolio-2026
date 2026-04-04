/* PROYECTO 01: Análisis de Flujo de Caja y Proyección de Ahorro
   OBJETIVO: Trackeo de ingresos/egresos para determinar la viabilidad 
   financiera de un proyecto de relocalización (Mudanza a BA).
*/

CREATE TABLE Flujo_Caja (
    Mes_ID INT,
    Mes_Nombre VARCHAR(20),
    Categoria VARCHAR(50),
    Tipo VARCHAR(10),
    Monto DECIMAL(10,2)
);

INSERT INTO Flujo_Caja VALUES 
(1, '01-Enero', 'Ayuda Familiar', 'Ingreso', 150000),
(2, '02-Febrero', 'Ayuda Familiar', 'Ingreso', 150000),
(3, '03-Marzo', 'Ayuda Familiar', 'Ingreso', 150000),
(4, '04-Abril', 'Sueldo Junior (Est)', 'Ingreso', 800000),
(4, '04-Abril', 'Gastos Fijos', 'Egreso', 250000),
(5, '05-Mayo', 'Sueldo Junior (Est)', 'Ingreso', 800000),
(5, '05-Mayo', 'Gastos Fijos', 'Egreso', 250000),
(6, '06-Junio', 'Sueldo Junior (Est)', 'Ingreso', 850000),
(6, '06-Junio', 'Gastos Fijos', 'Egreso', 280000);

WITH Resumen_Mensual AS (
    SELECT 
        Mes_ID,
        Mes_Nombre,
        SUM(CASE WHEN Tipo = 'Ingreso' THEN Monto ELSE -Monto END) AS Saldo_Neto_Mes
    FROM Flujo_Caja
    GROUP BY Mes_ID, Mes_Nombre
)
SELECT 
    Mes_Nombre,
    Saldo_Neto_Mes,
    SUM(Saldo_Neto_Mes) OVER (ORDER BY Mes_ID) AS Ahorro_Acumulado,
    CASE 
        WHEN SUM(Saldo_Neto_Mes) OVER (ORDER BY Mes_ID) >= 1000000 THEN 'LISTO PARA MUDARSE'
        ELSE 'Sigue Ahorrando'
    END AS Estado_Objetivo
FROM Resumen_Mensual
ORDER BY Mes_ID;