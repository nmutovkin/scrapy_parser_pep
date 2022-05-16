import datetime as dt
import os
from pathlib import Path
from scrapy.exceptions import DropItem

BASE_DIR = Path(__file__).parent.parent
DATETIME_FORMAT = '%Y-%d-%mT%H-%M-%S'


class PepParsePipeline:

    def open_spider(self, spider):
        now = dt.datetime.now().strftime(DATETIME_FORMAT)
        os.makedirs(BASE_DIR / 'results', exist_ok=True)
        self.fd = open(BASE_DIR / 'results' / f'status_summary_{now}.csv',
                       'w')
        self.fd.write('Статус,Количество\n')
        self.statuses = {}

    def process_item(self, item, spider):
        if 'status' in item.keys():
            if item['status'] in self.statuses.keys():
                self.statuses[item['status']] += 1
            else:
                self.statuses[item['status']] = 1
            return item
        else:
            raise DropItem('Статус не найден!')

    def close_spider(self, spider):
        total = 0

        for status, count in self.statuses.items():
            self.fd.write(f'{status},{count}\n')
            total += count

        self.fd.write(f'Total,{total}\n')
        self.fd.close()
