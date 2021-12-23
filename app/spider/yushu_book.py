from app.lib.httper import HTTP
from flask import current_app


class YuShuBook:
    """
    isbn搜索： http://t.talelin.com/v2/book/isbn/{isbn}
    关键字搜索： http://t.talelin.com/v2/book/search?q={}&start={}&count={}
    豆瓣api： https://api.douban.com/v2/book
    """
    pageCount = 15
    isbn_url = "http://t.talelin.com/v2/book/isbn/{}"
    keyword_url = "http://t.talelin.com/v2/book/search?q={}&start={}&count={}"

    @classmethod
    def search_by_isbn(cls, isbn):
        result = HTTP.get(url=cls.isbn_url.format(isbn))
        return result

    @classmethod
    def search_by_keyword(cls, keyword, page):
        # page = 1 , 1 * 0  ;  page = 2 -> 1 * 15 + 1
        result = HTTP.get(url=cls.keyword_url.format(keyword, cls.solution_start(page),
                                                     current_app.config["PAGE_COUNT"]))
        return result

    @staticmethod
    def solution_start(page):
        return (page - 1) * current_app.config["PAGE_COUNT"]