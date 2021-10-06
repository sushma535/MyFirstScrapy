import csv
import scrapy

class StudentsScrapySpider(scrapy.Spider):
    name = 'StudentsScrapy'
    allowed_domains = ['vu.edu.au/']
    start_urls = ['http://www.vu.edu.au/current-students//']
    csv_columns = ['title', 'url', 'status', 'tags', 'content']
    csv_file = f'./studentsscrapy/spiders/csv/{name}.csv'

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