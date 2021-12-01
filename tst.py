#Chapter 11
#Testing My Code
#Testing a Function
def get_full_name(first, last, middle=""):
	"""generate the full name"""
	if middle:
		name = first + " " + middle + " " + last
	else:
		name = first + " " + last
	
	return name.title()

#Ass-1
def city_func(city, country, population=""):
	"""generate the full string"""
	if population:
		same_name = city + " " + str(population) + " " + country
	else:
		same_name = city + " " + country

	return same_name.title()

#Testing class
#A variety of Assert Module
#AssertEqual
#AssertNotEqual
#AssertTrue
#AssertFalse
#AssertIn
#AssertNotIn


#A Class to Test
class AnonymouSurvey():
	"""Collect answers from survey questions"""
	def __init__(self, question):
		self.question = question
		self.responses = []

	def show_question(self):
		print(question)

	def store_response(self, new_response):
		self.responses.append(new_response)

	def show_results(self):
		print("Survey Results: ")
		for response in responses:
			print("-" + response)