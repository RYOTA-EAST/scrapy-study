import scrapy


class DesktopSpider(scrapy.Spider):
    name = 'desktop'
    allowed_domains = ['www.yodobashi.com']
    start_urls = ['http://www.yodobashi.com/category/19531/11970/34646/']

    def parse(self, response):
        products = response.xpath('//div[contains(@class, "productListTile")]')
        for product in products:
            maker = product.xpath('.//div[contains(@class, "pName")]/p/text()').get()
            name = product.xpath('.//div[contains(@class, "pName")]/p[2]/text()').get()
            price = product.xpath('.//span[@class="productPrice"]/text()').get()

            yield {
                'maker': maker,
                'name': name,
                'price': price,
            }
