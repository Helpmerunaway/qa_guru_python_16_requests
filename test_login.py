import allure
import requests
import selene

browser.config.base_url = WEB_URL

#TODO: Copy module from lection


def test_login_with_cookie():
	"""Sucessful auth"""
	with step('Get cookie by api and set it to browser'):
		authorization_cookie = requests.post(
			url=API_URL + '/login',
			params={'Email': LOGIN, 'Password': PASSWORD},
			headers={'content-type': 'application/x-www-form-urlencoded; charset=UTF-8'},
			allow_redirects=False
		)
		assert authorization_cookie.status_code == 200
		authorization_cookie = authorization_cookie.cookies.get("NOPCOMMERCE.AUTH")
		print(authorization_cookie)

		with step('Open minimal content, because cookie can be set when site is opened'):
			browser.open('/Themes/DefaultClean/')