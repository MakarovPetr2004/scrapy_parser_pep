# Проект парсинга pep
Парсит сайт [PEP](https://peps.python.org/), собирает информацию о всех pep(файл pep_ДАТА), а также о количестве всех статусов pep(файл status_summary_ДАТА) в папку results.
 
## Содержимое
* [Локальный запуск](#локальный-запуск)
* [Технологии](#технологии)
* [Авторы](#авторы)
 
## Локальный запуск:
```
pip install -r requirements.txt
```

```
scrapy crawl pep
```

## Технологии:
- Python 3.9
- Scrapy 2.5.1
- Pillow 9.0.0
- DRF 3.12.4
- Djoser 2.2.0

## Автор
* [Макаров Пётр](https://github.com/MakarovPetr2004)





