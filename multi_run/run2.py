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
        print(f'method {sec} start. ', datetime.now())

        s = str(sec).zfill(4)

        sleep_sec = sec / 10
        time.sleep(sleep_sec)

        if sec % 10 == 0:
            raise Exception('error')

        print(f'method {sec} finish. ', datetime.now())
        return s

    def multi(self, cnt: int):
        print(f'cnt: {cnt}')
        future_list = []
        with ThreadPoolExecutor() as executor:
            for i in range(1, cnt + 1):
                print('org start:', i)
                future = executor.submit(fn=self.some_method, sec=i)
                future_list.append(future)
                print('org end:', i)
            futures = as_completed(fs=future_list)

        print('-- futures')
        for f in futures:
            try:
                r = f.result()
                print(r)
            except Exception as e:
                print(e)
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
