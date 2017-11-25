import json
import elasticsearch
from elasticsearch_dsl import Search, Q
from elasticsearch_dsl.query import Match, MultiMatch

es = elasticsearch.Elasticsearch()
INDEX = "bd_avance"
DOC_TYPE = "emails"


def get_data(fname):
    with open(fname) as fhandle:
        for line in fhandle:
            data = json.loads(line, encoding='utf-8')
            data["id"] = data["_id"]["$oid"]  # Remapping the id for ES
            del data['_id']
            yield data


# Exercice 1.1
def search_natural_gas_summit():
    # TODO
    pass


# Exercice 1.2
def search_natural_gas_summit_v2():
    # TODO
    pass


# Exercice 1.3
def search_meetings_in_houston():
    # TODO
    pass


# Exercice 1.4
def boosted_search():
    # TODO
    pass

# Exercice 2.1
def cross_fields():
    # TODO
    pass


# Exercice 3.1
def proximity():
    # TODO
    pass


# Exercice 5.1
def query_for_2000():
    # TODO
    pass


# Exercice 6.1
def synonymes():
    # TODO
    pass


if __name__ == '__main__':
    # TODO
    pass
