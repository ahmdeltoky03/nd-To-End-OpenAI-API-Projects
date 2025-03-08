## Import Needed Libraries
import os
import re
import time
import openai
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv()) # read local .env file

## configure openai api key
openai.api_key  = os.getenv('OPENAI_API_KEY')

all_messages = list()

## system prompt
system_prompt = "Answer as concisely as possible."
all_messages.append({"role":"system", "content":system_prompt})

def custom_chatbot(user_prompt: str):
  """This function is a custom chatbot that uses GPT-3.5-turbo model to generate responses to user prompts.
  

  Args:
      user_prompt (str): User's input prompt

  Returns:
      response : The response of chat completion API
  """

  while True:
  
      ## if user want to exit
      if user_prompt.lower() in ["exit","quit"]:
        time.sleep(3)
        all_messages.clear()
        return "Thanks For Using My Chatbot ...."
      
      ## if user wronged and entered more space
      elif re.sub(r'\s+', ' ', user_prompt)==" ":
          # `\s+` matches one or more whitespace characters (spaces, tabs, newlines)
          # `re.sub(r'\s+', '', user_prompt)` removes all whitespace
          # If the result is an empty string (""), it means the input contained only spaces
          continue  # Skip this iteration == entered new prompt
      
      else :          
          all_messages.append({"role":"user", "content":user_prompt})
          response = openai.ChatCompletion.create(
                                  model = "gpt-3.5-turbo",
                                  messages = all_messages,
                                  temperature = .7,
                                  max_tokens = 1000
                                  )
          response = response["choices"][0]["message"]["content"]
        
          ## add memory (answer of previous question )
          all_messages.append({"role":"assistant", "content":response})
          
          return response
