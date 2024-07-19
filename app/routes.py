# from flask import render_template
# import pandas as pd
# from app import app

# @app.route('/')
# def home():
#     df = pd.read_csv('data/fashion_data.csv')
#     return render_template('index.html', images=df.to_dict(orient='records'))

from flask import render_template, request
import pandas as pd
import requests

from app import app

API_KEY = 'AIzaSyCbR7Yu0jtGGG0o9KQv3Lo2BmHCUcTglMg'
CSE_ID = '9770547ff93ef4ec8'


def fetch_images(api_key, cse_id, query, num_results=10):
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&cx={cse_id}&key={api_key}&searchType=image&num={num_results}"
    response = requests.get(url)
    return response.json()

@app.route('/')
def home():
    query = request.args.get('query', 'latest fashion trends')
    data = fetch_images(API_KEY, CSE_ID, query)
    images = []

    for item in data.get('items', []):
        images.append({
            'title': item['title'],
            'link': item['link'],
            'image_link': item['link']
        })

    df = pd.DataFrame(images)
    return render_template('index.html', images=df.to_dict(orient='records'))
