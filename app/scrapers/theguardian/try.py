import json
import subprocess
from scrapy.crawler import CrawlerProcess
from article import TGArticleSpider

with open('headlines.json') as f: items = json.load(f)

i = 1

extracted = []
outputResponse = dict()
process = CrawlerProcess({'FEED_FORMAT':'json'})
process.crawl(TGArticleSpider, start_urls=[item['link'][0] for item in items], outputResponse=outputResponse)
process.start(stop_after_crawl=True)

data = outputResponse

for item in data['items']:

    extracted.append(item)

    with open('test.html', 'a') as outfile:
        outfile.write("<h1>"+ ''.join(item['title']) + "</h1>")
        outfile.write("<br>\n")
        outfile.write("<h2>"+ ''.join(item['author']) + "</h2>")
        outfile.write("<br>\n")
        outfile.write("<h3>"+ ''.join(item['tags']) + "</h3>")
        outfile.write("<br>\n")
        outfile.write("<h4>"+ ''.join(item['url']) + "</h4>")
        outfile.write("<br>\n")
        outfile.write(''.join(item['body']))
        outfile.write("<br>\n")
        outfile.write(''.join(item['images']))
        outfile.write('<hr>')

    i += 1

    if i == 20: break

process.stop()
# with open('data.json', 'w') as outfile:
#     json.dump({"items": extracted}, outfile)
