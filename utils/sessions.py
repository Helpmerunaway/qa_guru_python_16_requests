import os

from dotenv import load_dotenv

from utils.requests_helper import BaseSession


# оборачиваем без бейс юрл а через cats.get
def cats() -> BaseSession:
	load_dotenv()
	cats_url = 'https://catfact.ninja'
	return BaseSession(base_url=cats_url)


def demoqa() -> BaseSession:
	load_dotenv()
	demo_url = os.getenv('demo_shop_url')
	return BaseSession(base_url=demo_url)