codes = {
1 : '''
# Number of subjects
num_subjects = int(input("Enter the number of subjects: "))
# Initialize total marks to 0
total_marks = 0
# Input marks for each subject and calculate the total
for i in range(num_subjects):
 mark = float(input(f"Enter marks for subject {i+1}: "))
 total_marks += mark
# Calculate percentage
percentage = (total_marks / (num_subjects * 100)) * 100
# Display results
print("\nResults:")
print(f"Total Marks: {total_marks}")
print(f"Percentage: {percentage:.2f}%")
''' ,
2 : '''
# Input four numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
num4 = float(input("Enter the fourth number: "))
# Find the largest number using conditional statements
if num1 >= num2 and num1 >= num3 and num1 >= num4:
 largest = num1
elif num2 >= num1 and num2 >= num3 and num2 >= num4:
 largest = num2
elif num3 >= num1 and num3 >= num2 and num3 >= num4:
 largest = num3
else:
 largest = num4
# Display the result
print(f"The largest number is: {largest}")
''' ,
3 : '''
number = int(input("Enter the number for the multiplication table: "))
# Input the range for the table
limit = int(input("Enter the range up to which you want the table: "))
# Print the multiplication table
print(f"\nMultiplication Table for {number}:")
for i in range(1, limit + 1):
 print(f"{number} x {i} = {number * i}")
''',

4 : '''
#a = 1 + 2 + 3 + ⋯ + n
# Input the value of n
n = int(input("Enter the value of n: "))
# Calculate the sum of the series
sum_series = n * (n + 1) // 2
# Display the result
print(f"The sum of the series 1 + 2 + 3 + ... + {n} is: {sum_series}")
#b = 1^2+2^2+3^2+...+n^2
# Input the value of n
n = int(input("Enter the value of n: "))
# Calculate the sum of the series
sum_series = sum(i**2 for i in range(1, n + 1))
# Display the result
print(f"The sum of the series 1^2 + 2^2 + 3^2 + ... + {n}^2 is: 
{sum_series}")
''' ,

5 : '''
# Input the number
number = int(input("Enter a number less than 15: "))
# Check if the number is valid
if number >= 15:
 print("Error: Please enter a number less than 15.")
else:
 # Calculate factorial
 factorial = 1
 for i in range(1, number + 1):
 factorial *= i
 # Display the result
 print(f"The factorial of {number} is: {factorial}")
''' , 
6 : '''
# Input the marks
marks = int(input("Enter the marks (0 to 100): "))
# Determine the grade based on the ranges
if 91 <= marks <= 100:
 grade = 'A'
elif 81 <= marks <= 90:
 grade = 'B'
elif 71 <= marks <= 80:
 grade = 'C'
elif 61 <= marks <= 70:
 grade = 'D'
else:
 grade = 'E'
# Display the grade
print(f"The grade for marks {marks} is: {grade}")
''' ,
7 : '''
# Input the character
char = input("Enter a character: ")
# Check if the character is a digit, alphabet, or special character
if char.isdigit():
 print(f"The character '{char}' is a digit.")
elif char.isalpha():
 print(f"The character '{char}' is an alphabet.")
else:
 print(f"The character '{char}' is a special character.")
''' ,
8 : '''
# Input two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
# Join the two lists
joined_list = list1 + list2
# Display the result
print(f"The joined list is: {joined_list}")
''' ,
9 : '''
import numpy as np
from scipy import stats
# Input a list of numbers
data = list(map(int, input("Enter the numbers separated by space: 
").split()))
# Calculate mean
mean = np.mean(data)
# Calculate median
median = np.median(data)
# Calculate mode
mode = stats.mode(data)[0][0] # Extract the mode value from the 
result
# Display the results
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")
''' ,
10:  '''
import statistics
# Example data set
data = [10, 12, 23, 23, 16, 23, 21, 16]
# Calculate variance and standard deviation using statistics module
variance = statistics.variance(data)
standard_deviation = statistics.stdev(data)
# Print the results
print(f"Variance: {variance}")
print(f"Standard Deviation: {standard_deviation}")
''' ,
11 : ''' 
#import the library
import matplotlib.pyplot as plt
#Create list for data
player=['Gurbaz','Kohli','Warner','Sharma','Quinton','Pooran']
runs=[281,151,178,257,243,228]
plt.plot(player,runs,color='blue',marker='o')
#Giving title for the graph
plt.title('Runs scored in ICC Men’s T20 World Cup, 2024')
plt.xlabel('Players')
plt.ylabel('Runs')
plt.show()
#import the library
import matplotlib.pyplot as plt
#Create list for data
player=['Gurbaz','Kohli','Warner','Sharma','Quinton','Pooran']
runs=[281,151,178,257,243,228]
plt.plot(player,runs,color='blue',marker='o')
#Giving title for the graph
plt.title('Runs scored in ICC Men’s T20 World Cup, 2024')
plt.xlabel('Players')
plt.ylabel('Runs')
plt.show()
''' ,
12 : '''
# import the library to print scatter plot 
import matplotlib.pyplot as plt
fuelPrice = [72,75,73,75,72,75,78,75]
fuelConsumption = [150,200,125,150,300,180,60,148]
plt.scatter(fuelPrice,fuelConsumption,marker= "s", color= "red") 
plt.title("Fuel consumption at different Fuel Price") 
plt.xlabel("Fuel Price")
plt.ylabel("Fuel Consumption")
plt.show()
''' ,
13 : '''
# import the library to print Bubble chart 
import matplotlib.pyplot as plt
year = [1995,1996,1997,2000,2001,2002,2003,2004,2005]
played = [14,25,24,16,20,25,22,28,22]
wins = [3,6,8,5,6,9,11,15,12]
plt.scatter(year,played,c=wins,s=300,alpha=0.8) 
plt.title("Matches played in year 1995 to 2005") 
plt.xlabel("Year")
plt.ylabel("Matches played") 
plt.colorbar()
plt.grid()
plt.show()
''' ,
14 : '''
#import the library
import matplotlib.pyplot as plt
#Create list for data
mon=['March','April','May','June','July','August'] 
jeans=[1500,3500,6500,6700,6000,6800] 
tshirt=[4400,4500,5500,6000,5600,6300] 
shirt=[6500,5000,5800,6300,6200,4500]
plt.plot(mon,jeans,color='green',linestyle='dashed',label='Jeans') 
plt.plot(mon,tshirt,color='red',linestyle='dashed',label='T-Shirts') 
plt.plot(mon,shirt,color='blue',linestyle='dashed',label='Shirt')
#Giving title for the graph
plt.title("Apna Bazar Garments - Sales graph") 
plt.xlabel("Months")
plt.ylabel('Garments')
plt.legend() 
plt.show()
''' ,
15 : '''
#import the library
import matplotlib.pyplot as plt 
classes = [6,7,8,9,10]
average = [67,72,62,68,78]
plt.bar(classes,average,color=('black','red','green','cyan','yellow')) 
plt.yticks(range(0,100,5))
plt.xlabel('CLASSES') 
plt.ylabel('AVERAGE MARKS')
plt.title('UNIT TEST CLASS AVERAGE MARKS OF CLASSES 6 TO 10')
plt.show()
''' ,
16: '''
#import library
import matplotlib.pyplot as plt
label = ['By bus', 'By Walk','By Bicycle','By Car'] 
values = [60,240,150,50]
col = ['red','green','cyan','blue']
plt.pie(values, labels=label,colors=col)
plt.title('Student mode of Transport to school')
plt.show()'''
}
filepath = str(input("Enter the filepath for the codes : "))
for i in range(5):
    code = int(input("Enter the chosen code no.s (only enter numbers 1-16 pls) : "))
    with open(str(f"C:\\Users\\deepa\\Desktop\\{code}.py"), "a") as f:
        text = list(codes.values())[code-1]
        f.write(text)
        f.close()