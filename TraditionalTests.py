from TraditionalTestFramework.PageObjects.LoginPage import *
from TraditionalTestFramework.PageObjects.RecentTransactionsPage import *
from TraditionalTestFramework.BrowserConfig.Browsers import *
import time

class TraditionalTest(LoginPage, RecentTransactionsPage):

	url = "https://demo.applitools.com/hackathon.html"
	#url = "https://demo.applitools.com/hackathonV2.html"

	def test_005_assert_login_page_elements(self):
		driver = self.driver

		pageElements = [LoginPage.pageHeading, LoginPage.usernameLabel, LoginPage.usernameIcon, LoginPage.usernameField, 
		LoginPage.passwordLabel, LoginPage.passwordLabel, LoginPage.passwordIcon, LoginPage.passwordField, LoginPage.loginButton,
		LoginPage.rememberMe, LoginPage.twitter, LoginPage.facebook, LoginPage.linkedin]
		
		for element in pageElements:
			element = self.findPageElement(element)
			self.assertEqual(element, True)

	def test_010_no_username_no_password_on_login(self):
		driver = self.driver	
		self.assertEqual(self.invalidLogin('', ''), True)

	def test_015_valid_username_no_password_on_login(self):
		driver = self.driver	
		self.assertEqual(self.invalidLogin('username', ''), True)

	def test_020_no_username_valid_password_on_login(self):
		driver = self.driver	
		self.assertEqual(self.invalidLogin('', 'password'), True)

	def test_025_valid_username_valid_password_on_login(self):
		driver = self.driver	
		self.assertEqual(self.validLogin('username', 'password'), True)

	def test_030_assert_recent_transactions(self):
		driver = self.driver
		self.validLogin('username', 'password')
		transactionDataBaseline = self.getRowData()	
		self.transactionTableSortByAsc(self.transactionTableAmountHeading)
		transactionDataSoreted = self.getRowData()

		for x in transactionDataSoreted.keys():
			self.assertEqual(transactionDataBaseline[x], transactionDataSoreted[x])

	#def test_035_Canvas_Chart_Test(self):
		"""
		* Unfortunately I couldn't find a nice way to implement this with the time.
		* Due to the limitations with selectors I would have went with an image detections/extraction approach.
		"""
	url = url+"?showAd=true"

	def test_040_assert_transaction_page_ad_1(self):
		driver = self.driver
		self.validLogin('username', 'password')
		self.assertEqual(self.getAdImage(self.transactionPageAd1), True)
		
	def test_045_assert_transaction_page_ad_2(self):
		driver = self.driver
		self.validLogin('username', 'password')
		self.assertEqual(self.getAdImage(self.transactionPageAd2), True)

		         
class TestChrome(ChromeSetupDefault, unittest.TestCase, TraditionalTest):
	"""
	* ChromeSetupDefault - Chrome specific setUp and tearDown methods
	* unittest.TestCase - Indicates that this class is a test
	* TraditionalTest - The class that contains the test
	"""

if __name__ == "__main__":
    unittest.main(verbosity=2)
