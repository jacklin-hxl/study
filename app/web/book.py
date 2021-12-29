from flask import jsonify, request, make_response
from app.forms.book import SearchForm
import json

from app.lib.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.view_models.book import BookCollection

from . import web

@web.route("/book/search/")
def search():
    """
        q: keyword or isbn   至少一个字符，有最大长度限制
        page: 页数    正整数，有个最大值
    """
    form = SearchForm(request.args)
    yushu_book = YuShuBook()
    books = BookCollection()
    if form.validate():
        headers = {
            "content-type": "application/json"
        }

        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)

        if isbn_or_key == "isbn":
            yushu_book.search_by_isbn(q)
        else:
            yushu_book.search_by_keyword(q, page)

        books.fill(yushu_book, q)
        res = make_response(json.dumps(books, default=lambda o: o.__dict__))
        res.headers = headers
        return res
    else:
        return jsonify({"msg": "数据校验失败"})
