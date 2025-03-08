import os
import openai
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv()) # read local .env file

openai.api_key = os.getenv('OPENAI_API_KEY')

# customizing chatgpt

def analyze_sentiment(user_prompt):
    """
    text : user_prompt
    """
        
    system_prompt = """
                            You are a highly accurate sentiment analysis assistant. Your task is to analyze the sentiment of user-provided text and classify it into one of the following categories:  

                            1. **Positive** – The text expresses happiness, satisfaction or any form of positive emotion.  
                            2. **Negative** – The text expresses  sadness, anger, disappointment, or any negative sentiment.  
                            3. **Neutral** – The text does not strongly convey positive or negative emotions; it is factual or balanced.  

                            Additionally, provide a **confidence score** from 0 to 1, where:  
                            - **1.0** means extremely confident,  
                            - **0.5** means moderately confident,  
                            - **0.0** means not confident at all.  

                            When analyzing sentiment, consider the following:  
                            - **Emotion Words**: Look for strong emotional indicators like "love," "hate," "amazing," "terrible."  
                            - **Context & Tone**: Consider sarcasm, exclamation marks, or tone that changes the meaning.  
                            - **Polarity & Intensity**: Evaluate whether the sentiment is weak or strong.  

                            Format your response as follows:  
                            ```json
                            {
                              "sentiment": "Positive/Negative/Neutral",
                              "confidence": 0.0-1.0,
                              "explanation": "Brief reason why the sentiment was classified this way."
                            }

                            """

    messages = [
                {
                    "role":"system",
                    "content":system_prompt
                },
                {
                    "role":"user",
                    "content":user_prompt
                }
            ]

    ## call API
    response = openai.ChatCompletion.create(
                model = "gpt-3.5-turbo",
                messages = messages,
                temperature = 0.0,
                n = 1,
                max_tokens = 1000
            )

    return response["choices"][0]["message"]["content"]



