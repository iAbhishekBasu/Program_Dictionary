import bs4
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

BASE_URL = 'https://codedrills.io'


def to_timedelta(time_str: str) -> timedelta:
    t = datetime.strptime(time_str, '%H:%M:%S')
    return timedelta(hours=t.hour, minutes=t.minute, seconds=t.second)


class TableScraper:
    BASE_URL = 'https://codedrills.io'

    def __init__(self, html_content: str):
        self.soup = BeautifulSoup(html_content, features="html.parser")
        table = self.soup.find('table')
        self.table_head = table.find('thead')
        self.table_body = table.find('tbody')
        self.header_data = self.scrape_header()
        self.headers = self.header_data['keys']

    def scrape(self):
        return {'header_data': self.header_data, 'body': self.scrape_body()}

    def scrape_body(self):
        body = self.table_body
        result = []
        for row in body.find_all('tr'):
            result.append(self.scrape_body_row(row))
        return result

    def _process_rank(self, data: bs4.element.Tag) -> int:
        return int(data.text.strip())

    def _process_team(self, data: bs4.element.Tag) -> dict:
        result = {'name': data.text.strip()}
        anchor = data.findChild('a')
        if anchor:
            result['link'] = self.BASE_URL + anchor.get('href', '')
        return result

    def _process_org(self, data: bs4.element.Tag) -> str:
        return data.text.strip()

    def _process_score(self, data: bs4.element.Tag) -> dict:
        data = data.findChild('span')
        solved_span, time_span = data.find_all('span')
        result = {'solved': int(solved_span.text.strip())}
        total_time = to_timedelta(time_span.text.strip())
        result['total_time'] = total_time.seconds
        return result

    def _process_problem(self, data: bs4.element.Tag) -> dict:
        _data = data.findChild('a')
        _success = 1 if _data else 0
        if not _data:
            _data = data.findChild('span').findChild('span')
        if not _data:
            return {}
        result = {}
        tries_span, time_span = _data.find_all('span')
        if '(' in tries_span.text.strip():
            _tries = int(tries_span.text.strip().split('(')[-1][:-1])
        else:
            _tries = 1
        _time = to_timedelta(time_span.text.strip())
        return {
            'tries': _tries,
            'time': _time.seconds,
            'submission': self.BASE_URL + _data.get('href') if _data.get('href') else '',
            'success': _success,
        }

    def scrape_body_row(self, row: bs4.element.Tag):
        result = {}
        processing_functions = {
            0: self._process_rank,
            1: self._process_team,
            2: self._process_org,
            3: self._process_score,
            4: self._process_problem,
        }
        for idx, data in enumerate(row.find_all('td')):
            _idx = min(max(processing_functions.keys()), idx)
            result[self.headers[idx]] = processing_functions[_idx](data)
        return result

    def scrape_header(self) -> dict:
        headers = self.table_head
        keys = [i.text.strip() for i in headers.find_all('th')]
        problems = self.get_problem_details(headers)
        return {
            'keys': keys,
            'problems': problems
        }

    def get_problem_details(self, headers: bs4.element.Tag) -> dict:
        data = {}
        for header in headers.find_all('th'):
            key, val = self._get_problem_details(header=header)
            if not key:
                continue
            data[key] = val
        return data

    def _get_problem_details(self, header: bs4.element.Tag) -> tuple:
        anchor_tag = header.findChild('a')

        if not anchor_tag or not anchor_tag.get_attribute_list('href')[0]:
            return None, None
        link = BASE_URL + anchor_tag.get('href', '')
        data = {
            'link': link,
        }
        return header.text.strip(), data

# def scrape(html_content: str) -> dict:
#     soup = BeautifulSoup(html_content, features="html.parser")
#     table = soup.find('table')
#     header_data = scrape_header(soup)
#     return {}

#
# def scrape_header(soup: BeautifulSoup) -> dict:
#     table = soup.find('table')
#     header = []
#     headers = table.find('thead')
#     keys = [i.text.strip() for i in headers.find_all('th')]
#     problems = get_problem_details(headers)
#     return {
#         'keys': keys,
#         'problems': problems
#     }
#
#
# def get_problem_details(headers: bs4.element.Tag) -> dict:
#     data = {}
#     for header in headers.find_all('th'):
#         key, val = _get_problem_details(header=header)
#         if not key:
#             continue
#         data[key] = val
#     return data
#
#
# def _get_problem_details(header: bs4.element.Tag) -> tuple:
#     anchor_tag = header.findChild('a')
#
#     if not anchor_tag or not anchor_tag.get_attribute_list('href')[0]:
#         return None, None
#     link = BASE_URL + anchor_tag.get('href', '')
#     data = {
#         'link': link,
#     }
#     return header.text.strip(), data