# Python 3.7.3
import time
from datetime import datetime
from concurrent.futures import (
    ThreadPoolExecutor,
    as_completed,
)


class MultiRun:

    def target_texts(self):
        return [str(i).zfill(5) for i in range(1, 33)]

    def chunked_texts(self, texts, size=5):
        # size = os.cpu_count()
        for idx in range(0, len(texts), size):
            yield texts[idx:idx + size]

    def sync(self, idx: int, is_created: bool, text: str):
        time.sleep(0.5)
        now = datetime.now().strftime('%Y-%M-%d %H:%M:%S')
        return {
            'index': idx,
            'is_created': now,
            'text': text,
        }

    def update(self, texts):
        result = {
            'all_count': len(texts),
            'list': [],
        }
        max_workers = 5
        i = 0
        for chunked_texts in self.chunked_texts(texts):
            print(chunked_texts)
            future_list = []
            with ThreadPoolExecutor(max_workers=max_workers) as executor:
                for text in chunked_texts:
                    i += 1
                    future = executor.submit(
                        fn=self.sync,
                        idx=i,
                        is_created=True,
                        text=text
                    )
                    future_list.append(future)
                futures = as_completed(fs=future_list)

            result_list = []
            for f in futures:
                result_list.append(f.result())
            result['list'] = result_list

            yield result


def main():
    app = MultiRun()
    target_texts = app.target_texts()

    result = app.update(target_texts)
    for idx, d in enumerate(result):
        print(idx, d)


if __name__ == '__main__':
    main()
