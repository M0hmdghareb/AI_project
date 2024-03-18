import os
from dotenv import load_dotenv
from langchain_openai import OpenAI
import requests

def generate_title(user_input_prompt):
    load_dotenv('.env')
    llm = OpenAI(model_name='gpt-3.5-turbo-instruct',
                       max_tokens='256',
                       temperature='0.5')
    prompt =  f"{user_input_prompt} not exceed 4 word" #f"Suggest a title for a website about {user_input_prompt}"
    output = llm(prompt)
    
    # Split the suggestions (assuming they are separated by newline characters)
    suggestions = output.strip().split('\n')
    
    # Select the first suggestion
    suggested_title = suggestions[0].strip()   
    return suggested_title


def generate_description(title):
    load_dotenv('.env')
    llm = OpenAI(model_name='gpt-3.5-turbo-instruct',
                       max_tokens='256',  # Set the max tokens to half of 512 for a shorter description
                       temperature='0.5')  

    prompt = f"Create a brief description for the title: '{title}'\n\nDescription:"
    output = llm(prompt)
    
    # Assuming output is a string containing the suggested description
    suggested_description = output.strip()
    
    return suggested_description




def search_image(image_name):
    # Replace with your Google Custom Search API credentials
    api_key = 'AIzaSyDAqHqVO9fRiESqLeQjslNh53ZiV36rgqI'
    cx = '7266ebe81ea1a4367'

    def get_google_custom_search_url():
        base_url = 'https://www.googleapis.com/customsearch/v1'
        params = {
            'key': api_key,
            'cx': cx,
            'q': image_name,
            'searchType': 'image',
            'num': 1
        }
        return f'{base_url}?{requests.compat.urlencode(params)}'

    # Construct the Google Custom Search API URL
    url = get_google_custom_search_url()

    # Make a request to the API
    response = requests.get(url)

    # Check if the request was successful
    if response.ok:
        # Parse the JSON response
        data = response.json()

        # Extract the first image URL from the search results
        items = data.get('items', [])
        if items:
            image_url = items[0]['link']

            # Print the image URL
            print(f"Image URL: {image_url}")

            # You can download or display the image as needed
        else:
            print("No images found for the given text query.")
    else:
        print(f"Error: {response.status_code}")


"""
def search_image(query):
  prompt = f"Search for a relevant, high quality image for {query}"
  response = openai.Image.create(
    prompt=prompt, 
    n=1,
    size="1024x1024"
  )
  return response['data'][0]['url']
  """



print(generate_title("generate a title for flower website"))

#search_image("cats")