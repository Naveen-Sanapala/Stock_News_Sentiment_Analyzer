# tracking.py
import mlflow

# Set up MLflow experiment
mlflow.set_experiment("RealTimeSentimentAnalyzer")
mlflow.langchain.autolog()  # enable LangChain tracing

def log_run(company, ticker, news, sentiment_result):
    with mlflow.start_run():
        mlflow.log_param("company", company)
        mlflow.log_param("stock_code", ticker)
        # Log raw news text as artifact
        mlflow.log_text(news, "news.txt")
        # Log output JSON
        mlflow.log_text(str(sentiment_result), "sentiment_output.json")
        # Metrics
        mlflow.log_param("sentiment", sentiment_result.get("sentiment"))
        mlflow.log_metric("confidence_score", float(sentiment_result.get("confidence_score", 0.0)))
