"""
This module is used to converse with chatgpt agent
"""

# Imports
import os
import openai
import logging


# Settings
openai.api_key = os.getenv("OPENAI_API_KEY")


# Classes
class Chat:
    
  def __init__(self, model: str):
    self.model = model
    self.messages = []

  def continue_conversation(self, message: str):
    """
    Use this to continue the conversation in the same thread
    """
    logging.info(f"Asking question: {message}")
    self.messages.append({"role": "user", "content": message})
    return self.__chat_completion()
    

  def start_new_conversation(self):
    """
    Use this to clear prior conversation
    """
    logging.info("Starting new conversation...")
    self.messages = []

  def __chat_completion(self):
    """
    Makes API call
    """
    logging.debug(f"Reaching out to ChatGPT with conversation: {self.messages}")
    completion = openai.ChatCompletion.create(
      model=self.model,
      messages=self.messages
    )
    message = completion['choices'][0]['message']
    logging.info(f"Response: {message}")
    self.messages.append(message)
    return message['content']
        
  
# Functions
def sample():
  conv = Chat(model='gpt-3.5-turbo')
  conv.continue_conversation('Tell the world about the ChatGPT API in the style of a pirate.')
  conv.continue_conversation('Give me more')  # Will continue talking about API in a pirate accent
  conv.start_new_conversation()
  conv.continue_conversation('Give me more')  # Should be confused
