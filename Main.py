#cs3620 coding challenge 1

#--------------------------< Part 1 >------------------------------
#get user input
p = int(input("Enter the principal: "))
n = int(input("Enter the Number of years: "))
r = int(input("Enter the interest % (as a whole number): ")) / 100

#calculate and print
print(p * r * n)
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

#insert and print new item at [3]
foodItems.insert(3,"tacos")
print(foodItems)

#---------------------------< Part 3 >--------------------------

#print from loop
for i in range(5):
    print("I am a programmer.")


#define function
def printSquares():
    for i in range(10):
        if(i > 0):
            print(i**2)

#call function
printSquares()