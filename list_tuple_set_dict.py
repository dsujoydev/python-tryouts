# LIST 
print("------------ LIST --------------")
numlist = [1, 2, 3, 4, 5]
numlist.append(6)
numlist.remove(1)
print(numlist) #[2, 3, 4, 5, 6]
total = sum(numlist)
print(f"TOTAL:", total) #TOTAL: 20
for n in numlist:
    print(n) # print the list of numbers in line

zillaList = list(("Dhaka", "Tangail", "Gazipur", "Sirjaganj")) #list constructor
for zilla in zillaList:
  print(zilla) 

for item in range(2,3):
   print(zillaList[item])

# TUPLE
print("------------ Tuple --------------")

locations = {
    ("Paris", "France"): "Eiffel Tower",
    ("New York", "USA"): "Statue of Liberty"
}

print(locations[("Paris", "France")])
print(locations.append({("New York", "USA"): "Statue of Liberty"}))
# countryList = tuple(("Bangladesh", "Tangail", "Gazipur", "Sirjaganj")) #list constructor
print(locations)

# def modify_tuple(tupl, elem):
#     tuple_to_list = list(tupl)
#     list_with_new_elem = tuple_to_list.append(elem)
#     back_to_tuple = tuple(list_with_new_elem)
#     return back_to_tuple

numTuple = (1,2,3)
add_element = 4

# print(modify_tuple(tuple, add_element))

#SET

set_one = {1,2,3,4,5}
set_two = {3,4,5,6,7,6,5} 
print(set_two) # it doesn't contain duplicates
set_one.add(6)
set_two.add(8)
set_two.discard(6)
print(set_one, set_two)
print (set_one.union(set_two))
print (set_one.intersection(set_two))
print (set_one.difference(set_two))

# Dictionary 
country_capitals = {
  "Germany": "Berlin", 
  "Bangladesh": "Dhaka", 
  "England": "London"
}

print(country_capitals["Bangladesh"])
country_capitals["Italy"] = "Rome"
print(country_capitals)
del country_capitals["England"]
print(country_capitals)