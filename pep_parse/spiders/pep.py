from urllib.parse import urljoin

import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        all_peps = response.css(
            'section[id*=numerical-index] tbody tr td a::attr(href)'
        ).getall()
        for pep_link in all_peps:
            next_url = urljoin(response.url, pep_link)
            yield response.follow(next_url, callback=self.parse_pep)

    def parse_pep(self, response):
        data = {
            'number': response.xpath(
                '//*[@id="pep-page-section"]/header/ul/li[3]/text()'
            ).get().replace('PEP ', ''),
            'name': response.css('h1.page-title::text').get().split(' – ')[1],
            'status': response.css(
                'dt:contains("Status") + dd abbr::text'
            ).get(),
        }

        yield PepParseItem(data)
