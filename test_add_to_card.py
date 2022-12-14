from uuid import uuid4

import requests

from utils.sessions import demoqa
from dotenv import load_dotenv
import os
load_dotenv()

def test():
	print(uuid4())


def test_add_to_cart_unauthorized():
	response = demoqa().post('/addproducttocart/catalog/31/1/1'
	                         , cookies={'Nop.customer': '890413c2-f100-4e74-9a60-cbe5676f3cbb;'}
	                         )
	assert response.status_code == 200
	assert response.json()['success'] is True
	assert response.json()['message'] == "The product has been added to your <a href=\"/cart\">shopping cart</a>"


def test_add_to_cart_unauthorized_one_product():
	response = demoqa().post('/addproducttocart/catalog/31/1/1'
	                         , cookies={'Nop.customer': str(uuid4())}
	                         )
	assert response.status_code == 200
	assert response.json()['success'] is True
	assert response.json()['message'] == "The product has been added to your <a href=\"/cart\">shopping cart</a>"
	assert response.json()['updatetopcartsectionhtml'] == '(1)'


def test_add_to_cart_unauthorized_two_product():
	uid = str(uuid4())
	demoqa().post('/addproducttocart/catalog/31/1/1'
	                         , cookies={'Nop.customer': uid}
	                         )
	response = demoqa().post('https://demowebshop.tricentis.com/addproducttocart/catalog/31/1/1'
	                         , cookies={'Nop.customer': uid}
	                         )
	assert response.status_code == 200
	assert response.json()['success'] is True
	assert response.json()['message'] == "The product has been added to your <a href=\"/cart\">shopping cart</a>"
	assert response.json()['updatetopcartsectionhtml'] == '(2)'


def test_add_to_cart_authorized():
	from dotenv import load_dotenv
	import os
	load_dotenv()
	auth_cookie_name = 'NOPCOMMERCE.AUTH'
	login = os.getenv('user_login')
	password = os.getenv('user_password')

	response = demoqa().post(
		'/login',
		data={'Email': login, 'Password': password},
		allow_redirects=False)
	auth_cookie_value = response.cookies.get(auth_cookie_name)
	print(auth_cookie_value)

	response = demoqa().post(
		'/addproducttocart/catalog/31/1/1',
		cookies={auth_cookie_name: auth_cookie_value}
	)

	assert response.status_code == 200
	assert response.json()['success'] is True
	assert response.json()['message'] == "The product has been added to your <a href=\"/cart\">shopping cart</a>"
	assert response.json()['updatetopcartsectionhtml'] == '(1)'


def test_add_to_cart_authorized_new(demoqa_authorized):

	# auth_cookie_name = 'NOPCOMMERCE.AUTH'
	# login = os.getenv('user_login')
	# password = os.getenv('user_password')
	#
	# response = demoqa().post(
	# 	'/login',
	# 	data={'Email': login, 'Password': password},
	# 	allow_redirects=False)
	# auth_cookie_value = response.cookies.get(auth_cookie_name)
	# print(auth_cookie_value)

	response = demoqa().post(
		'/addproducttocart/catalog/31/1/1',
		#cookies={auth_cookie_name: auth_cookie_value}
	)

	assert response.status_code == 200
	assert response.json()['success'] is True
	assert response.json()['message'] == "The product has been added to your <a href=\"/cart\">shopping cart</a>"
	#assert response.json()['updatetopcartsectionhtml'] == '(1)'