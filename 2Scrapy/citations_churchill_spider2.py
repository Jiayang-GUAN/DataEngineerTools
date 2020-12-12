import scrapy
import re

class ChurchillQuotesSpider(scrapy.Spider):
    name = "citations de Churchill"
    start_urls = ["http://evene.lefigaro.fr/citations/winston-churchill",]

    def parse(self, response):
        for cit in response.xpath('//li[@class="figsco__selection__list__evene__list__item"]'):
            text_value = cit.xpath('article/div[1]/a/text()').extract_first()
            text_value = re.sub('“','',text_value)
            text_value = re.sub('”','',text_value)
            author_value = cit.xpath('article/div[2]/div[2]/a/text()').extract_first()
            
            yield { 'text' : text_value, 'author' : author_value}