import random
import string

from app import db
from app.models import Urls
from flask import request
from urllib.request import HTTPError, Request, urlopen

def count_db_short_url():
    number = Urls.query.count()
    return number

def request_url(long_url):
    try:
        request = Request(long_url, None, {'User-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'})
        code = urlopen(request).code
        if (code < 400):
            return True
        else:
            return False
    except HTTPError:
        return False
    else:
        return False

def generate_random_string(length):
    random_string = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(length))
    return random_string

def check_short_url(long_url):
    lurl_query = Urls.query.filter_by(long_url=long_url).first()
    if lurl_query is None:
        for x in range(1, 9):
            short_url = generate_random_string(x)
            surl_query = Urls.query.filter_by(short_url=short_url).first()
            if surl_query is None:
                data = Urls(short_url, long_url)
                db.session.add(data)
                db.session.commit()
                return request.url_root + short_url
    else:
        return request.url_root + lurl_query.short_url