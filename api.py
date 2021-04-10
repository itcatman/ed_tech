import requests

class Api():
    def get_req(self, url):
        return requests.get(url)

    def post_req(self, url, data):
        return requests.post(url, data)

    def del_req(self, url, target):
        return requests.delete(url, params=target)
