import scrapy
from scrapy.crawler import CrawlerProcess
class NewSpider(scrapy.Spider):
    name = "new_spider"
    start_urls = ['http://brickset.com/sets/year-2019']
process = CrawlerProcess()
process.crawl(NewSpider)
process.start()