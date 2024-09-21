import scrapy


class IlluminatenewwscrapSpider(scrapy.Spider):
    name = "illuminatenewwscrap"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/kaliningrad/category/svet"]

    def parse(self, response):
        illuminaires = response.css('div.WdR1o')
        for illuminaire in illuminaires:
            yield {
                'name' : illuminaire.css("span.itemprop = 'name'").get(),
                'price' : illuminaire.css('span.ui-LD-ZU KIkOH').get(),
                'link' : illuminaire.css('a').attrib['href']
            }
