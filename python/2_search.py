from sentence_transformers import SentenceTransformer
import redis
    
sentences = ["I love dogs", "I like cats", "I enjoy birds"]

def get_sentence_embeddings(sentences):
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    embeddings = model.encode(sentences, clean_up_tokenization_spaces=True)
    return embeddings

def search_redis(query):
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)
    # Get the embedding for the query
    query_embedding = get_sentence_embeddings([query])[0]
    # Convert the query embedding to float[]
    query_embedding = [float(x) for x in query_embedding]
    # Search for the query in Redis
    results = r.vset().vsim("mydata", query_embedding, with_scores=True)
    return results

if __name__ == "__main__":

    query = "I love"
    results = search_redis(query)
    print("Search results:", results)