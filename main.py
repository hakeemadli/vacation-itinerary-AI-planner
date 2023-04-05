from flask import Flask, render_template, request, redirect, url_for
import openai
import os
from app import text_completion
from dotenv import load_dotenv

load_dotenv()
 

app = Flask(__name__)

# Set API key in auth_key
openai.api_key= os.getenv('auth_api_key')

@app.route('/', methods=['POST', 'GET'])

def home():
    result= []
    if request.method =='POST'and 'days' in request.form and 'destination' in request.form:
        
        
        result = text_completion()

         
    return render_template('index.html', result = result)
   
   
if __name__ == '__main__':
    app.run(debug=True)