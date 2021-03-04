# Python 3.7.3
import os
import time
from datetime import datetime
from concurrent.futures import (
    ThreadPoolExecutor,
    as_completed,
)


class MultiRun:

    def some_method(self, sec: int):
        name = f'method{sec}'
        print(f'{name} start. ', datetime.now())
        sleep_sec = sec / 10
        time.sleep(sleep_sec)

        if sec % 10 == 0:
            print(f'error {sec}')
            raise Exception(f'error {sec}')

        print(f'{name} end. ', datetime.now())
        return

    def multi(self, cnt: int):
        print(f'cnt: {cnt}')
        future_list = []
        with ThreadPoolExecutor() as executor:
            for i in range(1, cnt + 1):
                print('org start:', i)
                future = executor.submit(fn=self.some_method, sec=i)
                future_list.append(future)
                print('org end:', i)
            as_completed(fs=future_list)

        return


def main():
    cpu_count = os.cpu_count()
    print(f'cpu count: {cpu_count}')
    print('-- start')
    app = MultiRun()
    app.multi(cpu_count * 5 + 1)
    print('-- end')


if __name__ == '__main__':
    main()
