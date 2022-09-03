import requests
import pytest
from pytest_voluptuous import S  # class validation
from voluptuous import Any, PREVENT_EXTRA

from utils.sessions import cats



def test_facts_count():
	"""
	1. get https://catfact.ninja/facts?limit=2
	2. asserts
	:return:
	"""
	limit = 2
	response = requests.get('https://catfact.ninja/facts', params={'limit': limit})

	assert len(response.json()['data']) == limit


def test_facts_count2():
	"""
	1. get https://catfact.ninja/facts?limit=2
	2. asserts
	:return:
	"""
	limit = 2
	response = cats().get('/facts', params={'limit': limit})

	assert len(response.json()['data']) == limit


def test_facts_status_code():
	"""
	1. get https://catfact.ninja/facts?limit=2
	2. asserts
	:return:
	"""
	limit = 2
	response = requests.get('https://catfact.ninja/facts', params={'limit': limit})

	assert response.status_code == 200


from voluptuous import Schema

schema = Schema({
	'fact': str,
	'length': int
})

def test_fact_fields_validation():
	response = requests.get('https://catfact.ninja/fact')
	# valid schemas
	assert isinstance(response.json()['fact'], str)
	assert isinstance(response.json()['length'], int)


def test_fact_fields_validation_voluptuous():
	schema = Schema({
		'fact': str,
		'length': int
	})

	response = requests.get('https://catfact.ninja/fact')
	# valid schemas
	assert S(schema) == response.json()



# def test_facts_count_voluptuous():
# 	"""
# 	1. get https://catfact.ninja/facts?limit=2
# 	2. asserts
# 	:return:
# 	"""
# 	limit = 2
# 	fact = Schema({
# 			'fact': str,
# 			'length': int
# 			}
# 		]
# 	},
# 		extra=PREVENT_EXTRA,
# 		required=True
# 	)
#
# 	response = requests.get('https://catfact.ninja/facts', params={'limit': limit})
#
# 	assert S(schema) == response.json()