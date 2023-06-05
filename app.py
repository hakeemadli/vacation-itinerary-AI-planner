from flask import request
import openai



def text_completion():
    
     # fecthing input prompt on web-form
    days = request.form.get ("days")
    destination =request.form.get ("destination")
    
    with open('static/prompt.txt', 'r') as f:
        content= f.read()

        
    input_prompt = ('List'+ days + 'days itinerary at' + destination+ ' :')
    prompt= content + input_prompt
    
    
    # Generate a response
    completion = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=500,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        #stream = True, 
        stop = ['\#']
    )
    
    if days == '' and destination =='':
        result = "There is no input?"
    else:
         result = completion.choices[0].text

    
    return result
            
        