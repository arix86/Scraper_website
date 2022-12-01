import scrapy
import requests
class WebsitesSpider(scrapy.Spider):
    name='web_site'
    start_urls=[
        'https://micerveza.com/sucursal/hab/caja-malta.html'
    ]
    custom_settings = {
        'CONCURRENT_REQUEST': 24,
        'MEMUSAGE_LIMIT_MB': 2048,
        'MEMUSAGE_NOTIFY_MAIL': ['arix86.solutions@gmail.com'],
        'ROBOTSTXT_OBEY': False,
        'USER_AGENT': 'REDCRIFY',
        'FEED_EXPORT_ENCODING': 'utf-8',
               
    }
    
    def parse(self,response):
        asw=response.xpath('//div[@class="product-info-stock-sku"]//span/text()').get()
        url="https://hooks.slack.com/services/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"
        if asw=="No está disponible":
            pass
        else:
            requests.post(url=url,json={'text':"Update desde la web Mi Cerveza: " + asw})
        