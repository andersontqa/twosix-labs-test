import pytest
from selenium import webdriver
import time

@pytest.mark.usefixtures("driver_init")
class TestTwoSixLabs:

	def test_author_name(self):
		self.driver.get("https://www.google.com")
		search = self.driver.find_element_by_css_selector("input[title='Search']")
		search.send_keys("cyber-warriors-lack-planning-tools-that-could-change")
		search.submit()
		first_item = self.driver.find_element_by_css_selector("#rso > div:nth-child(1) > div > div > div > div > div > div:nth-child(3) > div > div > div > a")
		first_item.click()
		author_name = self.driver.find_element_by_css_selector("#f0mcELYnsjf5vr > div > div.m-byline__meta.a-body1 > div.m-byline__author > span > span > a").text
		try:
			assert author_name == "Mark Pomerleau"
			self.driver.save_screenshot("correct_author_name.png")
		except AssertionError:
			print(author_name + " is not Mark Pomerleau")
			self.driver.save_screenshot("wrong_author_name.png")
			assert False


		



