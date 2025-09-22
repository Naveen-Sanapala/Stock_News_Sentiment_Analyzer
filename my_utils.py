# news_fetch.py
from langchain_community.tools.yahoo_finance_news import YahooFinanceNewsTool
from langchain_community.tools import BraveSearch
import requests
# Initialize tools (you need to install langchain-community package)
yahoo_news_tool = YahooFinanceNewsTool()

def fetch_news(ticker: str) -> str:
    # Use Yahoo Finance News tool

    news_content = yahoo_news_tool.invoke(ticker)
    
    return news_content
print(fetch_news("MSFT"))
#print(fetch_news("AMZN"))
#print(fetch_news("AAPL"))

def get_stock_ticker(company_name:str):
    yfinance = "https://query2.finance.yahoo.com/v1/finance/search"
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    params = {"q": company_name, "quotes_count": 1, "country": "United States"}

    res = requests.get(url=yfinance, params=params, headers={'User-Agent': user_agent})
    data = res.json()

    company_code = data['quotes'][0]['symbol']
    return company_code
#print(get_stock_ticker("apple"))