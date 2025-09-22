# sentiment_analysis.py
from langchain_core.prompts import ChatPromptTemplate
from langchain.output_parsers.structured import StructuredOutputParser, ResponseSchema
from llm_utils import llm
# Define the output schema
schemas = [
    ResponseSchema(name="company_name", description="Name of the company (string)"),
    ResponseSchema(name="stock_code", description="Stock ticker symbol (string)"),
    ResponseSchema(name="newsdesc", description="Summary of news content given (string)"),
    ResponseSchema(name="sentiment", description="Sentiment (Positive, Negative, or Neutral) (string)"),
    ResponseSchema(name="people_names", description="List of people named in the news (list of strings)"),
    ResponseSchema(name="places_names", description="List of places mentioned (list of strings)"),
    ResponseSchema(name="other_companies_referred", description="Other companies mentioned (list of strings)"),
    ResponseSchema(name="related_industries", description="Industries related to the news/company (list of strings)"),
    ResponseSchema(name="market_implications", description="Impact on the stock market or investors (string)"),
    ResponseSchema(name="confidence_score", description="Confidence score (float, between 0.0 and 1.0)")
]

output_parser = StructuredOutputParser.from_response_schemas(schemas)

# Build prompt
prompt_template = """
Given the following news description, classify the sentiment as Positive/Negative/Neutral,
extract people, places, other companies, and related industries mentioned, and assess market implications.
Return a JSON with the fields: company_name, stock_code, newsdesc, sentiment, 
people_names, places_names, other_companies_referred, related_industries, market_implications, confidence_score.

News: "{newsdesc}"
Company: "{company}", Ticker: "{stock_code}"

Output JSON format instructions:
{output_format}
"""
chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a financial news analysis assistant."),
    ("user", prompt_template)
])

def analyze_sentiment(company: str, ticker: str, news_text: str) -> dict:
    # Fill prompt and parse output
    formatted_prompt = chat_prompt.format_prompt(
        company=company, stock_code=ticker, newsdesc=news_text,
        output_format=output_parser.get_format_instructions()
    )
    response = llm.invoke([("user", formatted_prompt.to_string())])
    # Parse JSON from LLM output
    output = output_parser.parse(response.content)
    return output

