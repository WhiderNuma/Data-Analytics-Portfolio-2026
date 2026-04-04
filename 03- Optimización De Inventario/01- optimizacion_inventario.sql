/* PROYECTO: Optimización de Inventario y Alertas de Reabastecimiento
OBJETIVO: Monitorear el nivel de stock cruzando el inventario físico con 
el volumen de ventas para disparar alertas automáticas de compra.
*/

CREATE TABLE Stock (
    Producto_ID INT PRIMARY KEY,
    Nombre_Producto VARCHAR(50),
    Stock_Inicial INT
);

INSERT INTO Stock VALUES 
(101, 'Smartphone X', 100),
(102, 'Laptop Gaming', 50),
(103, 'Auriculares BT', 200),
(104, 'Monitor 4K', 30);

CREATE TABLE Ventas (
    Venta_ID INT PRIMARY KEY,
    Producto_ID INT,
    Cantidad_Vendida INT,
    Fecha_Venta DATE,
    FOREIGN KEY (Producto_ID) REFERENCES Stock(Producto_ID)
);

INSERT INTO Ventas VALUES 
(1, 101, 20, '2026-03-01'),
(2, 101, 65, '2026-03-15'), 
(3, 102, 35, '2026-03-10'), 
(4, 103, 120, '2026-03-20'), 
(5, 104, 5, '2026-03-22');   

WITH Ventas_Agrupadas AS (
    SELECT 
        Producto_ID, 
        SUM(Cantidad_Vendida) AS Total_Vendido_Mes
    FROM Ventas
    GROUP BY Producto_ID
)
SELECT 
    s.Nombre_Producto,
    s.Stock_Inicial,
    COALESCE(v.Total_Vendido_Mes, 0) AS Ventas_Mes,
    (s.Stock_Inicial - COALESCE(v.Total_Vendido_Mes, 0)) AS Stock_Remanente,
    CASE 
        WHEN (s.Stock_Inicial - COALESCE(v.Total_Vendido_Mes, 0)) <= (s.Stock_Inicial * 0.2) 
            THEN '🔴 URGENTE: REABASTECER'
        WHEN (s.Stock_Inicial - COALESCE(v.Total_Vendido_Mes, 0)) <= (s.Stock_Inicial * 0.4) 
            THEN '🟡 ALERTA: STOCK BAJO'
        ELSE '🟢 STOCK SUFICIENTE'
    END AS Estado_