from PIL import Image
import pandas as pd
import requests
from io import BytesIO

def create_inspiration_board(image_urls):
    images = [Image.open(BytesIO(requests.get(url).content)) for url in image_urls]
    board_width = max(image.width for image in images)
    board_height = sum(image.height for image in images)
    board = Image.new('RGB', (board_width, board_height))
    y_offset = 0
    for image in images:
        board.paste(image, (0, y_offset))
        y_offset += image.height
    return board

df = pd.read_csv('data/fashion_data.csv')
image_urls = df['image_link'].tolist()
board = create_inspiration_board(image_urls)
board.show()
