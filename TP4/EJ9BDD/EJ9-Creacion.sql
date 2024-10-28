    CREATE TABLE Pedidos (
        PedidoId INTEGER PRIMARY KEY AUTOINCREMENT,
        ClienteId INT NOT NULL,
        FechaPedido DATE NOT NULL,
        TotalPedido DECIMAL(10,2) NOT NULL,
        Facturado BOOLEAN DEFAULT 0
    );

    CREATE TABLE Facturas (
        FacturaId INTEGER PRIMARY KEY AUTOINCREMENT,
        PedidoId INT,
        FechaFactura DATE NOT NULL,
        MontoFacturado DECIMAL(10,2) NOT NULL,
        FOREIGN KEY (PedidoId) REFERENCES Pedidos(PedidoId)
    );