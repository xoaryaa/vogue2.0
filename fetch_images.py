import requests
import pandas as pd
import os

API_KEY = os.getenv('API_KEY')
CSE_ID = os.getenv('CSE_ID')
QUERY = 'latest fashion trends'

def fetch_images(api_key, cse_id, query, num_results=10):
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&cx={cse_id}&key={api_key}&searchType=image&num={num_results}"
    response = requests.get(url)
    return response.json()

data = fetch_images(API_KEY, CSE_ID, QUERY)
images = []

for item in data.get('items', []):
    images.append({
        'title': item['title'],
        'link': item['link'],
        'image_link': item['link']
    })

df = pd.DataFrame(images)
df.to_csv('data/fashion_data.csv', index=False)
