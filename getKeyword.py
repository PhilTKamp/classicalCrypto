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


print("Enter the file of ciphertext to generate the cosets and keyword for: ");
fileName = input();

print("Enter the length of the keyword: ")
keyLength = int(input());

file = open(fileName, 'r');
cipherText = file.read();

cosets = createCoSets(cipherText, keyLength);

for coset in cosets:
	print( coset );