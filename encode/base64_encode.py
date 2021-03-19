import base64


def main():
    text = (
        'ある日の暮方の事である。一人の下人げにんが、'
        '羅生門らしょうもんの下で雨やみを待っていた。'
        '広い門の下には、この男のほかに誰もいない。'
        'ただ、所々丹塗にぬりの剥はげた、大きな円柱まるばしらに、'
        '蟋蟀きりぎりすが一匹とまっている。'
    )

    print('---- plain text')
    print(text)

    print('---- base64.b64encode(text.encode()).decode()')
    print(base64.b64encode(text.encode()).decode())


if __name__ == '__main__':
    main()
