#My FizzBuzz Program in Python
#Which I spent all too much time thinking about.

for number in range(1, 34):
    word = ''
    if (number%3 == 0):
        word+="Fizz"
    if (number%5 == 0):
        word+="Buzz"
    print(word or number)
    

