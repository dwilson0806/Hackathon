from TraditionalTestFramework.PageObjects.LoginPage import *
from TraditionalTestFramework.PageObjects.RecentTransactionsPage import *
from TraditionalTestFramework.BrowserConfig.Browsers import *


class VisualAITests(LoginPage, RecentTransactionsPage):

	#url = "https://demo.applitools.com/hackathon.html"
	url = "https://demo.applitools.com/hackathonV2.html"
	
	def test_005_assert_login_page_elements(self):
		driver = self.driver
		print(self._testMethodName)
		self.setBatching(self._testMethodName)
		self.eyes.check_window()
	
	def test_010_no_username_no_password_on_login(self):
		driver = self.driver
		self.setBatching(self._testMethodName)	
		self.login('', '')
		self.eyes.check_window()

	def test_015_valid_username_no_password_on_login(self):
		driver = self.driver
		self.setBatching(self._testMethodName)	
		self.login('username', '')
		self.eyes.check_window()

	def test_020_no_username_valid_password_on_login(self):
		driver = self.driver
		self.setBatching(self._testMethodName)
		self.login('', 'password')
		self.eyes.check_window()

	def test_025_valid_username_valid_password_on_login(self):
		driver = self.driver
		self.setBatching(self._testMethodName)	
		self.login('username', 'password')
		self.eyes.check_window()

	def test_030_assert_transaction_page_elements(self):
		driver = self.driver
		self.setBatching(self._testMethodName)
		self.login("test", "test")
		self.eyes.check_window()
		self.transactionTableSortByAsc(self.transactionTableAmountHeading)
		self.eyes.check_window()

	#def test_035_Canvas_Chart_Test(self):
		"""
		* Unfortunately I couldn't find a nice way to implement this with the time using functional approach with time
		* This AI tests corresponds to this
		"""

	#url = url+"?showAd=true" will override main url, so commented out to avoid this. Works as expected on traditional side. 
	#Thinking my code integration with eyes is make csausing this to. run differently, but I couldn't get to bottom of this in time. 

	def test_040_assert_transaction_page_ad_1(self):
		driver = self.driver
		self.setBatching(self._testMethodName)
		self.login('username', 'password')
		self.eyes.check_window()
		
	def test_045_assert_transaction_page_ad_2(self):
		driver = self.driver
		self.setBatching(self._testMethodName)
		self.login('username', 'password')
		self.eyes.check_window()
    	
class TestChrome(ChromeSetupAI, unittest.TestCase, VisualAITests):
	"""
	* ChromeSetupAI - Chrome specific setUp and tearDown methods
	* unittest.TestCase - Indicates that this class is a test
	* VisualAITests - The class that contains the test
	"""
if __name__ == "__main__":
    unittest.main(verbosity=2)
