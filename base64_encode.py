# Python 3.7.3
import base64


def to_b64(text: str) -> str:
    return base64.b64encode(text.encode()).decode()


def main():
    # 羅生門の冒頭
    text = (
        'ある日の暮方の事である。一人の下人げにんが、'
        '羅生門らしょうもんの下で雨やみを待っていた。'
        '広い門の下には、この男のほかに誰もいない。'
        'ただ、所々丹塗にぬりの剥はげた、大きな円柱まるばしらに、'
        '蟋蟀きりぎりすが一匹とまっている。'
    )

    actual = to_b64(text)
    assert actual == (
        '44GC44KL5pel44Gu5pqu5pa544Gu5LqL44Gn44GC44KL44CC5L'
        'iA5Lq644Gu5LiL5Lq644GS44Gr44KT44GM44CB576F55Sf6ZaA'
        '44KJ44GX44KH44GG44KC44KT44Gu5LiL44Gn6Zuo44KE44G/44'
        'KS5b6F44Gj44Gm44GE44Gf44CC5bqD44GE6ZaA44Gu5LiL44Gr'
        '44Gv44CB44GT44Gu55S344Gu44G744GL44Gr6Kqw44KC44GE44'
        'Gq44GE44CC44Gf44Gg44CB5omA44CF5Li55aGX44Gr44Gs44KK'
        '44Gu5Yml44Gv44GS44Gf44CB5aSn44GN44Gq5YaG5p+x44G+44'
        'KL44Gw44GX44KJ44Gr44CB6J+L6J+A44GN44KK44GO44KK44GZ'
        '44GM5LiA5Yy544Go44G+44Gj44Gm44GE44KL44CC'
    )


if __name__ == '__main__':
    main()
