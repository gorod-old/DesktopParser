from selenium.webdriver.common.by import By

from MessagePack import print_info_msg
from WebDriverPack import WebDriver

# information string
marker = 'Parser https://emex.ru'
# project folder
folder = 'emex_ru'
encoding = 'utf-8'
row_append_timeout = 0.2

# header
# list[header key, ...]
header_map = ['№ номер', 'Производитель', 'Номер', 'Описание', 'Цена', 'Ссылка']

# hyperlink keys
hyper = ['Ссылка']

# status color key
status_key = 'Производитель'

# database setup
# dict[header key: [sqlite type | default value]]; sql types: INTEGER, REAL, NUMERIC, TEXT, NONE;
db_type_map = {

}

# formats of saving the result: 'json', 'xlsx', 'csv', 'db', 'image', 'html'; default: [];
save_list = ['xlsx']

# image resizing
img_max_size = None

# xlsx save settings
header_height = 30
row_height = 20
column_width = 15

# columns width for app table
col_width_list = [17, 40, 60, 40, 40, 40]
# columns width by name for excel
col_width_map = {
    '№ номер': 10.54,
    'Производитель': 24.8,
    'Номер': 37.2,
    'Описание': 24.8,
    'Цена': 24.8,
    'Ссылка': 24.8,
}


class ParsItem:
    __key_list = ['№ номер', 'Производитель', 'Номер', 'Описание', 'Цена', 'Ссылка']

    def __init__(self, parser: WebDriver, start_url):
        super(ParsItem, self).__init__()
        self._parser = parser
        self._start_url = start_url
        self.__key_data = {}
        self._files = []
        self._msg_info = False

    def msg_check(self):
        return self._msg_info

    def get_row_data(self):
        row_data = {}
        self._parser.get_page(self._start_url)
        data_check = False
        for key in self.__key_list:
            print_info_msg(msg=f'processing key: {key}', stream=self._parser.stream)
            data = self._get_key_data(key)
            print_info_msg(msg=f'key: {key}, data: {data}', stream=self._parser.stream)
            if data is not None and len(data) != 0:
                data_check = True
            row_data.update({key: data})
        if not data_check:
            print('NO data URL: ', self._start_url)
        return row_data if data_check else None

    def _get_key_data(self, key):
        extractors = {
            'Производитель': self._func_1,
            'Номер': self._func_2,
            'Описание': self._func_3,
            'Цена': self._func_4,
            'Ссылка': self._func_5,
        }
        func = extractors.get(key)
        data = func() if func else None
        return data

    def _func_1(self):
        get_by = (By.XPATH, '')
        in_el = None
        attr = ('text', 'href',)
        data = self._parser.get_el_attribute(get_by, in_el, *attr)

        return data

    def _func_2(self):
        get_by = (By.XPATH, '')
        in_el = None
        attr = ('text',)
        data = self._parser.get_el_attribute(get_by, in_el, *attr)

        return data

    def _func_3(self):
        get_by = (By.XPATH, '')
        in_el = None
        attr = ('text',)
        data = self._parser.get_el_attribute(get_by, in_el, *attr)

        return data

    def _func_4(self):
        get_by = (By.XPATH, '')
        in_el = None
        attr = ('text',)
        data = self._parser.get_el_attribute(get_by, in_el, *attr)

        return data

    def _func_5(self):
        get_by = (By.XPATH, '')
        in_el = None
        attr = ('text', 'href',)
        data = self._parser.get_el_attribute(get_by, in_el, *attr)

        return data
