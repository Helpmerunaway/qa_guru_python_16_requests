import json
import logging

import curlify
import allure
from requests import Session
import logging


# def allure_request_logger(function):
# 	def wrapper(*args, **kwargs):
# 		response = function(args, kwargs)
# 		message = curlify.to_curl(response.request)
# 		logging.info(f'{response.status_code} {message}')
# 		allure.attach(
# 			body=message.encode('utf-8'),
# 			name=f'Request {response.request.method} {response.status_code}',
# 			attachment_type=allure.attachment_type.TEXT,
# 			extension='txt'
# 		)
# 		try:
# 			allure.attach(
# 				body=json.dumps(response.json(), indent=4, ensure_ascii=False).encode('utf-8'),
# 				name=f'Response {response.request.method}',
# 				attachment_type=allure.attachment_type.JSON,
# 				extension='json'
# 		)
# 		except ValueError as error:
# 			allure.attach(
# 				body=response.text.encode('utf8'),
# 				name=f'NOT Json Response {response.request.method}',
# 				attachment_type=allure.attachment_type.JSON,
# 				extension='json'
# 			)
# 		return response
# 	return wrapper

# переопределение бейс юрл

class BaseSession(Session):
	def __init__(self, **kwargs):
		self.base_url = kwargs.pop('base_url')
		super().__init__()




	# с помощью курлифая преобразуем параметры запроса в курл в аллюр тест бади - реквест
	#@allure_request_logger
	def request(self, method, url, **kwargs):
		with allure.step(f'{method} {url}'):
			response = super().request(method, url=f'{self.base_url}{url}', **kwargs)
			message = curlify.to_curl(response.request)
			logging.info(f'{response.status_code} {message}')
			allure.attach(
				body=message.encode('utf-8'),
				name=f'Request {method} {response.status_code}',
				attachment_type=allure.attachment_type.TEXT,
				extension='txt'
			)
		return response


