import random
import time 

MIN_DIGIT = 3
MAX_DIGIT = 15
OPERATORS = ["+", "-", "*", "/"]
TOTAL_PROBLEMS_AMOUNT = 10

def createMathProblem(): 
    left_value = random.randint(MIN_DIGIT, MAX_DIGIT)
    right_value = random.randint(MIN_DIGIT, MAX_DIGIT)
    operator = random.choice(OPERATORS)

    math_problem = str(left_value) + ' ' + operator + ' '  + str(right_value)
    answer = eval(math_problem) 
    return math_problem, answer

 
math_problem, answer = createMathProblem()

wrong_answers = 0
input('Press enter to start!')
print('__________________________')

start_time = time.time()

for i in range(TOTAL_PROBLEMS_AMOUNT):
    math_problem, answer = createMathProblem()
    while True:
        guess = input("Problem #" + str(i + 1) + ': ' + math_problem + " = ")
        if guess == str(answer):
            break
        else:
            wrong_answers += 1
            print('Nope...')

end_time = time.time()
quiz_time_duration = round(end_time - start_time, 2)

print('__________________________')
print('Good job! You have only failed' + ' ' + str(wrong_answers) + ' ' + 'times. The whole quiz took:' + ' ' + str(quiz_time_duration) + 'seconds.')
