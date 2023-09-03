from django.shortcuts import render
import openai
import os
from dotenv import load_dotenv


# Create your views here.
load_dotenv()
api_key = os.getenv("OPENAI_KEY", None)


def chatgpt(request):
    chatgpt_response = None
    if api_key != None and request.method == 'POST':
        openai.api_key = api_key
        user_input = request.POST.get('user_input')
        prompt = user_input

        response = openai.Completion.create(
            engine="gpt-3.5-turbo",
            prompt=prompt,
            max_tokens=256,
            # n=1,
            # stop=None,
            temperature=0.5,
        )
        print(response)
        
        chatgpt_response = response["choices"][0]["text"]

    return render(request, 'chatgpt.html', {"response":chatgpt_response})
