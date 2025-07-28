input = "Hello Hello World. This is a fantastic world"

def number_of_words(input):
    words = input.split()
    return len(words)

def unique_words(input):
    words = input.split()
    unique = set(words)
    return len(unique)

def most_common_words(input):
    array = {}
    words  = input.split()
    for word in words:
        if( word in array):
            array[word] += 1
        else:
            array[word] = 1
    return array 

print (number_of_words(input))
print (unique_words(input))
print (most_common_words(input))