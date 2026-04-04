/* PROYECTO 03: Normalización de Datos y Análisis de Margen Retail
OBJETIVO: Saneamiento de una base de datos transaccional con inconsistencias 
críticas en formatos de fecha, moneda y geografía para habilitar el análisis de rentabilidad.
*/

CREATE TABLE Ventas_Retail_Bruto (
    ID_Transaccion INT PRIMARY KEY,
    Producto_Descripcion VARCHAR(100),
    Fecha_Registro VARCHAR(50),
    Precio_Unitario_Sucio VARCHAR(20),
    Costo_Unitario DECIMAL(10,2),
    Cantidad_Vendida INT,
    Punto_Venta_Ciudad VARCHAR(50)
);

INSERT INTO Ventas_Retail_Bruto VALUES 
(1, '  televisor 4k  ', '2026/03/20', '$500.00', 350.00, 10, 'Buenos Aires'),
(2, 'TELEVISOR 4K', '20-03-2026', '500', 350.00, 5, 'bs as'),
(3, 'Smartphone Pro ', NULL, '$1200', 800.00, 3, 'BARILOCHE'),
(4, 'smartphone pro', '2026-03-21', '1200.00', 800.00, 8, 'Bariloche'),
(5, ' Auriculares BT', '2026-03-22', '$80.00', 30.00, 25, 'CABA');

WITH Datos_Normalizados AS (
    SELECT 
        ID_Transaccion,
        UPPER(TRIM(Producto_Descripcion)) AS Producto,
        COALESCE(Fecha_Registro, '2026-01-01') AS Fecha_Normalizada,
        CAST(REPLACE(Precio_Unitario_Sucio, '$', '') AS DECIMAL(10,2)) AS Precio_Final,
        Costo_Unitario,
        Cantidad_Vendida,
        CASE 
            WHEN UPPER(Punto_Venta_Ciudad) IN ('BUENOS AIRES', 'BS AS', 'CABA') THEN 'Buenos Aires'
            WHEN UPPER(Punto_Venta_Ciudad) = 'BARILOCHE' THEN 'Bariloche'
            ELSE Punto_Venta_Ciudad 
        END AS Ciudad_Estandar
    FROM Ventas_Retail_Bruto
)
SELECT 
    Producto,
    Ciudad_Estandar,
    SUM(Cantidad_Vendida) AS Volumen_Ventas,
    SUM(Precio_Final * Cantidad_Vendida) AS Ingresos_Totales,
    SUM((Precio_Final - Costo_Unitario) * Cantidad_Vendida) AS Margen_Ganancia_Total
FROM Datos_Normalizados
GROUP BY Producto, Ciudad_Estandar
ORDER BY Margen_Ganancia_Total DESC;