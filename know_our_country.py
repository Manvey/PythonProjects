from random import shuffle
ques = [
    ("What is the name of your country","india"),
    ("What is the capital of your country","new delhi"),
    ("What is the national flower","lotus"),
    ("What is name of your national animal","tiger"),
    ("What is the name of national bird","peacock"),
    ("What is your national flag","tiranga")
]
right = 0
wrong = 0
for question, right_ans in ques:
    ans=input(question+" ")
    if ans.lower() == right_ans:
        right += 1
    else:
        print("No, the right answer is: ",right_ans)
        wrong += 1
print("Congratulations!")
print("You gave ", right, "right answers and", wrong, "wrong answers")
