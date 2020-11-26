import scrapy


class BookspiderSpider(scrapy.Spider):
    name = 'bookspider'
    allowed_domains = ['books.toscrape.com/']
    start_urls = ['https://books.toscrape.com//']

    def parse(self, response):
       # print(response.url)
       # print(response.status)

       all_the_books = response.xpath('//article[@class="product_pod"]')

       for book in all_the_books:
           #each book is the article selected above
           #in each article grab the h3 anchor tag title attribute
           #whole html xpath: response.xpath('//....
           #for on in the loop: response.xpath('.//....
           title = book.xpath('.//h3/a/@title').extract_first()
           price = book.xpath('.//div[@class="product_price"]/p[@class="price_color"]/text()').extract_first()
           thumb = self.start_urls[0] + book.xpath('.//div[@class="image_container"]/a/img/@src').extract_first()
           bookLink = self.start_urls[0] + book.xpath('.//div[@class="image_container"]/a/@href').extract_first()
           print(title)
           print(price)
           print(thumb)
           print(bookLink)
            
           yield{
                'Title': title,
                'Price': price,
                'Thumb': thumb,
                'Link': bookLink
            }
       print(len(all_the_books))
        #pass
