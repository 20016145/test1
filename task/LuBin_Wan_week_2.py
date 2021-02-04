a=4
b=8
c=2
for i in range(a,b):
    if i % c==0:
        print(i)
# 4 5 6 7



some_text="We will be discussing your toughts and questions."
alphabets="abcdefghijklmnopqrstuvwxyz"
for alphabet in alphabets:
    count=0
    for i in some_text:
        if i == alphabet:
            count+=1

    print(alphabet + "=" +str(count))




a=10
b=4
count=0

while a>=b:
    a=a-b
    count+=1
print(count)
print(a)


