# [스마일게이트] url-shortener(Github)

> * python3, Mysql

## Assignment
#### URL 단축 (URL shortening) 서비스 개발

- [x] URL 입력 폼 제공
- [x] 단축 후 결과 출력
- [x] 동일한 URL을 입력 할 경우 항상 동일한 shortening 결과 값 출력
- [x] shortening 의 결과 값은 8문자 이내로 생성(1~8문자 생성)
- [x] 브라우저에서 shortening URL을 입력하면 원래 URL로 리다이렉트
- [x] 도메인은 localhost로 처리 
- [x] 웹 페이지 개발
- [x] URL 입력시 정상적인 URL이 아니면 잘못된 URL 이라고 표시
- [x] 원래 URL이 404 코드를 받을 경우 사용자에게 표시
- [x] OG Tag 적용하기

## [DEMO 확인하기](http://13.125.81.144:5000/)
## ScreenShot
![Screenshot1](https://dl.dropbox.com/s/nfed4l5l68p2pg7/screenshot1.png)
![Screenshot2](https://dl.dropbox.com/s/yyybkgebmrlry78/screenshot2.png)
![Screenshot3](https://dl.dropbox.com/s/ffw2dn4be99dl5l/screenshot3.png)
## Code
### utils.py
* **count_db_short_url** : DB에 있는 단축 url의 개수를 출력
* **request_url** :  입력 받은 url이 정상적으로 작동하는 링크인지 확인.
* **generate\_random\_string** : 단축 url을 만들기 위해서 입력 받은 길이만큼 랜덤하게 string을 생성.
	* string.ascii\_letters와 string\_digits를 사용해 ascii코드의 대문자, 소문자, 숫자를 랜덤하게 선택하여 문자열에 join한다.
* **check_short_url**
	1. 입력받은 URL이 DB에 저장되어 있는지 확인
		* 저장되어 있다면 DB에 저장된 단축 Url을 리턴
	2. 저장되어 있지 않다면 generate\_random\_string을 이용하여 임의의 문자열을 생성
		* 생성한 string이 DB에 존재한다면, 길이를 하나 더 늘려 다시 임의의 문자열을 생성
	3. String이 DB에 존재하지 않는다면 DB에 값을 저장하고, Url을 Retrun
### form.py
* **GetLinkForm** : input form에서 URL을 가져오고, URL을 확인
### models.py
* **URls** : DB 테이블 urls는 short_url과 long_url 컬럼을 가짐
### views.py
* **home** : 메인 페이지
* **redirect_to_main_url** : short url의 original url로 리다이렉트
* **page_not_found** : 잘못된 페이지로 접근할 경우 출력되는 페이지

## Requirements
* Python 모듈 : pymysql, markupsafe
* Flask 플러그인 : Flask, flask-sqlalchemy, Flask-WTF
```powershell
pip3 install -r requirements.txt
```

## ToDo
- [ ] 링크의 클릭 횟수 표시하기
- [ ] 메인 페이지에 단축 url 테이블 보여주기
- [ ] url 단축 결과를 보여주면서, url의 스크린샷도 함께 보여주기

## Configuration
#### 1. MySQL 데이터베이스 설정
* Mysql Login
```powershell
mysql -u root
```
* smilegate 데이터베이스 생성하기
```sql
CREATE DATABASE smilegate;
```
* 데이터베이스 사용자를 생성하고 권한 부여하기
```sql
GRANT ALL ON smilegate.* TO userid@localhost IDENTIFIED BY 'userpw';
```
#### 2. config.py 파일 설정하기
* 사용자 수정하기
```python
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://userid:userpw@localhost/smilegate'
```
#### 3. manage.py 실행하기
```powershell
#cd /your_path/url_shortener/
python3 database.py
```
## Run
```powershell
#cd /your_path/url_shortener/
python3 run.py
```
>  \* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
