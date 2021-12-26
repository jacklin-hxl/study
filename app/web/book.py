from flask import jsonify, request
from app.forms.book import SearchForm

from app.lib.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.view_models.book import BookViewModel

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
            data = YuShuBook.search_by_isbn(q)
            result = BookViewModel.data_single(data, q)
        else:
            data = YuShuBook.search_by_keyword(q, page)
            result = BookViewModel.data_collection(data, q)

        return jsonify(result)
    else:
        return jsonify({"msg": "数据校验失败"})
