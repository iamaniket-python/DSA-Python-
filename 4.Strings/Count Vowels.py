# Count Vowels

text=input("Enter a name=")
vowels=""
count=0
for i in text:
    if i  in "aeiou":
        vowels +=i
        count +=1


print(f"vowels are {vowels} and the total count is {count}")