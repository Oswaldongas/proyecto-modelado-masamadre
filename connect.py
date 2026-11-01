import os
import logging
from pymongo import MongoClient
from cassandra.cluster import Cluster
import pydgraph

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_mongo_database():
    """
    Establece la conexión a MongoDB.
    Basado en la configuración local del puerto 27017.
    """
    try:
        client = MongoClient('mongodb://localhost:27017/')
        # Seleccionamos la base de datos para el proyecto
        db = client.viajes_masamadre 
        logger.info("Conexión a MongoDB exitosa.")
        return db
    except Exception as e:
        logger.error(f"Error conectando a MongoDB: {e}")
        return None

def get_cassandra_session():
    """
    Establece la conexión al clúster de Cassandra.
    Utiliza 127.0.0.1 por defecto o la variable de entorno.
    """
    try:
        cluster_ips = os.getenv('CASSANDRA_CLUSTER_IPS', '127.0.0.1')
        cluster = Cluster(cluster_ips.split(','))
        session = cluster.connect()
        logger.info(f"Conexión a Cassandra exitosa en {cluster_ips}.")
        return session
    except Exception as e:
        logger.error(f"Error conectando a Cassandra: {e}")
        return None

def get_dgraph_client():
    """
    Establece la conexión estándar a Dgraph local.
    Requiere instalar: pip install pydgraph
    """
    try:
        client_stub = pydgraph.DgraphClientStub('localhost:9080')
        client = pydgraph.DgraphClient(client_stub)
        logger.info("Conexión a Dgraph exitosa en localhost:9080.")
        return client
    except Exception as e:
        logger.error(f"Error conectando a Dgraph: {e}")
        return None

if __name__ == "__main__":
    # Prueba rápida de conexiones al ejecutar el script directamente
    print("Probando conexiones a las bases de datos...\n")
    
    mongo_db = get_mongo_database()
    cassandra_session = get_cassandra_session()
    dgraph_client = get_dgraph_client()

    print("\nEstado de las conexiones:")
    print(f"MongoDB: {'OK' if mongo_db is not None else 'FALLÓ'}")
    print(f"Cassandra: {'OK' if cassandra_session is not None else 'FALLÓ'}")
    print(f"Dgraph: {'OK' if dgraph_client is not None else 'FALLÓ'}")