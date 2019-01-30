import pandas
import matplotlib
from collections import Counter

# Accepts the overall text, and the size of the substring to find repeated iterations fo text
def getDistances( text, displacement ):
	distances = [];


# Accepts the substring, the overall text to find
# Will return a list of all indexes where it found the string, including the first occurence 
def findAll( substr, text ):
	indicies = []

	# If the substr didn't exist, kick out
	if(text.find(substr) == -1):
		return;

	# Finds the starting point for our text
	indicies.append(text.find(substr));

	# The point where we start our search, first index + the length of the substring to avoid overlap
	startSearch = indicies[0] + len(substr);

	# While we keep finding matches, keep searching and moving th starting point forward
	while(text.find(substr, startSearch) != -1):

		# Adds the next found index to our list and gets a new point to start the search from
		indicies.append(text.find(substr, start));
		startSearch = indicies[len(indicies) - 1] + len(substr);

	return indicies;


print("Enter the file to generate a histogram for: ");
file = input();

fileObj = open(file, 'r');
text = fileObj.read();

print(text);
