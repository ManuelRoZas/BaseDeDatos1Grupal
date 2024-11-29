Diseño esperado. Identifica entidades fuertes y débiles, atributos, relaciones y cardinalidades.
• Normalización: Debes aplicar las formas normales (1NF, 2NF y 3NF)
para optimizar el diseño de la base de datos y eliminar redundancias.
• Restricciones de Integridad: Define llaves primarias y foráneas. Aplica
restricciones NOT NULL, UNIQUE.
• Operaciones en cascada Define operaciones en cascada convenientes usando ON UPDATE CASCADE, ON DELETE RESTRICT, etc. donde sea necesario
para prevenir errores de consistencia.
• Consultas Avanzadas: Implementa INNER JOIN, LEFT JOIN y RIGHT
JOIN para recuperar datos relacionados. Utiliza cunando sea necesario
funciones agregadas y cláusulas como GROUP BY, HAVING, ORDER BY.

Desarrolla un sistema para gestionar un hospital que incluya pacientes, médicos
y turnos de consulta médica.
• Modelo del Sistema. Representa entidades como Pacientes, Médicos y
Turnos con fecha y horario.
• Datos inciales La base de datos inicial debe contener al menos diez (10)
pacientes y diez (10) médicos. La cantidad promedio de los turnos debe
ser de diez (10) turnos por cada paciente

1. Entidad Fuertes: Pacientes, Médicos, Turnos

2. Entidad Débiles: No hay entidades débiles

3. Atributos:

• Pacientes: Nombre, Apellido, Dirección, Teléfono, Fecha de Nacimiento, Número de Seguro Social
• Medicos: Nombre, Apellido, Especialidad, Número de Matrícula, Teléfono
• Turnos: Fecha, Hora, Paciente, Médico

4. Relaciones:
   • Pacientes: Puede tener muchos turnos
   • Médicos: Puede tener muchos turnos, pacientes
   • Turnos: Relación muchos a uno con Pacientes y Médicos

5. Cardinalidades:
   • Pacientes: Uno a
   • Médicos: Uno a
   • Turnos: Muchos a uno con Pacientes y Médicos

6. Normalización:

• 1NF:
Pacientes:
Todos los atributos son atómicos, ya que cada atributo almacena un solo dato por registro (por ejemplo, el nombre no contiene varios nombres juntos). Además, el Número de Seguro Social identifica de manera única a cada paciente.

Medicos:
Todos los atributos son atómicos, ya que cada atributo almacena un solo dato por registro (por ejemplo, el nombre no contiene varios nombres juntos). Además, el Número de Matrícula identifica de manera única a cada médico.

Turnos:
Todos los atributos son atómicos, ya que cada atributo almacena un solo dato por registro (por ejemplo, la fecha y la hora no contienen varios datos juntos). Además, la combinación de la fecha, hora, número de seguro social y número de matrícula identifica de manera única a cada turno.

• 2NF:
Entidad: Pacientes
Atributos: Nombre, Apellido, Dirección, Teléfono, Fecha de Nacimiento, Número de Seguro Social.
Clave primaria: Número de Seguro Social.
Justificación: Todos los atributos dependen de Numero de Seguro social, por lo que la tabla está en 2NF.

Entidad: Médicos
Atributos: Nombre, Apellido, Especialidad, Número de Matrícula, Teléfono.
Clave primaria: Número de Matrícula
Justificación: Todos los atributos dependen de Numero de matricula, por lo que la tabla está en 2NF.

Entidad: Turnos
Atributos: Fecha, Hora, Paciente, Médico
Clave primaria compuesta: Fecha, Hora, Número de Seguro Social, Número de Matrícula
Fecha y Hora: Son parte de la clave primaria, necesarias para identificar un turno único.
Paciente (Número de Seguro Social): Es parte de la clave primaria y no depende de ninguna otra parte.
Médico (Número de Matrícula): Es parte de la clave primaria y tampoco depende de ninguna otra parte.

• 3NF:
** Tabla Turnos **

- Fecha (Clave primaria compuesta)
- Hora (Clave primaria compuesta)
- NumeroSeguroSocial (Clave foránea que referencia a Pacientes.NumeroSeguroSocial)
- NumeroMatricula (Clave foránea que referencia a Medicos.NumeroMatricula)
- Clave primaria compuesta: (Fecha, Hora, NumeroSeguroSocial, NumeroMatricula)

** Tabla Pacientes **

- NumeroSeguroSocial (Clave primaria)
- Nombre
- Apellido
- Dirección
- Teléfono
- FechaNacimiento
- Clave primaria: NumeroSeguroSocial

** Tabla Medicos **

- NumeroMatricula (Clave primaria)
- Nombre
- Apellido
- Especialidad
- Teléfono
- Clave primaria: NumeroMatricula

7. Restricciones de Integridad:
   • Llaves Primarias:
   • Pacientes: Número de Seguro Social
   • Médicos: Número de Matrícula
   • Turnos
   • Paciente: Número de Seguro Social
   • Médico: Número de Matrícula
   • Llaves Foráneas:
   • Turnos: Número de Seguro Social (Paciente) y Número de Matrícula (Médico)

8. Operaciones en cascada:
   HECHO EN EL SQL
9. Consultas Avanzadas:
   HECHO EN EL SQL
