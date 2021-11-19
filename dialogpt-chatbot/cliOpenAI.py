from flask import Flask, render_template, request
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import openai
import os

app = Flask(__name__)

tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")




def get_bot_response():

    # Load your API key from an environment variable or secret management service
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.Completion.create(engine="davinci", prompt="what the fuck", max_tokens=5)
    print ("Fucking Type: ", type(response))
    print (response.values())

    return response

get_bot_response()

