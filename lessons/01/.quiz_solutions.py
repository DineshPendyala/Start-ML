def vowel_count(string):
    vowels = ['a','e','i','o','u']
    vowel_count = 0
    for v in vowels:
        vowel_count += string.count(v)
    return(vowel_count)
            
string = 'Hey you guys!'
print(vowel_count(string))


def animals_to_upper(animals):
    for animal in animals:
        print(animal.upper())
        
animals = ['Lions', 'Tigers', 'Bears', 'Chihuahuas']
animals_to_upper(animals)
