from utils import analyze_sentiment
from fastapi import FastAPI


# Initialize a FastAPI app
app = FastAPI(debug=True)


@app.post("/analyze_sentiment")
async def _analyze_sentiment(user_prompt: str):
    """
    text : user_prompt
    """
    result = analyze_sentiment(user_prompt)
    return result