NATO={"A":"Alpha","B":"Bravo","C":"Charlie","D":"Delta",
"E":"Echo","F":"Foxtro","G":"Golf","H":"Hotel",
"I":"India","J":"Juliet","K":"Kilo","L":"Lima",
"M":"Mike","N":"November","O":"Oscar","P":"Papa",
"Q":"Quebec","R":"Romeo","S":"Sierra","T":"Tango",
"U":"Uniform","V":"Victor","W":"Whisky","X":"X-Ray",
"Y":"Yankee","Z":"Zulu",}
word = input("enter a word").upper()
for letter in word:
        if letter in NATO.keys():
                word=NATO.get(letter)
                print(word)



w = input("enter a word:").lower()
shift = int (input("enter a number:"))
alphabet = "abcdefghijklmnopqrstuvwxyz"

def ceaser(plaintxt,key):
        cipher = ""
        for letters in w:
                if letters == "":
                        cipher+=""
                else:
                        for i in range (len(albhabet)):
                                if alphabet[i] == letters:
                                        cipher+= alphabet[(i+key) % 26]
                                        return cipher
                                print(ceaser(w,shift))
