from flask import jsonify, request
from app.forms.book import SearchForm

from helper import is_isbn_or_key
from yushu_book import YuShuBook

from . import web

@web.route("/book/search/")
def search():
    """
        q: keyword or isbn   至少一个字符，有最大长度限制
        page: 页数    正整数，有个最大值
    """

    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == "isbn":
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q, page)

        return jsonify(result)
    else:
        return jsonify({"msg": "数据校验失败"})
