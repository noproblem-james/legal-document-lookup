from dotenv import load_dotenv
import os

from elasticsearch import Elasticsearch


load_dotenv()

def connect_to_elasticsearch():
    # Retrieve credentials from environment variables
    es_host = os.getenv("ES_HOST", "https://localhost:9200")
    es_user = os.getenv("ES_USER", "elastic")
    es_password = os.getenv("ES_PASSWORD")
    print(es_password)

    if not es_password:
        raise ValueError("Elasticsearch password not found in environment variables")

    # Initialize the Elasticsearch client

    es = Elasticsearch(
        es_host,
        basic_auth=(es_user, es_password),
        verify_certs=False,
    )


    # Check connection
    if es.ping():
        print("Connected to Elasticsearch successfully!")
    else:
        raise ConnectionError("Failed to connect to Elasticsearch")

    return es

if __name__ == '__main__':
    connect_to_elasticsearch()
