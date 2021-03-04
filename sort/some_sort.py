# Python 3.7.3
from copy import deepcopy


class SomeSort:

    data = [
        {
            'id': '1',
            'created_at': '2021/02/01 00:00:00',
            # 'text': None,
        },
        {
            'id': '2',
            'created_at': '2021/02/01 00:00:00',
            'text': 'abc',
        },
        {
            'id': '3',
            'created_at': '2021/02/01 00:00:00',
            'text': '',
        },
        {
            'id': '4',
            'created_at': '2021/02/01 00:00:00',
            'text': None,
        },
        {
            'id': '5',
            'created_at': '2021/02/01 00:00:01',
            'text': None,
        },
        {
            'id': '6',
            'created_at': '2021/02/01 00:00:01',
            'text': 'abc',
        },
    ]

    def none_is_head(self):
        """
        text: None を先頭にasc
        created_at: desc
        """
        data = deepcopy(self.data)
        data.sort(key=lambda x: x['created_at'], reverse=True)

        # Noneを先頭に(key の第1要素に bool, 第2要素に text)
        data.sort(key=lambda x: (x.get('text') is not None, x.get('text')))
        return data

    def none_is_foot(self):
        """
        text: None を末尾にasc
        created_at: desc
        """
        data = deepcopy(self.data)
        data.sort(key=lambda x: x['created_at'], reverse=True)

        # Noneを最後に(key の第1要素に bool, 第2要素に text)
        data.sort(key=lambda x: (x.get('text') is None, x.get('text')))
        return data


def test_none_is_head():
    one = SomeSort()
    actual = one.none_is_head()
    assert actual == [
        {'id': '5', 'created_at': '2021/02/01 00:00:01', 'text': None},
        {'id': '1', 'created_at': '2021/02/01 00:00:00'},
        {'id': '4', 'created_at': '2021/02/01 00:00:00', 'text': None},
        {'id': '3', 'created_at': '2021/02/01 00:00:00', 'text': ''},
        {'id': '6', 'created_at': '2021/02/01 00:00:01', 'text': 'abc'},
        {'id': '2', 'created_at': '2021/02/01 00:00:00', 'text': 'abc'},
    ]


def test_none_is_foot():
    one = SomeSort()
    actual = one.none_is_foot()
    assert actual == [
        {'id': '3', 'created_at': '2021/02/01 00:00:00', 'text': ''},
        {'id': '6', 'created_at': '2021/02/01 00:00:01', 'text': 'abc'},
        {'id': '2', 'created_at': '2021/02/01 00:00:00', 'text': 'abc'},
        {'id': '5', 'created_at': '2021/02/01 00:00:01', 'text': None},
        {'id': '1', 'created_at': '2021/02/01 00:00:00'},
        {'id': '4', 'created_at': '2021/02/01 00:00:00', 'text': None},
    ]


def main():
    test_none_is_head()
    test_none_is_foot()


if __name__ == '__main__':
    main()
