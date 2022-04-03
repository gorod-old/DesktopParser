import math
import os
import subprocess
import sys
import threading
import webbrowser
from datetime import datetime
from queue import Queue
from time import sleep, perf_counter

import schedule
import urlvalidator
from PyQt5.QtWidgets import QTableWidgetItem, QApplication, QMainWindow
from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QSize, QDate, QTimer, QThread, pyqtSignal
from selenium.webdriver.common.by import By
from urlvalidator import ValidationError

import design
from MessagePack import print_info_msg, print_progress_msg, print_exception_msg
from Projects.emex_ru import proj_setup
from Projects.emex_ru.proj_setup import ParsItem, col_width_list, hyper, status_key, row_append_timeout
from WebDriverPack import WebDriver
from WebDriverPack.webDriver import try_func
from WinSoundPack import beep
from saveData import remove_directory, save_json, get_json_data_from_file, save_xlsx

HEADLESS = True


def start_app():
    marker = proj_setup.marker
    app = QApplication(sys.argv)
    app_window = MainWindow(marker=marker)
    app_window.show()
    sys.exit(app.exec())


class ScheduleThread(QThread):
    about_time = pyqtSignal(int)

    def add_time(self, time: int):
        schedule.every(time).hours.do(
            lambda: self.about_time.emit(time)
        )

    def run(self):
        while True:
            schedule.run_pending()
            sleep(1)


