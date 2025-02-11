#project 2
#t-

word_in=input("put yo word to see if its an uppercase ")
# print("-------checking-------")
# for text in word_in:
#     print(text,text.isupper())
num=0
word_out=word_in.replace(" ","")
length=len(word_out)
while num < length:
    if not word_out[num].isupper():
    # print(word_out[num].upper())
     print("letter","->",word_out[num],"is",word_out[num].isupper(),"with index",num,"isn't uppercase")
    num +=1


print("full word in uppercase will be\n",word_in.upper())



