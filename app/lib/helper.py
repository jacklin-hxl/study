

def is_isbn_or_key(word):
    """
    判断搜索的字段是类型，isbn or key
    :param word: 请求的关键字，isbn or key
    :return: 关键字类型 ，isbn or key
    """

    isbn_or_key = "key"
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    if '-' in word and len(word.replace('-', '')) == 10 and word.replace('-', '').isdigit():
        isbn_or_key = 'isbn'

    return isbn_or_key