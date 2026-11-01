# Plataforma de Reservaciones de Viajes - Masa Madre

## Integrantes del Equipo
* Oswaldo Oseguera Sandoval - 758479
* André Rodrigo Álvarez Flores - 757821
* Neguib Zayed Beltran Zuno - 755217

## Descripción del Proyecto
Plataforma que unifica la búsqueda, gestión y recomendación de viajes (vuelos y hoteles). Utiliza una arquitectura políglota para optimizar diferentes procesos:
* **MongoDB:** Núcleo transaccional para catálogos y reservaciones activas.
* **Cassandra:** Registro histórico inmutable de alta disponibilidad.
* **Dgraph:** Motor de recomendaciones basado en grafos para descubrir conexiones entre viajeros y destinos.

## Flujo de Trabajo (Draft Inicial)
1. Levantar los contenedores de las bases de datos (MongoDB, Cassandra, Dgraph) localmente.
2. Ejecutar `python populate.py` para generar e insertar los datos de prueba (usando Faker/JSON) en las tres bases de datos.
3. Ejecutar `python main.py` para desplegar el menú interactivo y realizar las consultas a la base de datos correspondiente.