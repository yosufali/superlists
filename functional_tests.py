from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Chrome()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		# Edith has heard about a cool new online to-do app.
		# She goes to check its homepage
		self.browser.get('http://localhost:8000')

		# She notices the page title and the header mention to-do lists
		self.assertIn('To-Do', self.browser.title)
		self.fail('Finish the test!')

		# She is invited to enter a to-do item straight away


		# She types "Buy peacock feathers" into a textbox
		# (Edith's hobby is tying flying-fish lures)


		# When she hits enter, the page updates and now the page lists
		# "1: But peacock feathers" as an item in to-do lists


		# There is still a test box inviting her to add another item. She
		# enters "Use peacock feathers to make a fly" (Edith is very methodical)


		# The page updates again, and now shows both items on her list


		# Edith wonders whether the site will remember her list. Then she sees
		# that the site has generated a unique URL for her -- there is some
		# explanatory text to that effect.


		# She visits that URL - her to-do list is still there.


		# Satisfied, she goes back to sleep

if __name__ == '__main__':
	unittest.main(warnings='ignore')
