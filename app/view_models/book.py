
class BookViewModel:
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

    @classmethod
    def data_single(cls, data, keyword):
        """
        单个数据
        :param data: 原始数据内容
        :param keyword: 搜索值
        :return: {}
        """

        return_data = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }

        if data:
            return_data['books'] = [cls.cut_book_data(data)]
            return_data['total'] = 1

        return return_data

    @classmethod
    def data_collection(cls, data, keyword):
        return_data = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }

        if data["books"]:
            return_data['books'] = [cls.cut_book_data(book) for book in data["books"]]
            return_data['total'] = data["total"]

        return return_data

    @classmethod
    def cut_book_data(cls, data):
        book = {
            'title': data["title"],
            'publisher': data["publisher"],
            'pages': data.get("page") or '',
            'price': data['price'],
            'summary': data["summary"] or '',
            'image': data["image"],
            "author": data['author']
        }

        return book


