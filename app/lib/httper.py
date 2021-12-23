import requests

class HTTP:

    @staticmethod # 和类/对象 都没有关系
    def get(url, return_json=True):
        """
        通过外部api获取书籍信息
        :param url:
        :param return_json:
        :return:
        """

        r = requests.get(url)

        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text


