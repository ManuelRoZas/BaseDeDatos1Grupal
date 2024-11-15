Ejercicio 2 - ESTADIAS
Sea el siguiente esquema de BD que modela las estadías de pasajeros en diferentes hoteles.

ESTADIA<dniCliente, codHotel, cantidadHabitaciones, direccionHotel, ciudadHotel,dniGerente, nombreGerente, nombreCliente, ciudadCliente,fechaInicioHospedaje, cantDiasHospedaje, #Habitacion>
con las restricciones:
a. Existe un único gerente por hotel. Un gerente podría gerenciar más de un hotel.
b. Un cliente puede realizar la estadía sobre más de una habitación del hotel en la misma fecha. Para cada habitación puede reservar diferentes cantidades de días.
c. cantidadHabitaciones indica la cantidad de habitaciones existentes en un hotel.
d. El código de hotel (codHotel) es único y no puede repetirse en diferentes ciudades.
e. Un cliente puede realizar reservas en diferentes hoteles para la misma fecha.
f. #Habitacion se puede repetir en distintos hoteles.
g. En la misma direccionHotel de una ciudadHotel puede haber más de un hotel funcionando.

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

1. dniCliente -> nombreCliente, ciudadCliente: Un cliente tiene un unico nombre y ciudad

2. codHotel -> direccionHotel, ciudadHotel, cantidadHabitaciones, dniGerente: Un hotel tiene una direccion, ciudad, cantidad de habitaciones y un unico gerente

3. dniGerente -> nombreGerente: Un gerente tiene un unico nombre

4. dniCliente, codHotel, fechaInicioHospedaje, #Habitacion -> cantDiasHospedaje: Un cliente puede realizar estadias en un hotel en una fecha y una cantidad de habitaciones

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Claves candidatas:

1. El cliente (dniCliente), Un cliente puede ser unico por dniCliente
2. El hotel (codHotel), cada hotel tiene un codigo unico
3. La fecha de inicio de la estadia (fechaInicioHospedaje), diferencia entre estadias en distintas fechas, aunque no es unica por si misma
4. La Habitacion (#Habitacion), identifica de manera unica la habitaciones sdentro de un hotel, pero no por si sola, ya que un cliente puede reservar mas de una habitacion

5. ESTADIA (dniCliente, codHotel, fechaInicioHospedaje, #Habitacion), esta combinacion es la que realmente identifica una estadia

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

3FN

1. TABLA CLIENTE (
   dniCliente (PK),
   nombreCliente,
   ciudadCliente
   )

2. TABLA HOTEL (
   codHotel (PK),
   direccionHotel,
   ciudadHotel,
   cantidadHabitaciones,
   dniGerente (FK, referencia a GERENTE)
   )

3. TABLA GERENTE (
   dniGerente (PK),
   nombreGerente
   )

4. TABLA ESTADIA (
   dniCliente (FK, referencia a CLIENTE),
   codHotel (FK, referencia a HOTEL),
   fechaInicioHospedaje,
   #Habitacion,
   cantDiasHospedaje,
   **Clave primaria compuesta:** (dniCliente, codHotel, fechaInicioHospedaje, #Habitacion)
   )
