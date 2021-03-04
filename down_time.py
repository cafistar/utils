# Python 3.7.3
import sys
from decimal import Decimal


def calc_integer_remainder(all_num: int, division: int):
    if all_num == 0:
        return 0, 0
    num = Decimal(str(all_num)) // Decimal(str(division))
    reminder = all_num - num * division
    return num, reminder


def calc_down_time(rate: str) -> str:
    """
    稼働率を与えると年間(365日)のダウンタイムを返す
    """
    down_per = (Decimal('100') - Decimal(rate)) / Decimal('100')

    all_sec = Decimal(str(60 * 60 * 24 * 365))
    down_sec = all_sec * down_per

    # 日数
    down_days, nokori = calc_integer_remainder(down_sec, 86400)

    # 時間
    down_hours, nokori = calc_integer_remainder(nokori, 3600)

    # 分
    down_minuts, nokori = calc_integer_remainder(nokori, 60)

    # print(f'稼働率: {rate}%')
    # print(f'ダウン: {down_days}日 {down_hours}時間 {down_minuts}分 {nokori}秒 ({down_sec}秒)')
    return (
        f'稼働率: {rate}%\n'
        f'ダウン: {down_days}日 {down_hours}時間 {down_minuts}分 {nokori}秒 ({down_sec}秒)'
    )


def test_1():
    actual = calc_down_time('0')
    assert actual == (
        '稼働率: 0%\n'
        'ダウン: 365日 0時間 0分 0秒 (31536000秒)'
    )


def test_2():
    actual = calc_down_time('50')
    assert actual == (
        '稼働率: 50%\n'
        'ダウン: 182日 12時間 0分 0秒 (15768000.0秒)'
    )


def test_3():
    actual = calc_down_time('100')
    assert actual == (
        '稼働率: 100%\n'
        'ダウン: 0日 0時間 0分 0秒 (0秒)'
    )


def main():
    try:
        per = sys.argv[1]
    except IndexError:
        print('稼働率を与えてください.\n例) $ python down_time.py 99.9')
        exit(0)

    result = calc_down_time(per)
    print(result)

    test_1()
    test_2()
    test_3()


if __name__ == '__main__':
    main()
