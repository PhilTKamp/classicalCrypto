# Accepts a string of text and the keyLength to divide that string upon
# Returns a 2D list where each 1D list is the coset of the original text
def createCoSets(text, keyLength):
	cosets = [];
	charSet = [];
	for i in range(keyLength):
		charSet= text[i::keyLength];
		cosets.append(charSet);

	return cosets;

# Accepts a string of text and the value to shift the text forwards or backwards by, and the current alphabet
# Returns the string of text after being shifted
def shiftText( text, shift, alphabet ):
	lowerText = text.lower()
	shiftedText = "";

	for character in text:
		# Finds the index of the character in the alphabet and adds the shift, modding to not overstep
		shiftedText += alphabet[(alphabet.find(character) + shift) % len(alphabet)];

	return shiftedText;

# Accepts a string of characters, and the alphabet to compare the characters to
# Returns a list correlating to the rates of appearance of each alphabetic 
# character within that string
def getCharStats( text, alphabet ):
	charStats = [];
	lowerText = text.lower()
	for character in alphabet:
		charStats.append(float(lowerText.count(character)) / len(lowerText));

	return charStats;

# Accepts an array of doubles/floats which correlate to the frequencies of characters appearing
# Returns the difference between the X2 calculated and the X2 of the English language (AKA the IC)
def getXSquaredDiff( charStatistics ):
	num = 0.0;
	den = 0.0;
	IC = 0.0667;
	for stat in charStatistics:
		i = stat
		num += stat*(stat-1);
		den += stat;
	if ( den == 0.0 or den == 1):
		return 0.0;
	else:
		return abs(IC - num / ( den * ( den - 1 )));

def getCosetCharICList(coset, alphabet):
	cosetCharICList = [];
	for i in range(len(alphabet)):
		currShift = shiftText(coset, i, alphabet);
		currShiftStats = getCharStats(currShift, alphabet);
		cosetCharICList.append(getXSquaredDiff(currShiftStats));

	return cosetCharICList

alphabet = "abcdefghijklmnopqstuvwxyz";
keyword = "";


print("Enter the file of ciphertext to generate the cosets and keyword for: ");
fileName = input();

print("Enter the length of the keyword: ")
keyLength = int(input());

file = open(fileName, 'r');
cipherText = file.read();

cosets = createCoSets(cipherText, keyLength);
cosetsCharICLists = [];

for coset in cosets:
	cosetsCharICLists.append(getCosetCharICList(coset, alphabet));

for cosetCharICList in cosetsCharICLists:
	# Find the minimum for all of the IC's of the current coset This is your offset, Find the index of the minimum
	index = cosetCharICList.index(min(cosetCharICList))
	print(cosetCharICList);
	# The index of the minimum correlates to the index of the keyword character
	keyword += alphabet[index];

print("Calculated Keyword: ", keyword);

