import csv
import scrapy

class Victoria_Edu_ScrapySpider(scrapy.Spider):
    name = 'Victotia_Edu_Scrapy'
    allowed_domains = ['vu.edu.au/']
    start_urls = ['http://www.vu.edu.au//']
    csv_columns = ['title', 'url', 'status', 'tags', 'content']
    csv_file = f'./victoria_edu_scrapy/spiders/csv/{name}.csv'

    def parse(self, response):
        content = response.css('article').get()
        tags = response.css('a::attr(href)').getall()
        title_text = response.css('title::text').get()
        result = {'title': title_text, 'url': response.url, 'status': response.status, 'tags': tags, 'content': content}

        try:
            with open(self.csv_file, 'w') as self.csv_file:
                writer = csv.DictWriter(self.csv_file, fieldnames=self.csv_columns)
                writer.writeheader()
                writer.writerow(result)
        except IOError:
            print("I/O error")