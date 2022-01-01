


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
        self.title = book["title"],
        self.publisher = book["publisher"],
        self.pages = book.get("page") or '',
        self.pric = book['price'],
        self.summary = book["summary"] or '',
        self.image = book["image"],
        self.author = book['author']


class BookCollection():

    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = ''

    def fill(self, yushu_book, keyword):
        self.total = yushu_book.total
        self.books = [BookSingle(book) for book in yushu_book.books]
        self.keyword = keyword

