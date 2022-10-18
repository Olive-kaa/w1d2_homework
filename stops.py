stops_list = [ "Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket"]

#1. Add "Edinburgh Waverley" to the end of the list
#2. Add "Glasgow Queen St" to the start of the list
#3. Add "Polmont" at the appropriate point (between "Falkirk High" and "Linlithgow")stops_list.append("Edinburgh Waverley")
stops_list.insert(0, "Glasgow Queen St")
stops_list.insert(4, "Polmount")

#4. Print out the index position of "Linlithgow"
stop = "Linlithgow"
print(f"The index position of {stop} is: ")
print(stops_list.index(stop))

#5. Remove "Livingston" from the list using its name
stops_list.remove("Livingston")

#6. Delete "Cumbernauld" from the list by index
stop = "Cumbernauld"
position = int(stops_list.index(stop))
del stops_list[position]

#7. Print the number of stops there are in the list
print("The number of stops is: ")
print(len(stops_list))

#8. Sort the list alphabetically
alph_list = sorted(stops_list)
print(alph_list)

#9. Reverse the positions of the stops in the list
alph_list = sorted(stops_list, reverse = True)
print(alph_list)

#10 Print out all the stops using a for loop
for stop in stops_list:
    print(stop)