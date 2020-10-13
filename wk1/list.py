my_words = ["Hello", "Python"]

for word in my_words:
    print(word)
    
    
    
print(my_words[1])

my_list = [2, 4, 6, 8]
my_element = [my_list[1],my_list[3]]
print(my_element)

my_list.append(111)
print(my_list)



phrase = "Hello Python"

for letter in phrase:
    print(letter)
    
    
    
sounds = {"cat": "meow", "dog": "woof", "horse": "neigh"}

cat_sound = sounds["cat"]

print(cat_sound)

sounds = {
    "cat": "meow",
    "dog": "woof",
    "horse": "neigh"
}

dog_sound = sounds["dog"]

print(dog_sound)


sounds = {
    "cat": "meow",
    "dog": "woof",
    "horse": "neigh"
}

sounds["cow"] = "moo"

print(sounds)


sounds = {
    "cat": "meow",
    "dog": "woof",
    "horse": "neigh"
}

for thing in sounds:
    print(thing)
    
    


sounds = {
    "cat": "meow",
    "dog": "woof",
    "horse": "neigh"
}

for animal, sound in sounds.items():
    print(animal, "goes", sound)

        
word = ["s", "u", "c", "c", "e", "s", "s", "f", "u", "l", "l", "y"]

for letter in word:
    print(letter, end="")
    ###加不加end=空，差别很大