#cs3620 coding challenge 1
#alexander lustig


#--------------------------< Part 1 >------------------------------
#get user input
p = int(input("Enter the principal: "))
n = int(input("Enter the Number of years: "))
r = int(input("Enter the interest % (as a whole number): "))

#calculate and print
print((p * r * n) / 100)
print("\n")

#-----------------------< Part 2 >------------------------------
#list
foodItems = ["watermelon","blue cheese","peanut butter","gummy bears","chocolate"]

#print item at 3rd position
print(foodItems[2])

#add and print new items
foodItems.append("chicken")
foodItems.append("pineapple")
foodItems.append("salmon")

print(foodItems)
print("\n")


#insert and print new item at [3]
foodItems.insert(3,"tacos")
print(foodItems)
print("\n")

#---------------------------< Part 3 >--------------------------

#print from loop
for i in range(5):
    print("I am a programmer.")

print("\n")

#define function
def printSquares():
    for i in range(10):
        if(i > 0):
            print(i**2)

#call function
printSquares()