# Stock_News_Sentiment_Analyzer
This project analyzes stock market news in real time using Google Gemini (via LangChain), performs sentiment analysis, extracts entities (companies, people, places, industries), and provides insights on market implications.

It exposes:

A FastAPI backend with REST endpoints

A Streamlit frontend for interactive use

MLflow tracking for logging and experiment management

# Features

✅ Fetch company news and stock data from Yahoo Finance
✅ Perform sentiment analysis using langchain_google_genai
✅ Extract structured information (companies, people, places, industries)
✅ Return confidence scores for predictions
✅ Store results & artifacts in MLflow
✅ FastAPI endpoints for programmatic access
✅ Streamlit UI for analysts and users

# Folder structure
│── api_service.py          # FastAPI backend
│── streamlit_app.py        # Streamlit UI
│── sentiment_analysis.py   # Core sentiment analysis logic
│── tracking.py             # MLflow logging
│── requirements.txt        # Python dependencies
│── README.md               # Project documentation
│── venv/                  # Virtual environment (local only)
|-- .env.                  # api key (local only)


# Create the virtual environment
python3 -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate

# install dependencies 
pip install -r requirements.txt

# Set environment variables
GOOGLE_API_KEY=your_google_gemini_api_key
MLFLOW_TRACKING_URI=http://127.0.0.1:5000 


# Run Fastapi Backend:
uvicorn api_service:app --reload --port 8000


# Run streamlit backend 
streamlit run streamlit_app.py

# Run ML flow tracking UI 
mlflow ui
