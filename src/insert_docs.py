# insert_docs.py

import os
from elasticsearch import Elasticsearch, helpers
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def connect_to_elasticsearch():
    es_host = os.getenv("ES_HOST", "https://localhost:9200")
    es_user = os.getenv("ES_USER", "elastic")
    es_password = os.getenv("ES_PASSWORD")

    if not es_password:
        raise ValueError("Elasticsearch password not found in environment variables")

    es = Elasticsearch(
        es_host,
        http_auth=(es_user, es_password),
        verify_certs=False,
    )

    if es.ping():
        print("Connected to Elasticsearch successfully!")
    else:
        raise ConnectionError("Failed to connect to Elasticsearch")

    return es

def index_documents(es, index_name, docs):
    actions = [
        {
            "_index": index_name,
            "_source": doc,
        }
        for doc in docs
    ]
    helpers.bulk(es, actions)
    print(f"Indexed {len(docs)} documents into {index_name}")

if __name__ == "__main__":
    es = connect_to_elasticsearch()

    # Dummy document for Brown v. Board of Education
    brown_v_board_document = {
        "title": "Brown v. Board of Education",
        "content": (
            "Brown v. Board of Education of Topeka was a landmark 1954 Supreme Court case "
            "in which the justices ruled unanimously that racial segregation of children in public schools "
            "was unconstitutional. The case was brought by Oliver Brown, whose daughter Linda Brown was denied entry "
            "to an all-white elementary school. The decision overturned the Plessy v. Ferguson decision of 1896, "
            "which allowed state-sponsored segregation."
        )
    }

    # Insert the document
    documents = [brown_v_board_document]
    index_documents(es, "legal_documents", documents)
