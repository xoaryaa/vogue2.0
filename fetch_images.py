import requests
import pandas as pd

API_KEY = 'AIzaSyCbR7Yu0jtGGG0o9KQv3Lo2BmHCUcTglMg'
CSE_ID = '9770547ff93ef4ec8'
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
