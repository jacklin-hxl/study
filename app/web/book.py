from flask import jsonify, request, make_response, flash, render_template

from app.forms.book import SearchForm

from app.lib.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.view_models.book import BookCollection, BookSingle

from . import web
from ..models.gift import Gift
from ..models.wish import Wish
from ..view_models.trade import TradeInfo


@web.route("/book/search/")
def search():
    """
        q: keyword or isbn   至少一个字符，有最大长度限制
        page: 页数    正整数，有个最大值
    """
    form = SearchForm(request.args)
    if form.validate():
        # headers = {
        #     "content-type": "application/json"
        # }

        yushu_book = YuShuBook()
        books = BookCollection()

        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)

        if isbn_or_key == "isbn":
            yushu_book.search_by_isbn(q)
        else:
            yushu_book.search_by_keyword(q, page)

        books.fill(yushu_book, q)
        # res = make_response(json.dumps(books, default=lambda o: o.__dict__))
        # res.headers = headers
        # return res
    else:
        flash("搜索的关键子不符合要求，请重新搜索")
        # return jsonify({"msg": "数据校验失败"})
    return render_template("search_result.html", books=books)


@web.route("/book/<isbn>/detail")
def book_detail(isbn):
    if is_isbn_or_key(isbn) == "isbn":
        has_in_wishes = Wish.in_wishes(isbn)
        has_in_gifts = Gift.in_gifts(isbn)

        book = BookSingle(YuShuBook().search_by_isbn(isbn).books)

        trade_wish = TradeInfo(Wish.query.filter_by(isbn=isbn, launched=False, status=1).all())
        trade_gift = TradeInfo(Gift.query.filter_by(isbn=isbn, launched=False, status=1).all())

        return render_template("book_detail.html", book=book, wishes=trade_wish, gifts=trade_gift,
                               has_in_gifts=has_in_gifts, has_in_wishes=has_in_wishes)


@web.route("/", endpoint="index")
@web.route("/recent/")
def recent():
    recent_list = Gift.recent()
    gifts = []
    for gift in recent_list:
        single = BookSingle(YuShuBook().search_by_isbn(gift["isbn"]).books)
        gifts.append(single)

    return render_template("index.html", recent=gifts)
