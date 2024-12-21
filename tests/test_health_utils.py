import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from health_utils import calculate_bmi, calculate_bmr

def test_calculate_bmi():
	height = 1.75
	weight = 70
	expected_bmi = 22.86
	assert round(calculate_bmi(height, weight), 2) == expected_bmi

def test_calculate_bmr_male():
	height = 175
	weight = 70
	age = 25
	gender = 'male'
	expected_bmr = 1724.1
	assert round(calculate_bmr(height, weight, age, gender), 1) == expected_bmr

def test_calculate_bmr_female():
	height = 160
	weight = 55
	age = 30
	gender = 'female'
	expected_bmr = 1322.0
	assert round(calculate_bmr(height, weight, age, gender), 1) == expected_bmr
