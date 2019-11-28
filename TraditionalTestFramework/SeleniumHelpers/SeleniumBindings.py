import unittest
import time
from random import randint
from selenium import webdriver
from selenium.webdriver import ActionChains


class SeleniumBindings():
	def click(self, element):
		"""
		Triggers a mouse 'click' on the passed WebElement.
		"""
		Create = self.driver.find_element(*element)
		Create.click()
		
	def inputText(self, text, selector):
		"""
		Enters text into the passed selector and presses 'Enter'.
		Selector should be an input box / textarea.
		"""
		Create = self.driver.find_element(*selector)
		Create.clear()
		Create.send_keys(text)
		
	def findInnerText(self, selector):
		"""
		Random generator to support test data.
		"""
		innerHtmlText = self.driver.find_element(*selector).text
		
		return innerHtmlText

	def getElement(self, selector):
		"""
		support test data.
		"""
		try:
			attribute_selection = self.driver.find_element(*selector)
		except:
			return False
		return True

	def  getSrcAttribute(self, selector):
		"""
		Triggers a mouse 'click' on the passed WebElement.
		"""
		src = self.driver.find_element(*selector).get_attribute("src")
		return src
		
	

		
		
		

