-- Tabla Pacientes
CREATE TABLE Pacientes (
    NumeroSeguroSocial VARCHAR(20) PRIMARY KEY,
    Nombre VARCHAR(50) NOT NULL,
    Apellido VARCHAR(50) NOT NULL,
    Dirección VARCHAR(100),
    Teléfono VARCHAR(15),
    FechaNacimiento DATE
);

-- Tabla Medicos
CREATE TABLE Medicos (
    NumeroMatricula VARCHAR(20) PRIMARY KEY,
    Nombre VARCHAR(50) NOT NULL,
    Apellido VARCHAR(50) NOT NULL,
    Especialidad VARCHAR(50),
    Teléfono VARCHAR(15)
);

-- Tabla Turnos
CREATE TABLE Turnos (
    Fecha DATE NOT NULL,
    Hora TIME NOT NULL,
    NumeroSeguroSocial VARCHAR(20) NOT NULL,
    NumeroMatricula VARCHAR(20) NOT NULL,
    PRIMARY KEY (Fecha, Hora, NumeroSeguroSocial, NumeroMatricula),
    FOREIGN KEY (NumeroSeguroSocial) REFERENCES Pacientes(NumeroSeguroSocial),
    FOREIGN KEY (NumeroMatricula) REFERENCES Medicos(NumeroMatricula)
);

INSERT INTO Pacientes (NumeroSeguroSocial, Nombre, Apellido, Dirección, Teléfono, FechaNacimiento)
VALUES
('123-45-6789', 'Juan', 'Pérez', 'Calle Falsa 123', '555-1234', '1990-05-10'),
('987-65-4321', 'María', 'Gómez', 'Avenida Siempreviva 456', '555-5678', '1985-12-22'),
('456-78-9123', 'Carlos', 'López', 'Boulevard Central 789', '555-9012', '1978-03-15');

INSERT INTO Medicos (NumeroMatricula, Nombre, Apellido, Especialidad, Teléfono)
VALUES
('MED-001', 'Laura', 'Fernández', 'Cardiología', '555-2345'),
('MED-002', 'Miguel', 'Torres', 'Pediatría', '555-6789'),
('MED-003', 'Ana', 'Martínez', 'Dermatología', '555-3456');

INSERT INTO Turnos (Fecha, Hora, NumeroSeguroSocial, NumeroMatricula)
VALUES
('2024-11-21', '09:00:00', '123-45-6789', 'MED-001'),
('2024-11-21', '10:30:00', '987-65-4321', 'MED-002'),
('2024-11-21', '11:00:00', '456-78-9123', 'MED-003'),
('2024-11-22', '08:00:00', '123-45-6789', 'MED-003'),
('2024-11-22', '09:30:00', '987-65-4321', 'MED-001');


SELECT
    Pacientes.Nombre AS PacienteNombre,
    Pacientes.Apellido AS PacienteApellido,
    Medicos.Nombre AS MedicoNombre,
    Medicos.Apellido AS MedicoApellido,
    Turnos.Fecha,
    Turnos.Hora
FROM
    Turnos
INNER JOIN Pacientes ON Turnos.NumeroSeguroSocial = Pacientes.NumeroSeguroSocial
INNER JOIN Medicos ON Turnos.NumeroMatricula = Medicos.NumeroMatricula
ORDER BY
    Turnos.Fecha, Turnos.Hora;
------------------------
SELECT
    Pacientes.Nombre AS PacienteNombre,
    Pacientes.Apellido AS PacienteApellido,
    Medicos.Nombre AS MedicoNombre,
    Medicos.Apellido AS MedicoApellido,
    Turnos.Fecha,
    Turnos.Hora
FROM
    Pacientes
LEFT JOIN Turnos ON Pacientes.NumeroSeguroSocial = Turnos.NumeroSeguroSocial
LEFT JOIN Medicos ON Turnos.NumeroMatricula = Medicos.NumeroMatricula
ORDER BY
    Pacientes.Apellido, Pacientes.Nombre;
------------------------
SELECT
    Pacientes.Nombre AS PacienteNombre,
    Pacientes.Apellido AS PacienteApellido,
    Medicos.Nombre AS MedicoNombre,
    Medicos.Apellido AS MedicoApellido,
    Turnos.Fecha,
    Turnos.Hora
FROM
    Turnos
RIGHT JOIN Pacientes ON Turnos.NumeroSeguroSocial = Pacientes.NumeroSeguroSocial
RIGHT JOIN Medicos ON Turnos.NumeroMatricula = Medicos.NumeroMatricula
ORDER BY
    Turnos.Fecha, Turnos.Hora;
------------------------
SELECT
    Medicos.Nombre AS MedicoNombre,
    Medicos.Apellido AS MedicoApellido,
    COUNT(Turnos.Fecha) AS TotalTurnos
FROM
    Medicos
LEFT JOIN Turnos ON Medicos.NumeroMatricula = Turnos.NumeroMatricula
GROUP BY
    Medicos.NumeroMatricula
HAVING
    COUNT(Turnos.Fecha) > 0
ORDER BY
    TotalTurnos DESC;
------------------------
SELECT
    Pacientes.Nombre AS PacienteNombre,
    Pacientes.Apellido AS PacienteApellido,
    COUNT(Turnos.Fecha) AS TotalTurnos
FROM
    Pacientes
LEFT JOIN Turnos ON Pacientes.NumeroSeguroSocial = Turnos.NumeroSeguroSocial
GROUP BY
    Pacientes.NumeroSeguroSocial
HAVING
    COUNT(Turnos.Fecha) > 1
ORDER BY
    TotalTurnos ASC;
------------------------
SELECT
    Pacientes.Nombre AS PacienteNombre,
    Pacientes.Apellido AS PacienteApellido,
    COUNT(Turnos.Fecha) AS TotalTurnos
FROM
    Pacientes
INNER JOIN Turnos ON Pacientes.NumeroSeguroSocial = Turnos.NumeroSeguroSocial
GROUP BY
    Pacientes.NumeroSeguroSocial
ORDER BY
    TotalTurnos DESC;
------------------------




