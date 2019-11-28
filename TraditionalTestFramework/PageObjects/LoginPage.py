from TraditionalTestFramework.SeleniumHelpers.SeleniumBindings import *
from TraditionalTestFramework.SeleniumHelpers.SeleniumBindings import *
from selenium.webdriver.common.by import By

class LoginPage(SeleniumBindings):
  
	pageHeading = (By.XPATH, "/html/body/div/div/h4")
	validUsername = "Username"
	usernameLabel = (By.XPATH, "/html/body/div/div/form/div[1]/label")
	usernameIcon = (By.XPATH, "/html/body/div/div/form/div[1]/div")
	usernameField = (By.XPATH, "//*[@id='username']")
	validPassword = "Password"
	passwordLabel = (By.XPATH, "/html/body/div/div/form/div[2]/label")
	passwordIcon = (By.XPATH, "/html/body/div/div/form/div[2]/div")
	passwordField = (By.XPATH, "//*[@id='password']")
	loginButton = (By.XPATH, "//*[@id='log-in']")
	rememberMe = (By.XPATH, "/html/body/div/div/form/div[3]/div[1]/label/input")
	loginWarning = (By.XPATH, "/html/body/div/div/div[3]")
	twitter = (By.XPATH, "/html/body/div/div/form/div[3]/div[2]/a[1]/img")
	facebook = (By.XPATH, "/html/body/div/div/form/div[3]/div[2]/a[2]/img")
	linkedin = (By.XPATH, "/html/body/div/div/form/div[3]/div[2]/a[3]/img")

	def login(self, usernameValue, passwordValue):
		
		self.inputText(usernameValue,self.usernameField)
		self.inputText(passwordValue,self.passwordField)
		self.click(self.loginButton)

	def validLogin(self, usernameValue, passwordValue):
		
		self.inputText(usernameValue,self.usernameField)
		self.inputText(passwordValue,self.passwordField)
		self.click(self.loginButton)

		validationAlert = self.findPageElement(self.loginWarning)
		if(validationAlert == False):
			return True

	def invalidLogin(self, usernameValue, passwordValue):

		self.inputText(usernameValue,self.usernameField)
		self.inputText(passwordValue,self.passwordField)
		self.click(self.loginButton)

		validationAlert = self.findPageElement(self.loginWarning)
		if(validationAlert):
			return True

	def findPageElement(self, element):

		elementResult = self.getElement(element)
		return elementResult

	