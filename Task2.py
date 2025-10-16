#Task 2
#F3: Reverse a Word — Reverse a given word using loops (no built-in functions).

word = input("Enter the word that has to be reversed : ")
reversed_word=''
for i in range(len(word)-1,-1,-1):
    reversed_word += word[i]
print("The reversed word is : ",reversed_word)
