# age = {
#     "Harry" : 20,
#     "Love" : 23,
#     "Scout" : 0
    
# };

# print(age["Harry2"]); # returns an error
# print(age.get("Harry2")) # returns None

Translation = {
    "Namaste" : "hello",
    "Thanyavad": "Thank you",
    "Bewakuff" : "Stupid"
};

word = input("Enter the word you want to translate  ")
print(Translation.get(word))
