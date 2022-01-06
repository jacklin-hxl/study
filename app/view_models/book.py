


"""
前端通过 isbn 搜索返回数据结构：
    {
        "books": [{
            "author": [],
            "image": "https://img3.doubanio.com/lpic/s1635291.jpg",
            "pages": null,
            "price": null,
            "publisher": null,
            "summary": null,
            "title": "郭敬明音乐小说迷藏(CD)",
        }],
        "total": 1,
        "keyword": 9787884774340
    }

通过 keyword 搜索返回数据结构
    {
        "books": [{
            "author": [],
            "image": "https://img3.doubanio.com/lpic/s1635291.jpg",
            "pages": null,
            "price": null,
            "publisher": null,
            "summary": null,
            "title": "郭敬明音乐小说迷藏(CD)",
        },
        ...
        ],
        "total": len(books),
        "keyword": "郭敬明“
    }
"""


class BookSingle():

    def __init__(self, book):
        self.title = book.get("title", '')
        self.publisher = book.get("publisher", '')
        self.pages = book.get("pages", '')
        self.price = book.get("price", '')
        self.summary = book.get("summary", '')
        self.image = book.get("image", '')
        self.author = book.get("author", '')
        self.isbn = book.get("isbn", '')
        self.pubdate = book.get('pubdate', '')
        self.binding = book.get("binding", '')

    @property
    def intros(self):
        """
        鲁迅,老舍/出版社/¥35.00
        """
        res = ','.join(self.author)
        intro = filter(lambda x: True if x else False, [res, self.publisher, self.price])
        return ' / '.join(intro)



class BookCollection():

    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = ''

    def fill(self, yushu_book, keyword):
        self.total = yushu_book.total
        self.books = [BookSingle(book) for book in yushu_book.books]
        self.keyword = keyword

