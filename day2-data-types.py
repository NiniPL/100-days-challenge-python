#TIP CALCULATOR AS A FINAL PROJECT
bill = float(input("Welcome to the tip calculator!\nWhat was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
split = int(input("How may people to split the bill? "))
#result = (bill / split) * (1 + tip / 100)
result = (bill + (bill * tip / 100)) / split
print(f'Each person should pay: ${"{:.2f}".format(result)}.')  #format instead of round to avoid issues with 0 in the end
#----------------------------------------------------------------------
# ## Data Types
# # String
# "Hello"[index of letter, starting from 0]
# print("Hello"[4])
# print("123"+"345") 

# # Integer
# print(123)
# print(123+345)
# print(131_334_222)
# print(131334222)

# # Float
# print(3.14159)

# # Boolean
# print(True)
# print(False)
#----------------------------------------------------------------------
# # Error type
# num_char = len(input("Name: "))
# type = print(type(num_char))
# print("Your name has "+ str(num_char) +" characters.")

# a = float(123)
# print(type(a))
# print(70 +float("100.5"))
# print(str(70)+ str(100.5))
# print(int(70)+int(100.5))
#-----------------------------------
# coding challange
# two_digit_number = input()
# a = int(two_digit_number[0])
# b = int(two_digit_number[-1])
# print("Sum of numbers is: "+ str(a+b))
#-----------------------------------
# test = input() #the input is always str type
# print(type(test))
#----------------------------------------------------------------------
### Mathematical Operations (+-*/)
# print(6/3) #always type float
# print(2**3) #potegowanie

## Kolejnosc wykonywania dzialan: PEMDAS
# Parentheses:    ()
# Exponents:      **
# Multiplication: *     # Division:       /   #are equaly important, but first the left, then right
# Addition:       +     # Substraction:   -   #are equaly important, but first the left, then right
# print(3*(3+3)/3-3)
#-----------------------------------
# choding challenge - BMI counter
# h = input("Input height [m]: ")
# w = input("Input weight [kg]: ")
# bmi = int(float(w) / float(h)**2)
# # print("Your BMI is: "+str(bmi))
# print(f"Your height is {h}, your weight is {w}. So your BMI is: {round(bmi)}")
#----------------------------------------------------------------------
# print(int(8/3)) #it's chopping not rounding the number
# print(round(8/3)) #it's round
# print(round(8/3, 2)) #round till second character after dot
# print(8//3) #floor division (zaokragla do dolu)
# result = 4/2
# result /= 2   #it's the same like: result = result / 2 (shortcut)
# print(result)
#-----------------------------------
# Fstrings (mixed strings with other types)
# score = 0
# score += 1 #it's the same: score = score + 1 (shortcut)
# # print(score)
# print("your score is: "+str(score))
# print(f"Your score is: {score}")
#----------------------------------------------------------------------
# ### LIFE IN WEEKS
# age = input("Input your age: ")
# #result = (90*52) - int(age)*52      #parsowanie typow danych - zamienianie typow danych
# print(f"You have {((90*52) - int(age)*52)} weeks left.") 
# #-----------------------------------