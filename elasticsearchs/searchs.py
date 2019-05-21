
from elasticsearch import Elasticsearch

def match_phrase_prefix(field, tex):
    es = Elasticsearch()
    #Search as you type
    res = es.search(index="newpapers", 
                    doc_type="post", 
                    body={"query": {"match_phrase_prefix": {field: tex }}},
                    size=20)
    
    results=[]
    for post in res['hits']['hits']:
        result = post['_source']
        results.append(result)
    
    return res['took'], res['hits']['total'],results

def match(field, tex):
    es = Elasticsearch()
    #Search as you type
    res = es.search(index="newpapers", 
                    doc_type="post", 
                    body={"query": {"match": {field: tex }}},
                    size=20)
    
    results=[]
    for post in res['hits']['hits']:
        result = post['_source']
        results.append(result)
    
    return res['took'], res['hits']['total'],results
def fuzzy_search(field, tex):
    es = Elasticsearch()
    #Search as you type
    res = es.search(index="newpapers", 
                    doc_type="post", 
                    # max edit distance
                    body={"query":{"match":{field: {"query": tex, "fuzziness":"1" }  }}},
                    size=20)
    
    results=[]
    for post in res['hits']['hits']:
        result = post['_source']
        results.append(result)
    
    return res['took'], res['hits']['total'],results