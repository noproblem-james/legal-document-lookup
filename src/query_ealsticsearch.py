
from elasticsearch_connector import connect_to_elasticsearch


def list_documents(es, index_name, size=10):
    query = {
        "query": {
            "match_all": {}
        },
        "size": size
    }

    response = es.search(index=index_name, body=query)
    documents = response['hits']['hits']
    for doc in documents:
        print(f"ID: {doc['_id']}, Source: {doc['_source']}")


def query_elasticsearch(es, query, index_name="legal_documents"):
    response = es.search(index=index_name, query={"match": {"content": query}})
    return response


if __name__ == '__main__':
    es = connect_to_elasticsearch()
    # docs = list_documents(es, "legal_documents")
    response = query_elasticsearch(es, query=)
    
