import scrapy


class IlluminatenewwscrapSpider(scrapy.Spider):
    name = "illuminatenewwscrap"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/kaliningrad/category/svet"]

    def parse(self, response):
        pass
