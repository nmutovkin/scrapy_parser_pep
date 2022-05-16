from pep_parse.items import PepParseItem
import re
import scrapy


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse_pep(self, response):
        pep_info_tag = response.xpath('//section[@id="pep-content"]')
        pep_name_num = pep_info_tag.css('h1::text').get().strip()

        pattern = r'PEP (?P<number>\d+).*'
        pep_match = re.search(pattern, pep_name_num)

        pep_num = int(pep_match.group(1))

        data = {
            'number': pep_num,
            'name': pep_name_num,
            'status': (pep_info_tag.css('dt:contains("Status") + dd::text').
                       get().strip())
        }

        yield PepParseItem(data)

    def parse(self, response):
        num_index = response.xpath('//section[@id="numerical-index"]')
        table = num_index.css('tbody')

        for row in table.css('tr'):
            pep_link = row.css('td.num').css('a::attr(href)').get()
            yield response.follow(pep_link, callback=self.parse_pep)
