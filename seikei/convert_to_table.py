# Python 3.7.3
from pathlib import Path
import unicodedata
import argparse


TITLE_SEPARATOR = ','
BODY_SEPARATOR = ','


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="please set me", type=str)
    parser.add_argument("--title-separator", type=str, default=TITLE_SEPARATOR)
    parser.add_argument("--body-separator", type=str, default=BODY_SEPARATOR)

    args = parser.parse_args()
    return(args)


class MarkdownTableConverter:

    def __init__(self, title_separator=TITLE_SEPARATOR, body_separator=BODY_SEPARATOR):
        self.title_separator = title_separator
        self.body_separator = body_separator

    def convert(self, filename: str):
        titles, rows = self._read_data(filename)

        data = []
        max_length_data = {}
        for row in rows:
            if not row:
                continue

            splited_row = row.split(self.body_separator)
            one = {}
            for idx, title in enumerate(titles):
                content = splited_row[idx]
                one[title] = content
                width = self._calc_text_width(content)
                if title not in max_length_data:
                    max_length_data[title] = width
                elif max_length_data[title] < width:
                    max_length_data[title] = width
            data.append(one)
        self._show(max_length_data, data)

    def _read_data(self, filename: str):
        filepath = Path(__file__).parent / filename
        with open(filepath, 'r') as f:
            data = f.read()

        s = data.split('\n', 1)
        return s[0].split(self.title_separator), s[1].split('\n')

    def _calc_text_width(self, text: str) -> int:
        text_length = len(text)
        w = 0
        for i in range(text_length):
            res = unicodedata.east_asian_width(text[i])
            if res in ['F', 'W', 'A']:
                w += 2
            else:
                w += 1
        return w

    def _make_text(self, text, length):
        width = self._calc_text_width(text)
        fill_num = length - width
        return text + ' ' * fill_num

    def _show(self, length_data, data, separator='|'):
        none_line = []
        one = []
        for key, val in length_data.items():
            none_line.append(separator)
            none_line.append('-' * val)
            one.append(separator)
            one.append(self._make_text(key, val))

        none_line.append(separator)
        one.append(separator)
        print(''.join(one))
        print(''.join(none_line))

        for d in data:
            one = []
            for key, val in d.items():
                one.append(separator)
                one.append(self._make_text(val, length_data[key]))
            one.append(separator)
            print(''.join(one))


if __name__ == '__main__':
    """
    usage1: only filename
    $ python convert_to_table.py sample.txt

    usage2: filename and title_separator
    $ python convert_to_table.py sample.txt --title-separator=,

    usage3: all
    $ python convert_to_table.py sample.txt --title-separator=, --body-separator=,

    Example
    >>> python for_markdown_table.py data1.txt
    |code          |name          |value   |
    |--------------|--------------|--------|
    |kokumin_nenkin|国民年金保険料|10000   |
    |shokuhi01     |1月の食費     |10000   |
    |shokuhi02     |2月の食費     |20000   |
    |shokuhi03     |3月の食費     |30000   |
    |shokuhi04     |4月の食費     |40000   |
    |shokuhi05     |5月の食費     |50000   |
    |shokuhi06     |6月の食費     |60000   |
    |shokuhi07     |7月の食費     |70000   |
    |shokuhi08     |8月の食費     |80000   |
    |shokuhi09     |9月の食費     |90000   |
    |shokuhi10     |10月の食費    |100000  |
    |shokuhi11     |11月の食費    |110000  |
    |shokuhi12     |12月の食費    |120000  |
    |car_tax       |自動車税      |40000   |
    |適当コード    |適当コード名  |適当な値|
    """
    args = get_args()
    app = MarkdownTableConverter(
        title_separator=args.title_separator,
        body_separator=args.body_separator,
    )
    app.convert(args.filename)
