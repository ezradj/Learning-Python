# print("Why hello there!")

food = ["pizza", "tacos", "cheeseburgers", "pasta"]

food[0] = 'sushi'

food.append("ice cream") #inserts an item at the beginning of the list
food.remove("pasta") #removes the given item
food.pop() #removes the last item in the list
food.insert(0, 'cake') #inserts a given item at the given index
food.sort() #sorts the list alphabetically
food.clear() #removes everything from the list

for x in food:
  print(x)
