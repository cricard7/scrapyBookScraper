#Following: https://letslearnabout.net/tutorial/scrapy-tutorial/python-scrapy-tutorial-for-beginners-01-creating-your-first-spider/
#pip install scrapy
#scrapy startproject books
#cd to books
#scrapy genspider spidername url
#scrapy crawl spidername

#use xpath in chrome inspector to find elements
#eg:  //article[@class="product_pod"]

#https://devhints.io/xpath

# once spider has a yield statement we can output the file

#scrapy crawl spidername -o fileName.json
#scrapy crawl spidername -o fileName.csv
#scrapy crawl spidername -o fileName.xml