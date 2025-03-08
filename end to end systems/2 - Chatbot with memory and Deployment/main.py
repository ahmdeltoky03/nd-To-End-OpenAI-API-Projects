## import needed libraries
from fastapi import FastAPI
from utils import custom_chatbot


## Initialize an App
app = FastAPI(debug=True)


@app.post(("/chatbot"))
async def chatbot(user_prompt:str):
  response = custom_chatbot(user_prompt)
  return response 

"""
Before running this code, ensure you have the following:
Note: You must have a paid OpenAI API plan to use this endpoint and receive responses from the GPT-3.5-turbo model in your FastAPI deployment.
(loaded image of the fastapi deployment is shown but not give me output because I don't have a paid OpenAI API plan)

- Ensure you have a valid OpenAI API key set up in your `custom_chatbot` function.  
- This API expects a POST request with a `user_prompt` string as input.  
- The `custom_chatbot` function should handle API calls, formatting, and error handling.  
- Make sure your FastAPI server is running and accessible for clients to interact with the chatbot.  
"""

  

