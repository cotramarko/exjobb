'''
Is in charge of managing all text elements of a CrawlerData object, such as: 
	1. Making sure that each thesis title contains a certain keyword.
	2. Renaming the spelling of cities and regions. --TODO--

	TODO
	   Both functions should be placed as methods in CrawlerData
'''

# Should perhaps be crawlerData??
def isThesis(title):
	mixOfWords = ["Diploma","Thesis","Examensarbete",
				  "credits","Exjobb","30 hp",
				  "30 credits","60 hp","60 credits"]	
	hasKeyword = False

	for word in mixOfWords:
		if word.lower() in title.lower():
			hasKeyword = True

	return hasKeyword


def standardizeLocation(location):
	dictOfCities = {'Gothenburg': "Göteborg", 
  	 			    'Stockholm': "Stockholm",
  	 			    'Solna': "Stockholm",
  	 			    }

	# We use an 'or' so that even if 'location' has the correct spelling, we omit everything else
	# such as Län, country and so on.
	for cityKey in dictOfCities:
		if cityKey.lower() in location.lower() or dictOfCities[cityKey].lower() in location.lower():
			location = dictOfCities[cityKey]

	# Remove "Sweden" from location
	if "Sweden".lower() in location.lower():
		location = location.replace("Sweden","")
	
	# These are temporary, should be generalized more 
	if "-" in location.lower():
		location = location.replace("-"," ")
	
	if "\n".lower() in location.lower():
		location = location.replace("\n"," ")

	if ")".lower() in location.lower():
		location = location.replace(")"," ")

	if "(".lower() in location.lower():
		location = location.replace("("," ")

	if location[0] == " ":
		location = location[1:] 

	return location			 			   

'''
def runTests():

	location = "Sweden (Gothenburg)"

	print(standardizeLocation(location))

	location = "Stockholm Stockholm SE"

	print(standardizeLocation(location))

	location = "Gävle"

	print(standardizeLocation(location))

	location = "Gävle Sweden"

	print(standardizeLocation(location))

	location = "Västerås\nVaestmanland County\nSweden"

	print(standardizeLocation(location))

	location = "Sweden-Skane-Lund"

	print(standardizeLocation(location))
'''


