from httper import HTTP


class YuShuBook:
    """
    isbn搜索： http://t.talelin.com/v2/book/isbn/{isbn}
    关键字搜索： http://t.talelin.com/v2/book/search?q={}&start={}&count={}
    豆瓣api： https://api.douban.com/v2/book
    """

    isbn_url = "http://t.talelin.com/v2/book/isbn/{}"
    keyword_url = "http://t.talelin.com/v2/book/search?q={}&start={}&count={}"

    @classmethod
    def search_by_isbn(cls, isbn):
        result = HTTP.get(url=cls.isbn_url.format(isbn))
        return result

    @classmethod
    def search_by_keyword(cls, keyword, count=15, start=0):
        result = HTTP.get(url=cls.keyword_url.format(keyword, count, start))
        return result