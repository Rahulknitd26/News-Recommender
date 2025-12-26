# engine.py
import requests
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Load a pre-trained model for creating embeddings
model = SentenceTransformer('all-MiniLM-L6-v2')

def fetch_articles(api_key, keywords):
    """Fetches news articles from NewsAPI."""
    url = f"https://newsapi.org/v2/everything?q={' OR '.join(keywords)}&apiKey={api_key}&language=en"
    response = requests.get(url)
    data = response.json()
    
    articles = []
    if data['status'] == 'ok':
        for article in data['articles']:
            if article['title'] and article['description']:
                articles.append({
                    'title': article['title'],
                    'description': article['description'],
                    'url': article['url']
                })
    return articles

def create_embeddings(articles):
    """Converts article descriptions into vector embeddings."""
    descriptions = [article['description'] for article in articles]
    embeddings = model.encode(descriptions, convert_to_tensor=False)
    return embeddings


if __name__ == '__main__':
    NEWS_API_KEY = "59e3f6223a2c4b90ac9dad2baa84849e" 
    
    topics = ['artificial intelligence', 'cloud computing', 'python programming', 'space exploration']
    
    print("1. Fetching news articles...")
    articles = fetch_articles(NEWS_API_KEY, topics)
    
    if not articles:
        print("Could not fetch articles. Check your API key or network.")
    else:
        print(f"   - Found {len(articles)} articles.")
        
        print("2. Creating embeddings for each article...")
        article_embeddings = create_embeddings(articles)
        
        print(f"   - Created {len(article_embeddings)} embeddings.")
        print("✅ Processing complete!")
        
        
   
def create_vector_index(embeddings):
    """Creates a FAISS index for fast searching."""
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings))
    return index

def recommend_and_explain(user_interests, articles, article_embeddings, index):
    """Recommends articles and explains why."""
    interest_embedding = model.encode(list(user_interests.keys()))
    
    recommendations = []
    
    k = 25 
    distances, indices = index.search(np.array(interest_embedding), k)

    for i, article_index in enumerate(indices[0]):
        article_vec = article_embeddings[article_index].reshape(1, -1)
        
        sims = model.similarity(article_vec, interest_embedding)
        
        best_match_index = np.argmax(sims)
        reason = list(user_interests.keys())[best_match_index]

        recommendations.append({
            'article': articles[article_index],
            'reason': reason
        })
        
    return recommendations

if __name__ == '__main__':
    
    print("1. Fetching news articles...")
    articles = fetch_articles(NEWS_API_KEY, topics)
    
    if not articles:
        print("Could not fetch articles. Check your API key or network.")
    else:
        print(f"   - Found {len(articles)} articles.")
        
        print("2. Creating embeddings for each article...")
        article_embeddings = create_embeddings(articles)
        print(f"   - Created {len(article_embeddings)} embeddings.")
        
        print("3. Creating search index...")
        article_index = create_vector_index(article_embeddings)
        print("   - Index created.")

        user_interests = {
            "AI model advancements": 0.9,
            "Serverless computing on AWS": 0.8
        }
        
        print(f"4. Recommending articles for user with interests: {list(user_interests.keys())}")
        recommendations = recommend_and_explain(user_interests, articles, article_embeddings, article_index)
        
        print("\n--- Your Personalized News Feed ---")
        for rec in recommendations:
            print(f"📰 Title: {rec['article']['title']}")
            print(f"   Reason: Recommended because you're interested in '{rec['reason']}'.")
            print(f"   Link: {rec['article']['url']}\n")
