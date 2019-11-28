from TraditionalTestFramework.SeleniumHelpers.SeleniumBindings import *
from selenium.webdriver.common.by import By
import json
from array import *

class RecentTransactionsPage(SeleniumBindings):
 
	transactionTableAmountHeading = (By.XPATH, "//*[@id='amount']")
	transactionPageAd1 = (By.XPATH, "//*[@id='flashSale']/img")
	transactionPageAd2 = (By.XPATH, "//*[@id='flashSale2']/img")

	def getRowData(self):

		rowCount = 1
		columnCount = 1
		companyName = ""
		transactionTableEntry={}
		transactionTableData = {}
		tableRow = (By.XPATH, "//*[@id='transactionsTable']/tbody/tr["+str(rowCount)+"]")
		tableColumn = (By.XPATH, "//*[@id='transactionsTable']/tbody/tr["+str(rowCount)+"]/td["+str(columnCount)+"]")

		while(self.getElement(tableRow)):
			transactionTableData = {}
			while(self.getElement(tableColumn)):
				if(self.getElement(tableColumn)):
					text = self.findInnerText(tableColumn)
					transactionTableData[str(columnCount)] = {str(text)}
					if(columnCount == 3):
						companyName = text
					columnCount += 1
					tableColumn = (By.XPATH, "//*[@id='transactionsTable']/tbody/tr["+str(rowCount)+"]/td["+str(columnCount)+"]")
			rowCount += 1
			columnCount = 1
			tableRow = (By.XPATH, "//*[@id='transactionsTable']/tbody/tr["+str(rowCount)+"]")
			tableColumn = (By.XPATH, "//*[@id='transactionsTable']/tbody/tr["+str(rowCount)+"]/td["+str(columnCount)+"]")
			transactionTableEntry[companyName]=transactionTableData
		return transactionTableEntry

	def transactionTableSortByAsc(self, element):
		self.click(element)
		self.click(element)


	def checkBaseLine(self, currentAd):
		found = False

		with open('./TraditionalTestFramework/Baselines/adBaseline.txt', 'r+') as f:
			for ad in f:
				ad = ad.replace("\n", "")
				if(ad == currentAd):
					found = True
					break
			if(found == True):
				print("Ad previously displayed")
			if(found == False):
				print("New Ad feature, adding to baseline")
				f.write(currentAd + '\n')

	def getAdImage(self, element):
		adImage = self.getElement(element)

		if(adImage):
			imageSrc = self.getSrcAttribute(element)
			self.checkBaseLine(imageSrc)
			return True
		else:
			print("Ad not found")
			return False
	






	