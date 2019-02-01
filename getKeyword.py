#alphabet = [ 0.0815, 0.0144, 0.0276, 0.0379, 0.1311, 0.0292, 0.0199, 0.0526, 0.0635, 0.0013, 0.0042, 0.0339, 0.254, 0.071, 0.08, 0.0198, 0.0012, 0.0683, 0.061, 0.1047, 0.0246, 0.0092, 0.0154, 0.0017, 0.0198, 0.0008 ]


# Accepts a string of text and the keyLength to divide that string upon
# Returns a 2D list where each 1D list is the coset of the original text
def createCoSets(text, keyLength):
	cosets = [];
	charSet = [];
	for i in range(keyLength):
		charSet= text[i::keyLength];
		cosets.append(charSet);

	return cosets;

# Accepts a string of text and the value to shift the text forwards or backwads by
# Returns the string of text after being shifted
def shiftText( text, shift ):
	alphabet = "abcdefghijklmnopqrstuvwxyz";
	lowerText = text.lower()
	shiftedText = "";

	for character in text:
		shiftedText.append()

def getXSquaredDiff( charStatistics ):
	num = 0.0;
	den = 0.0;
	IC = 0.0667;
	for stat in charStatistics:
		i = stat
		num += stat*(stat-1);
		den += stat;
	if ( den == 0.0):
		return 0.0;
	else:
		return IC - num / ( den * ( den - 1 ));


print("Enter the file of ciphertext to generate the cosets and keyword for: ");
fileName = input();

print("Enter the length of the keyword: ")
keyLength = int(input());

file = open(fileName, 'r');
cipherText = file.read();

cosets = createCoSets(cipherText, keyLength);

for coset in cosets:
	print( coset );