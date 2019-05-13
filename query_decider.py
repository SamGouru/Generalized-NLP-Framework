def query_decider(sentence):
	PEDDHA = ""
	max_list = ["maximum", "max", "biggest", "largest", "most", "highest"]
	#if any(elem in max_list for elem in sentence):
	if ("maximum" in sentence or "max" in sentence or "biggest" in sentence or "largest" in sentence or "most" in sentence
	or "highest" in sentence):
		PEDDHA = "peddha"
	
	elif ("minimum" in sentence or "min" in sentence or "smallest" in sentence or "lowest" in sentence or "least" in sentence 
	or "tiniest" in sentence):
		PEDDHA = "chinna"
	
	elif ("average" in sentence or "avg" in sentence):
		PEDDHA = "avg"
		
	elif ("add" in sentence or "sum" in sentence):
		PEDDHA = "sum"
	
	elif ("count " in sentence or "how many" in sentence):
		PEDDHA = "count"
	
	else:
		PEDDHA = ""
		
	return PEDDHA
	
def pop_decider(sentence):
	PLACE = ""
	#if any(elem in max_list for elem in sentence):
	if ("city" in sentence and "population" in sentence or "populated" in sentence):
		PLACE = "city"
	elif ("country" in sentence and "population" in sentence or "populated" in sentence):
		PLACE = "country"
	else:
		PLACE = ""
		
	return PLACE

def size_decider(sentence):
	SIZE = ""
	#if any(elem in max_list for elem in sentence):
	if ("size" in sentence and "city" in sentence or "surface area" in sentence and "city" in sentence):
		SIZE = "citysize"
		
	elif ("size" in sentence and "country" in sentence or "surface area" in sentence and "country" in sentence):
		SIZE = "countrysize"
		
	else:
		SIZE = ""
		
	return SIZE
	
def cap_decider(sentence):
	PLACE = ""
	#if any(elem in max_list for elem in sentence):
	if ("city" in sentence and "population" in sentence):
		PLACE = "city"
	elif ("country" in sentence and "population" in sentence):
		PLACE = "country"
	else:
		PLACE = ""
		
	return PLACE
	

def howmany_decider(sentence):
	HOW = ""
	#if any(elem in max_list for elem in sentence):
	if ("how many cities are there" in sentence):
		HOW = "howcity"
	elif ("how many countries are there" in sentence):
		HOW = "howcountry"
	else:
		HOW = ""
		
	return HOW