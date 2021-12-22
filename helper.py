

def is_isbn_or_key(word):
    """
    :param word: 请求的关键字
    :return: 关键字类型
    """

    isbn_or_key = "key"
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    if '-' in word and len(word.replace('-', '')) == 10 and word.replace('-', '').isdigit():
        isbn_or_key = 'isbn'

    return isbn_or_key