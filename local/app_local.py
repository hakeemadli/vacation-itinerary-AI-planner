import openai
import os
from auth_key import auth_key

openai.api_key= auth_key

with open('flask-app/prompt.txt', 'r') as f:
    prompt = f.read()

# input prompt
print('Enter number of days: ')
days = input()
print('Enter vacation destination: ')
destination = input()

input_prompt = ('List '+ days + 'days itinerary at' + destination)

# Set the model and prompt
model_engine = 'text-davinci-003'
compiled_prompt = prompt + input_prompt

def text_completion():
# Generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=compiled_prompt,
        max_tokens=256,
        temperature=0.5,
        top_p=1,
        n = 3,
        frequency_penalty=0,
        presence_penalty=0, 
        stop = ['\#']
    )
    
    result = print(completion.choices[0].text)
    return result


text_completion()