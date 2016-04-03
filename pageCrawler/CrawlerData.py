"""
This class is used to encapsulate information gathered from an individual crawler. 
This way, information handling and retreival is the same for all crawlers. 
Contains the following parameters:

OBLIGATORY PROPERTIES

title 			- A string of the thesis job name as listed on the webpage
location 		- The location of the job. *TODO* A function using bag of words is used
			  	  for normalizing the locaion property based on a bag of words of 
			      allowable locations. 
link			- The href link to the job page 


OPTIONAL PROPERTIES (if available)

applicationDate - Last date to submit application
datePublished   - The date when the application was published (OR when we pulled the ad)
department      - Company department

"""

class CrawlerData:

	def __init__(self):
		self.title
		self.location
		self.link
		self.jobHTML

		self.applicationDate
		self.datePublished
				
		self.department


