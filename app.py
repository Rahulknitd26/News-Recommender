# app.py
from flask import Flask, render_template
from engine import fetch_articles, create_embeddings, create_vector_index, recommend_and_explain

app = Flask(__name__)

print("Loading news engine...")
NEWS_API_KEY = "59e3f6223a2c4b90ac9dad2baa84849e" 
topics = ['artificial intelligence', 'cloud computing', 'python programming', 'generative ai']
articles = fetch_articles(NEWS_API_KEY, topics)
article_embeddings = create_embeddings(articles)
article_index = create_vector_index(article_embeddings)
print("Engine loaded. Server is ready.")

@app.route('/')
def home():
    user_interests = {
        "Latest developments in generative AI": 0.9,
        "Cloud infrastructure and deployment": 0.8
    }
    
    recommendations = recommend_and_explain(user_interests, articles, article_embeddings, article_index)
    
    return render_template('index.html', recommendations=recommendations, interests=user_interests.keys())

