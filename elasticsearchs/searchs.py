
from elasticsearch import Elasticsearch

# tot
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
def multi_match(fields, tex):
    es = Elasticsearch()
    #Search as you type
    res = es.search(index="newpapers", 
                    doc_type="post", 
                    body={"query": {"multi_match": {"query": tex, "fields": fields}}},
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

# must: giao các kết quả, should: hợp các tập kết quả
def boolean_search_must(field, texs):
    
    texs = texs.split()
    
    must=[]
    for tex in texs:
        rule={"match": {field: tex}}
        must.append(rule)
    
    es = Elasticsearch()
    #Search as you type
    res = es.search(index="newpapers", 
                    doc_type="post", 
                    # max edit distance
                    body={"query":{"bool":{"must": must}}},
                    size=20)
    
    results=[]
    for post in res['hits']['hits']:
        result = post['_source']
        results.append(result)
    
    return res['took'], res['hits']['total'],results
def boolean_search_should(field, texs):
    
    texs = texs.split()
    
    should=[]
    for tex in texs:
        rule={"match": {field: tex}}
        should.append(rule)
    
    es = Elasticsearch()
    #Search as you type
    res = es.search(index="newpapers", 
                    doc_type="post", 
                    # max edit distance
                    body={"query":{"bool":{"should": should}}},
                    size=20)
    
    results=[]
    for post in res['hits']['hits']:
        result = post['_source']
        results.append(result)
    
    return res['took'], res['hits']['total'],results