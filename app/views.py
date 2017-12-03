from app import app
from app.form import GetLinkForm
from app.models import Urls
from app.utils import count_db_short_url, check_short_url, request_url
from flask import abort, flash, jsonify, redirect, render_template, request, url_for

@app.route('/', methods=['GET', 'POST'])
def home():
    number = count_db_short_url()
    if request.method == 'POST':
        form = GetLinkForm(request.form)
        if form.validate():
            long_url = form.long_url.data
            checker = request_url(long_url)
            if checker is True:
                short_url = check_short_url(long_url)
                return render_template('index.html', form=form,
                                       short_url=short_url, number=number)
            else:
                flash("작동하지 않는 URL 입니다.")
                return render_template('index.html', form=form, number=number)
        else:
            flash("정확한 URL을 입력해 주세요")
            return render_template('index.html', form=form, number=number)
    else:
        return render_template('index.html', form=GetLinkForm(), number=number)

@app.route('/<string:short_url>')
def redirect_to_main_url(short_url):
    surl_query = Urls.query.filter_by(short_url=short_url).first()
    if surl_query is None:
        abort(404)
    else:
        return redirect(surl_query.long_url)

@app.errorhandler(404)
def page_not_found(error):
    number = count_db_short_url()
    return render_template('404.html', number=number), 404
