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
           title = book.xpath('.//h3/a/@title').extract_first()
           print(title)
           #whole html xpath: response.xpath('//....
           #for on in the loop: response.xpath('.//....

       print(len(all_the_books))
        #pass
