import re


class BadRequest(Exception):
    def __init__(self, response):
        self.res = response

    @staticmethod
    def check_for_err(response):
        regex = re.compile("'error_code': 400")
        match = regex.search(str(response))
        if match:
            return True