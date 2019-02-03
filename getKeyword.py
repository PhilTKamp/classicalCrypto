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

	for character in lowerText:
		# Finds the index of the character in the alphabet and adds the shift, modding to not overstep
		shiftedText += alphabet[(alphabet.find(character) + shift) % len(alphabet)];

	return shiftedText;


# Accepts a string of characters, and the alphabet to compare the characters to
# Returns a list correlating to the rates of appearance of each alphabetic 
# character within that string
def getCharCounts( text, alphabet ):
	charStats = [];
	lowerText = text.lower()
	for character in alphabet:
		charStats.append(lowerText.count(character));

	return charStats;


# Accepts an array of doubles/floats which correlate to the frequencies of characters appearing
# Returns the difference between the X2 calculated and the X2 of the English language
def getXSquared( charCounts, textLen ):
	chi2 = 0.0;
	expectedCounts = [0.08167,0.01492,0.02782,0.04253,0.12702,0.02228,0.02015,0.06094,0.06966,0.00153,0.00772,
				0.04025,0.02406,0.06749,0.07507,0.01929,0.00095,0.05987,0.06327,0.09056,0.02758,0.00978,
				0.02360,0.00150,0.01974,0.00074];
	for i in range(len(charCounts)):
		chi2 += ((charCounts[i] - textLen*expectedCounts[i]) ** 2) / (textLen*expectedCounts[i]);

	return chi2;


def getCosetCharICList(coset, alphabet):
	cosetCharX2List = [99999];
	length = len(coset);
	# We only need to check shifts which are not shifted by 0
	for i in range(1,len(alphabet)):
		currShift = shiftText(coset, i, alphabet);
		# print(currShift);
		currShiftCounts = getCharCounts(currShift, alphabet);
		cosetCharX2List.append(getXSquared(currShiftCounts, length));

	# print("Current Coset: ", coset);
	# print("Current X2: ", cosetCharX2List);
	return cosetCharX2List;



alphabet = "abcdefghijklmnopqrstuvwxyz";
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
	index = cosetCharICList.index(min(cosetCharICList));
	# The index of the minimum correlates to the index of the keyword character
	keyword += alphabet[index];

# text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
# for i in range(len(alphabet)):
# 	print(shiftText(text, i, alphabet));

# print(getCosetCharICList(text, alphabet));

print("Calculated Keyword: ", keyword);

