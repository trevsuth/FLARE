from langchain_community.document_loaders import YoutubeLoader
import requests
import re
from tqdm import tqdm

sample_url = "https://www.youtube.com/@rrwithdeku8677/videos"
r = requests.get(sample_url)
page = (r.text)
pattern = r'watch\?v=([^"]+)'
matches = re.findall(pattern, page, re.IGNORECASE)
ids = [x.split('=')[-1] for x in matches] 

base_url = 'https://www.youtube.com/watch?v='

# Using YoutubeLoader
for i,id in tqdm(enumerate(ids)):
    loader = YoutubeLoader.from_youtube_url(
        base_url + id, add_video_info=True
    )
    print('got loader')
    data = loader.load()
    print(data)
    # create a file for each video and write the transcript to it
    with open(f"data/{i}.txt", "w") as f:
        f.write(data[0].page_content)