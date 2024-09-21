# LIST 

list = [1, 2, 3, 4, 5]
list.append(6)
list.remove(1)
print(list) #[2, 3, 4, 5, 6]

total = sum(list)
print(f"TOTAL:", total) #TOTAL: 20

for n in list:
    print(n) # print the list of numbers in line


# TUPLE

locations = {
    ("Paris", "France"): "Eiffel Tower",
    ("New York", "USA"): "Statue of Liberty"
}

print(locations)

# def modify_tuple(tupl, elem):
#     tuple_to_list = list(tupl)
#     list_with_new_elem = tuple_to_list.append(elem)
#     back_to_tuple = tuple(list_with_new_elem)
#     return back_to_tuple

tuple = (1,2,3)
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