# Python 3.7.3
from pathlib import Path
import base64
import os


def calc(filename):
    filepath = Path(__file__).parent / filename
    filesize = os.path.getsize(filepath)

    with open(filepath, 'r') as f:
        data = '\n'.join(f.read().splitlines())

    encoded = base64.b64encode(data.encode()).decode()
    length = len(encoded)

    msg = '\n'.join([
        f'[{filename}]',
        f'filesize: {filesize}',
        f'encoded length: {length}',
        f'original: {data}',
        '----',
    ])
    print(msg)


def main():
    calc('data1.txt')
    calc('data2.txt')
    calc('data3.txt')
    calc('data4.txt')
    calc('data5.txt')
    calc('data6.txt')


if __name__ == '__main__':
    main()
