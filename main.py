def print_menu():
    print("=== PLATAFORMA DE VIAJES: MASA MADRE ===")
    
    print("\n--- Consultas MongoDB (Catálogos y Transacciones) ---")
    print("1. Consulta de itinerario completo")
    print("2. Búsqueda de Vuelos Directos")
    print("3. Filtrado y Ordenamiento de Hoteles")
    print("4. Consulta por Coincidencias en Amenidades")
    print("5. Consulta de Reservaciones Activas")
    print("6. Búsqueda de Destinos por Palabra Clave")
    print("7. Reporte de Ingresos Mensuales por Destino (Agregación)")
    print("8. Top 5 de Hoteles Más Populares con Promedio de Estancia (Agregación)")
    
    print("\n--- Consultas Cassandra (Historial) ---")
    print("9. Ver las ultimas reservaciones de un usuario")
    print("10. Reservaciones de un usuario por rango de fechas")
    print("11. Búsquedas recientes del usuario")
    print("12. Búsquedas de un usuario en un día")
    print("13. Reservaciones por destino y mes")
    print("14. Búsquedas recientes hacia un destino")
    print("15. Últimos viajes completados de un usuario")
    print("16. Reservaciones canceladas de un usuario")

    print("\n--- Consultas Dgraph (Recomendaciones) ---")
    print("17. Recomendaciones de viajes")
    print("18. Identificación de Influenciadores de Viaje en la Red")
    print("19. Descubrimiento de Conexiones de Rutas y Escalas Populares")
    print("20. Amigos y Compañeros de Viaje en Común")
    print("21. Destinos Cercanos Recomendados por Categoría de Entorno")
    print("22. Camino de Conexión Más Corto entre Dos Viajeros")
    print("23. Destinos en Tendencia por Círculo Social Directo e Indirecto")
    print("24. Detección de Comunidades de Viaje por Estilo y Presupuesto")
    
    print("\n0. Salir")

if __name__ == "__main__":
    while True:
        print_menu()
        opcion = input("\nSelecciona una opción: ")
        if opcion == "0":
            print("Saliendo del sistema...")
            break
        else:
            print(f"La opción {opcion} aún no tiene lógica implementada.\n")