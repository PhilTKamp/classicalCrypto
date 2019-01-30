import matplotlib

# Accepts the overall text, and the size of the substring to find repeated iterations of text
# Returns a list of all distances between all duplicated substrings of size 'subStringSize'
def getDistances( text, subStringSize ):
	distances = [];

	finalIndex = len(text) - 2*subStringSize;

	# Steps through the overall text, pulling out subStringSize chunks and seeing if they're repeated
	# if repeats are found
	for i in range(0, finalIndex):
		subString = text[i:i+subStringSize];
		occurences = findAll(subString, text);
		if(len(occurences) > 1):
			for j in range(0, len(occurences) - 1):
				for k in range(1, len(occurences)):
					distances.append(occurences[k] - occurences[j]);

	distances.sort();
	return distances;


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
		indicies.append(text.find(substr, startSearch));
		startSearch = indicies[len(indicies) - 1] + len(substr);


	return indicies;


print("Enter the file to generate a histogram for: ");
file = input();

fileObj = open(file, 'r');
text = fileObj.read();

print("Parsed text:", text);

displacements = getDistances(text, 3);

print("Distances: ", displacements);
