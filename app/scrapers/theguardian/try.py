import json
import subprocess

with open('headlines.json') as f: items = json.load(f)

i = 1

extracted = []

for item in items:
    url = item['link'][0]

    subprocess.check_output([
        'scrapy',
        'runspider',
        'article.py',
        '-a',
        f'url={url}',
        '-o',
        f'{i}.json'
    ])

    with open(f'{i}.json') as f: data = json.load(f)

    extracted.append(data[0])

    subprocess.check_output([
        'rm',
        '-f',
        f'{i}.json'
    ])

    i += 1

with open('data.json', 'w') as outfile:
    json.dump({"items": extracted}, outfile)
