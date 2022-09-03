import os

from utils.requests_helper import BaseSession


class DemoQA:
	def __init__(self):
		self.demoqa = BaseSession(base_url=os.getenv('demo_shop_url'))

	def login(self, user, password):
		return self.demoqa.post(
			'/login',
			data={'Email': user, 'Password': password},
			allow_redirects=False
		)

	def add_to_cart(self, **kwargs):
		cookies = kwargs.pop('cookies', None)
		return self.demoqa.post('/addproducttocart/catalog/31/1/1', cookies=cookies)