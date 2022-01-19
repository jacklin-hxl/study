from app.lib.httper import HTTP
from flask import current_app

# 伪面向对象，都是静态方法，没有保存对象的相关信息，都是直接返回数据
# 一个类或者对象需要有描述自身特征的数据
# class YuShuBook:
#     """
#     isbn搜索： http://t.talelin.com/v2/book/isbn/{isbn}
#     关键字搜索： http://t.talelin.com/v2/book/search?q={}&start={}&count={}
#     豆瓣api： https://api.douban.com/v2/book
#     """
#     pageCount = 15
#     isbn_url = "http://t.talelin.com/v2/book/isbn/{}"
#     keyword_url = "http://t.talelin.com/v2/book/search?q={}&start={}&count={}"
#
#     @classmethod
#     def search_by_isbn(cls, isbn):
#         result = HTTP.get(url=cls.isbn_url.format(isbn))
#         return result
#
#     @classmethod
#     def search_by_keyword(cls, keyword, page):
#         # page = 1 , 1 * 0  ;  page = 2 -> 1 * 15 + 1
#         result = HTTP.get(url=cls.keyword_url.format(keyword, cls.solution_start(page),
#                                                      current_app.config["PAGE_COUNT"]))
#         return result
#
#     @staticmethod
#     def solution_start(page):
#         return (page - 1) * current_app.config["PAGE_COUNT"]

# 重构后
class YuShuBook:
    """
    isbn搜索： http://t.talelin.com/v2/book/isbn/{isbn}
    关键字搜索： http://t.talelin.com/v2/book/search?q={}&start={}&count={}
    豆瓣api： https://api.douban.com/v2/book
    """
    isbn_url = "http://t.talelin.com/v2/book/isbn/{}"
    keyword_url = "http://t.talelin.com/v2/book/search?q={}&start={}&count={}"

    def __init__(self):
        self.total = 0
        self.books = []

    def search_by_isbn(self, isbn):
        result = HTTP.get(url=self.isbn_url.format(isbn))
        self.__fill_single(data=result)
        return self

    def search_by_keyword(self, keyword, page):
        # page = 1 , 1 * 0  ;  page = 2 -> 1 * 15 + 1
        result = HTTP.get(url=self.keyword_url.format(keyword, self.solution_start(page),
                                                     current_app.config["PAGE_COUNT"]))
        self.__fill_collection(data=result)
        return self

    def __fill_single(self, data):
        if data:
            self.total = 1
            self.books.append(data)

    def __fill_collection(self, data):
        if data:
            self.total = data["total"]
            self.books = data["books"]

    @property
    def first(self):
        return self.books[0]

    @staticmethod
    def solution_start(page):
        return (page - 1) * current_app.config["PAGE_COUNT"]
