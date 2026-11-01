# ==========================================
# SCRIPT DE POBLACIÓN DE DATOS (DRAFT)
# ==========================================

# 1. GENERACIÓN DE DATOS BASE (CARPETA /data)
# - Importar la librería 'Faker' de Python para generar datos ficticios.
# - Crear listas predefinidas de ciudades (ej. GDL, MTY, CDMX) y amenidades.
# - Generar un diccionario en memoria con 500 usuarios base usando Faker (nombres, emails).

# 2. POBLADO DE MONGODB (Catálogos y Transacciones Activas)
# - Conectar a la instancia de MongoDB local.
# - Colección 'hotels': Insertar 100 hoteles generados aleatoriamente con Faker.
# - Colección 'flights': Insertar 300 vuelos variando rutas, fechas y escalas.
# - Colección 'destinations': Insertar 50 destinos con palabras clave en la descripción.
# - Colección 'reservations': Generar 500 reservaciones futuras vinculando los usuarios falsos con los catálogos.

# 3. POBLADO DE CASSANDRA (Registro Histórico)
# - Conectar al cluster local de Cassandra.
# - Tabla de búsquedas: Generar 2,000 registros de búsquedas pasadas usando fechas aleatorias del último año.
# - Tabla de viajes: Insertar 1,000 registros históricos de viajes completados y cancelados.

# 4. POBLADO DE DGRAPH (Motor de Recomendaciones)
# - Conectar al cliente de Dgraph local.
# - Crear nodos basados en los 500 usuarios y los 50 destinos previamente generados.
# - Generar mutaciones para crear aristas (relaciones) aleatorias como 'VISITED' o 'FRIENDS_WITH' para asegurar conexiones de 2do y 3er grado.