from app.spider.yushu_book import YuShuBook
from app.view_models.book import BookSingle


class Inventory:
    """
    [
        {
        'book': book,
        'count': count
        }
    ]

    iter_detail : [{"isbn":111, "count": count}]

    """

    def __init__(self, iter_detail):
        self.__iter_detail = iter_detail
        self.details = [i for i in self.__generator_imple()]

    def __iter__(self):
        """
        generator
        """
        return self.__generator_imple()

    def __generator_imple(self):
        for i in self.__iter_detail:
            book = self.__get_book(dict(i).get("isbn"))
            detail = {"book": book, "count": i.get("count"), "id": i.get("id")}
            yield detail
    
    def __get_book(self, isbn):
        if isbn:
            yushu = YuShuBook().search_by_isbn(isbn)
            return BookSingle(yushu.first)
        else:
            raise Exception("need isbn")



