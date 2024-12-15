questions = [
    ["1. What's the capital of France?", "Rome", "Paris", "Berlin", "Madrid", 2],
    ["2. What is 5 + 3?", "6", "7", "8", "9", 3],
    ["3. Which planet is known as the Red Planet?", "Venus", "Mars", "Jupiter", "Saturn", 2],
    ["4. Who wrote Romeo and Juliet?", "Mark Twain", "Charles Dickens", "William Shakespeare", "J.K. Rowling", 3],
    ["5. What is the boiling point of water at sea level?", "90°C", "100°C", "110°C", "120°C", 2],
    ["6. What is the largest mammal on Earth?", "Elephant", "Blue whale", "Shark", "Giraffe", 2],
    ["7. How many continents are there on Earth?", "5", "6", "7", "8", 3],
    ["8. What gas do plants absorb from the atmosphere?", "Oxygen", "Hydrogen", "Carbon dioxide", "Nitrogen", 3],
    ["9. What is the main ingredient in guacamole?", "Tomato", "Onion", "Avocado", "Cucumber", 3],
    ["10. Which country is famous for the Great Wall?", "India", "China", "Japan", "Korea", 2]
]

levels = [0,1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money = 0
for i in range(0,len(questions)):
    question=questions[i] 
    print(f"The question is of Rs{levels[i+1]}")
    print(question[0])
    print(f"a. {question[1]}          b. {question[2]} ")
    print(f"c. {question[3]}          d. {question[4]} ")
    reply=int(input("Chose your option(1-4) and 0 for quit : "))
    if(reply==question[-1]):
        print("Correct ans")
        # money=levels[i]
        if(i==4):
           money=10000
        elif(i == 9):
           money = 320000
        elif(i == 14):
            money = 10000000
    elif(reply==0):
        money=levels[i]
        break
    else:
       break
print(f"The total money earned is {money}")