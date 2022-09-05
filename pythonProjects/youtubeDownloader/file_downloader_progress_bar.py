from time import time
from tqdm import tqdm
import time

import requests

chunk_size = 1024

pdf_file= f"https://www.doc-developpement-durable.org/file/Projets-informatiques/cours-&-manuels-informatiques/Python/The%20Python%20Standard%20Library%20by%20Example.pdf"

r = requests.get(pdf_file, stream = True)
file_size = int(r.headers['content-length'])

""" for x in tqdm(range(1000)):
    time.sleep(0.01) """


with open("Python.pdf" , 'wb') as f :
    for data in tqdm(iterable=r.iter_content(chunk_size=chunk_size), total = file_size/chunk_size, unit = 'KB' ):
        f.write(data)

print("Download Completed!")