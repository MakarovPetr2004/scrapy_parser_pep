import csv
import datetime as dt

from pep_parse.constants import BASE_DIR


class PepParsePipeline:

    def open_spider(self, spider):
        self.status_counter = {}

    def process_item(self, item, spider):

        if item['status'] in self.status_counter:
            self.status_counter[item['status']] += 1
        else:
            self.status_counter[item['status']] = 1
        return item

    def close_spider(self, spider):
        results_dir = BASE_DIR / 'results'
        results_dir.mkdir(exist_ok=True)

        now_time = dt.datetime.now()
        filename = f'status_summary_{now_time}.csv'
        file_path = results_dir / filename

        with open(file_path, mode='w', encoding='utf-8') as f:
            writer = csv.writer(f, dialect='unix', quoting=csv.QUOTE_NONE)

            writer.writerow(('Статус', 'Количество'))

            writer.writerows(list(self.status_counter.items()))

            writer.writerow(('Total', sum(self.status_counter.values())))
