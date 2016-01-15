#coding:utf-8
__author__ = 'marvin'

from scrapy.conf import settings
from scrapy.contrib.exporter import CsvItemExporter

class CSVkwItemExporter(CsvItemExporter):

    def __init__(self, *args, **kwargs):
        kwargs['fields_to_export'] = settings.getlist('EXPORT_FIELDS') or None
        kwargs['encoding'] = settings.get('EXPORT_ENCODING', 'utf-8')

        super(CSVkwItemExporter, self).__init__(*args, **kwargs)

class CSVGoldItemExporter(CsvItemExporter):

    def __init__(self, *args, **kwargs):
        kwargs['fields_to_export'] = settings.getlist('EXPORT_FIELDS_GOLD') or None
        kwargs['encoding'] = settings.get('EXPORT_ENCODING', 'utf-8')

        super(CSVGoldItemExporter, self).__init__(*args, **kwargs)

class CSVBankItemExporter(CsvItemExporter):

    def __init__(self, *args, **kwargs):
        kwargs['fields_to_export'] = settings.getlist('EXPORT_FIELDS_BANK') or None
        kwargs['encoding'] = settings.get('EXPORT_ENCODING', 'utf-8')

        super(CSVBankItemExporter, self).__init__(*args, **kwargs)