class MainWindow(QMainWindow, design.Ui_MainWindow):
    # Переопределяем конструктор класса
    def __init__(self, marker: str = ''):
        # Обязательно нужно вызвать метод супер класса
        QMainWindow.__init__(self)
        self.setupUi(self)

        # colors
        self._l_grn_color = QtGui.QColor(195, 250, 210)
        self._grn_color = QtGui.QColor(165, 245, 157)
        self._red_color = QtGui.QColor(245, 199, 191)
        self._r_color = QtGui.QColor(245, 238, 218)
        self._org_color = QtGui.QColor(252, 224, 121)
        self._blue_color = QtGui.QColor(207, 229, 250)

        # extract data from setup file
        self._sound = False
        self._proxy = False
        self._auto = False
        self._app_setup()

        self._start_datetime = datetime.now()
        self._start, self._i_start = 0, 0
        self._search_urls = 0
        self._parsed_num = 0
        self._run = False
        self._close_app = False
        self._repack_out_data = []
        self._row_color = 0  # 0 or 1 value permissible
        self._stream_num = os.cpu_count()
        print_info_msg('App init', msg=f'app run with stream num: {self._stream_num}')
        self._save_list = proj_setup.save_list
        self.p_list = []
        # Устанавливаем заголовок окна
        self.setWindowTitle(marker)
        # Устанавливаем заголовки таблицы
        self.header_labels = proj_setup.header_map
        self.table_widget.setColumnCount(len(self.header_labels))
        self.table_widget.setHorizontalHeaderLabels(self.header_labels)
        self.table_widget.verticalHeader().setVisible(True)  # row numbering
        # гиперссылки по двойному клику
        self.table_widget.itemDoubleClicked.connect(self.open_link)
        # делаем ресайз колонок по содержимому
        # self.table_widget.resizeColumnsToContents()
        # делаем ресайз колонок по списку ширин в настройках проекта
        for i, width in enumerate(col_width_list):
            self.table_widget.setColumnWidth(i, width * 5.6)
        # обработчики событий
        self.startButton.clicked.connect(self._start_click)
        self.stopButton.clicked.connect(self._stop_pars)
        self.autoExcelButton.clicked.connect(self._auto_excel_click)
        self.soundButton.clicked.connect(self._sound_click)
        self.proxyButton.clicked.connect(self._proxy_click)
        self.lineEdit.textChanged.connect(self._textbox_text_changed)
        self.clearButton.clicked.connect(self._clear_textbox)
        self.saveButton.clicked.connect(self._save_click)
        # ToolTips stylesheet
        self.setStyleSheet("""QToolTip {
                            border: 1px solid black;
                            padding: 3px;
                            border-radius: 3px;
                            opacity: 200;
                        }""")

    @classmethod
    def _qdate_to_string(cls, date: QDate):
        if date is None:
            return None
        date = "%02d.%02d.%04d" % (date.day(), date.month(), date.year())
        return date

    @classmethod
    def _string_to_qdate(cls, date: str):
        if date is None:
            return None
        date = date.split('.')
        date = QDate(int(date[-1]), int(date[-2]), int(date[-3]))
        return date

    def _clear_textbox(self):
        self.lineEdit.setText('')

    def _textbox_text_changed(self):
        pass

    def _auto_excel_click(self):
        self._auto = not self._auto
        self._save_app_setup()
        if self._auto:
            self.autoExcelButton.setText('АВТО ЗАПУСК EXCEL ВКЛ')
            self.autoExcelButton.setStyleSheet('background: rgb(115, 115, 115); color: white;')
        else:
            self.autoExcelButton.setText('АВТО ЗАПУСК EXCEL ВЫКЛ')
            self.autoExcelButton.setStyleSheet('background: rgb(115, 115, 115); color: white;')

    def _sound_click(self):
        self._sound = not self._sound
        self._save_app_setup()
        if self._sound:
            self.soundButton.setText('ЗВУК ВКЛ')
            self.soundButton.setStyleSheet('background: rgb(115, 115, 115); color: white; margin-right: 7px;')
        else:
            self.soundButton.setText('ЗВУК ВЫКЛ')
            self.soundButton.setStyleSheet('background: rgb(115, 115, 115); color: white; margin-right: 7px;')

    def _proxy_click(self):
        self._proxy = not self._proxy
        self._save_app_setup()
        if self._proxy:
            self.proxyButton.setText('PROXY ON')
            self.proxyButton.setStyleSheet('background: rgb(115, 115, 115); color: white;')
        else:
            self.proxyButton.setText('PROXY OFF')
            self.proxyButton.setStyleSheet('background: rgb(115, 115, 115); color: white;')

    def _save_click(self):
        self._save_data()

    def _save_app_setup(self):
        data = {
            'proxy': self._proxy,
            'sound': self._sound,
            'auto': self._auto,
        }
        save_json(data, file_name='setup')

    def _app_setup(self):
        if not os.path.exists('setup.json'):
            data = {
                'proxy': False,
                'sound': False,
                'auto': False,
            }
            save_json(data, file_name='setup')
        setup = get_json_data_from_file('setup.json')
        self._sound = setup.get('sound')
        self._proxy = setup.get('proxy')
        self._auto = setup.get('auto')
        if self._proxy:
            self.proxyButton.setText('PROXY ON')
            self.proxyButton.setStyleSheet('background: rgb(115, 115, 115); color: white;')
        else:
            self.proxyButton.setText('PROXY OFF')
            self.proxyButton.setStyleSheet('background: rgb(115, 115, 115); color: white;')
        if self._sound:
            self.soundButton.setText('ЗВУК ВКЛ')
            self.soundButton.setStyleSheet('background: rgb(115, 115, 115); color: white; margin-right: 7px;')
        else:
            self.soundButton.setText('ЗВУК ВЫКЛ')
            self.soundButton.setStyleSheet('background: rgb(115, 115, 115); color: white; margin-right: 7px;')
        if self._auto:
            self.autoExcelButton.setText('АВТО ЗАПУСК EXCEL ВКЛ')
            self.autoExcelButton.setStyleSheet('background: rgb(115, 115, 115); color: white;')
        else:
            self.autoExcelButton.setText('АВТО ЗАПУСК EXCEL ВЫКЛ')
            self.autoExcelButton.setStyleSheet('background: rgb(115, 115, 115); color: white;')

    def _timer(self):
        while self._run:
            time = perf_counter() - self._start
            i_time = perf_counter() - self._i_start
            time = self.convert_sec_to_time_string(time)
            i_time = self.convert_sec_to_time_string(i_time)
            self.scanTimelabel.setText('время скана ' + time)
            self.timeLabel.setText('общее время ' + i_time)
            sleep(1)

    def _start_click(self):
        if not self._run:
            self._reset_variables_on_start()
            stopped = threading.Event()
            queue = Queue()
            p1 = threading.Thread(target=self._run_pars, args=(stopped, queue,))  # сновной процесс
            self.p_list.append(p1)
            p1.start()
            p2 = threading.Thread(target=self._pars_row_data, args=(stopped, queue,))  # обработка полученных данных
            self.p_list.append(p2)
            p2.start()
            p3 = threading.Thread(target=self._timer, daemon=True)  # run app status timer
            p3.start()
            p4 = threading.Thread(target=self._end_check, daemon=True)  # ожидание завершения p1 и p2
            p4.start()

    def _end_check(self):
        print('end func')
        for p in self.p_list:
            p.join()
        if self._sound:
            beep()
        self._run = False
        self._num_check(True)
        self.lineEdit.setReadOnly(False)
        self.infoLabel.setText('парсинг завершен')
        print_info_msg('[MainWindow][_end_check]', 'end\n')
        if self._close_app:
            self.close()

    def _reset_variables_on_start(self):
        self._run = True
        self._repack_out_data.clear()
        self._search_urls = 0
        self._parsed_num = 0
        self._row_color = 0  # 0 or 1 value permissible
        self._start_datetime = datetime.now()
        self._start = self._i_start = perf_counter()
        self.lineEdit.setReadOnly(True)
        self.infoLabel.setText('парсинг запущен')
        self.resultLabel.setText('результаты поиска (0/0)')
        self.timeLabel.setText('общее время 00:00:00')
        self.scanTimelabel.setText('время скана 00:00:00')
        self.table_widget.setRowCount(0)

    def _run_pars(self, stopped: threading.Event, queue: Queue):
        """Find a list of URLs for data parsing"""
        if not self.lineEdit.text() == '':
            if self._sound:
                beep()
            # main process here (find list of urls) >>>>>>>>>>>>>>>>>>>>>>>
            # web driver settings:
            # no sleep mode
            subprocess.call("powercfg -change -monitor-timeout-ac 0")
            subprocess.call("powercfg -change -disk-timeout-ac 0")
            subprocess.call("powercfg -change -standby-timeout-ac 0")
            # clear Downloads folder
            remove_directory('Downloads')
            os.mkdir('Downloads')
            parser = WebDriver(stream=1, headless=HEADLESS)

            # work process:
            parser.get_page('https://emex.ru')
            sleep(1)
            el = parser.driver.find_element(By.XPATH, '//button[contains(@aria-label, "Кнопка смены геолокации")]')
            print(el)
            el.click()
            sleep(1)
            el = parser.driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div/div/div/div[1]/div/div['
                                                      '2]/div/div/div[1]/div/input')
            parser.send_keys(el, 'Москва')
            sleep(1)
            el = parser.driver.find_element(By.CSS_SELECTOR, '#__next > div > div.w1uwwezs.withYellowBox.isAdaptive'
                                                             '.h1fyh9xv > div > div > div > div.isAdaptive.t1qgxfxh > '
                                                             'div > div:nth-child(3) > div > div > div.cm1waqu > div '
                                                             '> div > div.simplebar-wrapper > div.simplebar-mask > '
                                                             'div > div > div > ul > li')
            el.click()
            sleep(1)
            el = parser.driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div/div/div/div[2]/div[1]/div['
                                                      '1]/div/div/div/input')
            el.send_keys(self.lineEdit.text())
            el = parser.driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div/div/div/div[2]/div[1]/div['
                                                      '1]/div/button')
            el.click()
            el = (By.CSS_SELECTOR, '#__next > div > div.w1uwwezs.smallHeaderOnMobile.c7e6rl1 > div > div > '
                                   'div:nth-child(4) > a')
            parser.waiting_for_element(el, 10)
            els = parser.driver.find_elements(By.CSS_SELECTOR, '#__next > div > div.w1uwwezs.smallHeaderOnMobile'
                                                               '.c7e6rl1 > div > div > div:nth-child(4) > a')
            for i, el in enumerate(els):
                if not self._run:
                    break
                data = {'№ номер': [[i + 1]]}
                el_ = el.find_element(By.XPATH, './div[2]').text
                data.update({'Производитель': [[el_]]})
                el_ = el.find_element(By.XPATH, './div[3]').text
                data.update({'Номер': [[el_]]})
                el_ = el.find_element(By.XPATH, './div[4]').text
                data.update({'Описание': [[el_]]})
                el_ = el.find_element(By.XPATH, './div[5]').text
                data.update({'Цена': [[el_]]})
                queue.put(data)
                self._search_urls += 1
            # end main process here (find list of urls) >>>>>>>>>>>>>>>>>>>>>>>
        queue.join()
        stopped.set()

    def _pars_row_data(self, stopped: threading.Event, queue: Queue):
        """ Extract row data from web page and append to app table """
        while self._run and not stopped.is_set():
            if not queue.empty():
                row = queue.get()
                print(f'queue get: {row}')
                self.add_row(row)
                self._num_check()
                queue.task_done()
            sleep(row_append_timeout)

    def _stop_pars(self):
        if self._run:
            if self._sound:
                beep()
            self.infoLabel.setText('парсинг остановлен')
            self._run = False

    def closeEvent(self, event):
        print_info_msg(location='[MainWindow][closeEvent]', msg='close app click')
        self.infoLabel.setText('завершение работы')
        if not self._run:
            self._save_app_setup()
            remove_directory('Downloads')
            subprocess.call("powercfg -SETACTIVE SCHEME_BALANCED")
            event.accept()
        else:
            self._run = False
            self._close_app = True
            event.ignore()

    def _num_check(self, end=False):
        time = perf_counter() - self._start
        if not end:
            self._parsed_num += 1
            rem_time = self._get_rem_time(time)
            self.timeLeftLabel.setText(f'оставшееся время {rem_time}')
            self.resultLabel.setText(f'результаты поиска ({self._parsed_num}/{self._search_urls})')
        else:
            rem_time = '00:00:00'
        if self._parsed_num % 100 == 0 or end:
            time = self.convert_sec_to_time_string(time)
            msg = f' received data from {self._parsed_num} pages out of {self._search_urls}' \
                  f'\ndata list count: {len(self._repack_out_data)}, time: {time}, ' \
                  f'remaining time: {rem_time}'
            print_progress_msg(msg)

    def _get_rem_time(self, time):
        if self._parsed_num > 0:
            rem_time = float(time / self._parsed_num) * (self._search_urls - self._parsed_num)
            return self.convert_sec_to_time_string(rem_time)
        return 'не определено'

    def _save_data(self):
        if len(self._save_list) == 0:
            return
        d_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S").replace('/', '-').replace(' ', '_').replace(':', '-')
        f_name = f'result-{d_time}'
        for ext in self._save_list:
            if ext == 'json':
                save_json(self._repack_out_data, root_folder='result data', file_name=f_name + '.' + ext,
                          encoding=self.encoding, folder='json')
            elif ext == 'xlsx':
                save_xlsx(self._repack_out_data, file_name=f_name + '.' + ext, header_map=self.header_labels,
                          start_time=self._start_datetime, col_width_map=proj_setup.col_width_map,
                          auto_start=self._auto)

    @classmethod
    def convert_sec_to_time_string(cls, seconds):
        """ Convert time value in seconds to time data string - 00:00:00"""
        seconds = seconds % (24 * 3600)
        hour = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60
        return "%02d:%02d:%02d" % (hour, minutes, seconds)

    def __repack_row_data(self, row_data: dict, status_color):
        """ Repack row data for write to table widget. """
        data = []
        out_data = []
        for i, key in enumerate(self.header_labels):
            data_ = row_data.get(key)
            if data_:
                for j, cell in enumerate(data_):
                    if j >= len(data):
                        data.append({})
                        out_data.append({})
                    attr = self._get_cell_attr(key, status_color)
                    out_data[j].update({key: (cell, attr)})
                    data[j].update({key: cell})
        self._repack_out_data.append(out_data)
        return data

    def add_row(self, row_data_: dict):
        """ Adding row data to table widget. """
        if row_data_ is None:
            return
        self._row_color = 1 if self._row_color == 0 else 0
        color = self._r_color if self._row_color == 1 else self._l_grn_color
        status_color = self._check_row(row_data_)
        row_data_ = self.__repack_row_data(row_data_, status_color)
        for row_data in row_data_:
            row = self.table_widget.rowCount()
            row_count = self.table_widget.rowCount() + 1
            self.table_widget.setRowCount(row_count)
            for i, key in enumerate(self.header_labels):
                data = row_data.get(key)
                if data:
                    cell = data[0] if type(data) is list else data
                else:
                    cell = ''
                item = QTableWidgetItem(str(cell))
                item.setTextAlignment(Qt.AlignCenter)
                self.table_widget.setItem(row, i, item)
                self.table_widget.item(row, i).setBackground(color)
                if key == status_key and cell != '' and status_color:
                    self.table_widget.item(row, i).setBackground(status_color)

    def _get_cell_attr(self, key, status_color):
        if key == status_key:
            if status_color == self._grn_color:
                return '[color_green]'
            elif status_color == self._org_color:
                return '[color_orange]'
            elif status_color == self._blue_color:
                return '[color_blue]'
            elif status_color == self._red_color:
                return '[color_red]'
            else:
                return None
        elif key in hyper:
            return '[hyperlink]'
        else:
            return None

    def open_link(self, item: QTableWidgetItem):
        print('open link(row, col):', item.row(), item.column())
        if self.header_labels[item.column()] in hyper:
            validate = urlvalidator.URLValidator()
            try:
                data_ = None
                j = 0
                for data in self._repack_out_data:
                    for row in data:
                        if j == item.row():
                            data_ = row.get(self.header_labels[item.column()])
                        j += 1
                if data_:
                    link = data_[0][1] if len(data_[0]) > 1 else data_[0][0]
                    validate(link)
                    print_info_msg(location='open_link', msg='String is a valid URL')
                    webbrowser.open(link)
                else:
                    print_info_msg(location='open_link', msg='URL is empty')
            except ValidationError as exception:
                print_info_msg(location='open_link', msg='String is not valid URL')

    def _check_row(self, row_data):
        """ Проверка полученных данных на не соответствие требованиям. """
        if status_key is None or status_key == '':
            return None
        color = None
        status_list = ['Цена']  # check list for color choice
        for key in status_list:
            status = row_data.get(key)
            status = status[0][0] if status and len(status) > 0 else None
            # some logic for color choice here
            if status and float(status.replace(' ', '').replace('₽', '')) < 1000:
                color = self._blue_color
        return color
