import unittest
import scrapy
from scrapy.crawler import CrawlerProcess
class NewSpider(scrapy.Spider):
    name = "new_spider"
    start_urls = ['http://172.18.58.80/varsity/']

    def parse(self, response):
     css_selector = 'img'
     for x in response.css(css_selector):
      newsel = '@src'
      yield {
       'Image Link': x.xpath(newsel).extract_first(),
}
# To recurse next page
      Page_selector = '.next a ::attr(href)'
      next_page = response.css(Page_selector).extract_first()
      if next_page:
          yield scrapy.Request(
              response.urljoin(next_page),
              callback=self.parse
          )


process = CrawlerProcess()
process.crawl(NewSpider)
process.start()




