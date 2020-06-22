from elasticsearch import Elasticsearch
from configapp.settings import (
    ELASTICSEARCH_INDEX,
    ELASTICSEARCH_HOSTS
    )

es = Elasticsearch(
    hosts=ELASTICSEARCH_HOSTS
)


def update(docs):
    for doc in docs:
        serviceID = int(doc["serviceID"])
        es.indices.create(index=ELASTICSEARCH_INDEX, ignore=400)
        res = es.index(index=ELASTICSEARCH_INDEX, doc_type='TRX_CONFS', id=serviceID, body=doc)
        print(res)
