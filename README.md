
AI-Powered News Feed with Explainable Recommendations
This project is a Python-based web application that generates a personalized news feed for a user based on their specified interests. Its key feature is Explainable AI (XAI), where every recommended article is accompanied by a clear, simple reason explaining why it was chosen, making the AI's decision-making process transparent to the user.

Key Features
Personalized Content: Fetches and recommends news articles that semantically match a user's interests.

Explainable AI (XAI): Each recommendation includes a tag explaining which of the user's interests triggered it.

Real-Time News: Pulls the latest articles from around the world using the NewsAPI.

Efficient Semantic Search: Uses sentence transformers and a FAISS vector index for fast and accurate similarity search.

Simple Web Interface: A clean and modern UI built with Flask to display the results.

How It Works
The project follows a simple yet powerful pipeline to deliver explainable recommendations:

Fetch: It starts by fetching a large pool of recent news articles from the NewsAPI based on a broad set of keywords.

Embed: The description of each article is converted into a numerical vector (an embedding) using a sentence-transformers model. This vector captures the article's semantic meaning.

Index: All article embeddings are stored in a FAISS index, which allows for incredibly fast similarity searches.

Recommend & Explain: The user's interests are also converted into embeddings. The system searches the FAISS index for the articles most similar to the user's interests. For each match, it identifies which specific interest had the highest similarity score, and that becomes the "reason" for the recommendation.

Technologies Used
Backend: Python, Flask

AI & Machine Learning:

sentence-transformers: For creating high-quality semantic embeddings.

faiss-cpu: For efficient similarity search in the vector index.

Data: NewsAPI

Environment Management: python-dotenv for securely managing API keys.

Setup and Installation
Follow these steps to get the project running on your local machine.

1. Clone the Repository
git clone [https://github.com/your-username/news-recommender.git](https://github.com/your-username/news-recommender.git)
cd news-recommender

2. Install Dependencies
It's recommended to use a virtual environment.

# Create and activate a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

# Install the required libraries
pip install -r requirements.txt

(Note: You will need to create a requirements.txt file by running pip freeze > requirements.txt)

3. Set Up Environment Variables
This project requires a NewsAPI key to fetch articles.

Get an API Key: Register for a free developer account at NewsAPI.org to get your key.

Create a .env file: In the root of the project folder, create a new file named .env.

Add your key: Inside the .env file, add your API key like this:

NEWS_API_KEY="YOUR_ACTUAL_NEWS_API_KEY_HERE"

How to Run the Application
Once the setup is complete, you can start the web server.

Run the Flask app from your terminal:

flask run

Open your browser and navigate to:

[http://127.0.0.1:5000](http://127.0.0.1:5000)

You should now see your personalized and explainable news feed!

Project Structure
news-recommender/
├── app.py                # The main Flask web application
├── engine.py             # Core logic for fetching, embedding, and recommending
└── templates/
    └── index.html        # The HTML template for the user interface
