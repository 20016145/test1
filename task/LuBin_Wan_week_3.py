original=input("enter a word=")
print(original)
vowels={"a","e","i","o","u"}
consonant={"b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"}
word=original
first=original[0]
second=original[1]
third=original[2]
if first in vowels:
	new_word=word+'ay'
else:
	new_word=word[1:]+second+"ay"
	if (first and second) in consonant:
		new_word=word[2:]+first+second+'ay'
	if (first and second and third) in consonant:
			new_word= word[3:]+first+second+third+"ay"
			print(new_word)

    
