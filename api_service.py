# api_service.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
from my_utils import get_stock_ticker
from my_utils import fetch_news
from sentiment_analysis import analyze_sentiment
from tracking import log_run

class SentimentResponse(BaseModel):
    company_name: str
    stock_code: str
    newsdesc: str
    sentiment: str
    people_names: list
    places_names: list
    other_companies_referred: list
    related_industries: list
    market_implications: str
    confidence_score: float

app = FastAPI()

@app.get("/analyze/", response_model=SentimentResponse)
async def analyze(company: str):
    try:
        # Step 1: Get ticker
        ticker = get_stock_ticker(company)
        print("ticker:", ticker)
        # Step 2: Fetch news
        news_text = fetch_news(ticker)
        print("News:", news_text)
        if not news_text:
            raise HTTPException(status_code=404, detail="No news found for ticker")
        # Step 3: Analyze with LLM
        result = analyze_sentiment(company, ticker, news_text)
        for field in ["people_names", "places_names", "other_companies_referred", "related_industries"]:
            val = result.get(field, [])

            if isinstance(val, str):   # if LLM returned "[]" or '["x","y"]'
                try:
                    import json
                    parsed = json.loads(val)
                    if isinstance(parsed, list):
                        result[field] = parsed
                    else:
                        result[field] = [parsed]  # wrap single value
                except Exception:
                    result[field] = []
        # Log run to MLflow
        print("result:",result)
        log_run(company, ticker, news_text, result)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("api_service:app", host="0.0.0.0", port=8000)
