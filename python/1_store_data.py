from sentence_transformers import SentenceTransformer
import redis
    
sentences = ["I love dogs", "I like cats", "I enjoy birds"]

def get_sentence_embeddings(sentences):
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    embeddings = model.encode(sentences, clean_up_tokenization_spaces=True)
    return embeddings

def add_to_redis(embeddings):
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)
    for i, embedding in enumerate(embeddings):
        # Convert the embedding to float[]
        embedding = [float(x) for x in embedding]
        # Store the embedding in Redis
        r.vset().vadd("mydata", embedding, sentences[i])

if __name__ == "__main__":
    embeddings = get_sentence_embeddings(sentences)
    add_to_redis(embeddings)
    print("Embeddings saved to Redis")