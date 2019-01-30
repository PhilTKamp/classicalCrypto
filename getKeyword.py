# Accepts a string of text and the keyLength to divide that string upon
# Returns a 2D list where each 1D list is the coset of the original text
def createCoSets(text, keyLength):
	cosets = [];
	charSet = [];
	for i in range(keyLength):
		charSet= text[i::keyLength];
		cosets.append(charSet);

	return cosets;


test = "1234567123456712345671234567";

cosets = createCoSets(test, 7);

for coset in cosets:
	print(coset);