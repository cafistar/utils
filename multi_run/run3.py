# Python 3.7.3
from time import time, strftime, sleep, gmtime
from itertools import islice
from concurrent.futures import (
    ThreadPoolExecutor,
    as_completed,
)
# https://stackoverflow.com/questions/48263704/threadpoolexecutor-how-to-limit-the-queue-maxsize#answer-49622149


def nap(id, nap_length):
    t = nap_length/10
    sleep(t)
    return nap_length


def chunked_iterable(iterable, chunk_size):
    it = iter(iterable)
    while True:
        chunk = tuple(islice(it, chunk_size))
        if not chunk:
            break
        yield chunk


if __name__ == '__main__':
    startTime = time()

    range_size = 50
    chunk_size = 5
    nap_time = 2

    # Iterate in chunks.
    # This consumes less memory and kicks back initial results sooner.
    for chunk in chunked_iterable(range(range_size), chunk_size):

        with ThreadPoolExecutor(max_workers=chunk_size) as pool_executor:
            pool = {}
            for i in chunk:
                function_call = pool_executor.submit(nap, i, nap_time)
                pool[function_call] = i

            for completed_function in as_completed(pool):
                result = completed_function.result()
                i = pool[completed_function]

                print('{} completed @ {} and slept for {}'.format(
                    str(i + 1).zfill(4),
                    strftime("%H:%M:%S", gmtime()),
                    result))

    print('==--- Script took {} seconds. ---=='.format(round(time() - startTime)))
