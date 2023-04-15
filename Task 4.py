###-------Question3------
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# Read the text file
with open("E:\FCAI DU\Third Year\Second Term\IR\IR Task\List of largest Internet companies.csv", 'r') as f:
    text = f.read()

# Tokenize the text
tokens = word_tokenize(text)
print('\n','\n','---------------------------------------------------Tokenization-----------------------------------','\n','\n', tokens, '\n', '\n')

# Remove stop words
stop_words = set(stopwords.words('english'))
filtered_tokens = [token for token in tokens if token.lower() not in stop_words]
print('\n',"---------------------------------------Without stop word----------------------------------",'\n','\n',filtered_tokens,'\n','\n')

# Stem the tokens
stemmer = PorterStemmer()
stemmed_tokens = [stemmer.stem(token) for token in filtered_tokens]
print('\n',"-----------------------------------------Stemmer text--------------------------------------------------",'\n','\n',stemmed_tokens, '\n', '\n')


###-------Question1------
lst = [1, 2, 3, 4, 5, 6, 7]
def hash_key(v, lst):
    m = len(lst)
    return v % m
print(hash_key(3, lst),'\n')

###------Question2----------
def hash_function(key):
    return key % 5

hash_table = [[] for _ in range(5)]
value_list = [3, 2, 9, 11, 7]

for value in value_list:
    key = hash_function(value)
    hash_table[key].append(value)

while True:
    print("Choose one of the following options:")
    print("1. Construct the whole hash table")
    print("2. Add a new element to the hash table")
    print("3. Update a value of a certain key")
    print("4. Delete an element from the hash table")
    print("5. Search for an element in the hash table")
    print("6. Print all elements with their keys of the hash table")

    choice = int(input())

    if choice == 1:
        print(hash_table)
    
    elif choice == 2:
        value = int(input("Enter a new value: "))
        key = hash_function(value)
        hash_table[key].append(value)

    
    elif choice == 3:
        key = int(input("Enter a key to update: "))
        if len(hash_table[key]) > 0:
            value = int(input("Enter a new value: "))
            index = hash_table[key].index(key)
            hash_table[key][index] = value
        else:
            print("Key not found.")
    
    elif choice == 4:
        key = int(input("Enter a key to delete: "))
        if len(hash_table[key]) > 0:
            value = int(input(f"Which value do you want to delete from {hash_table[key]}? "))
            index = hash_table[key].index(value)
            del hash_table[key][index]
            print(f"{value} deleted from {key}.")
        else:
            print("Key not found.")
    
    elif choice == 5:
        value = int(input("Enter a value to search for: "))
        key = hash_function(value)
        if value in hash_table[key]:
            print(f"{value} found at key {key}.")
        else:
            print(f"{value} not found.")
    
    elif choice == 6:
        for key, values in enumerate(hash_table):
            print(f"Key {key}: {values}")
    
    else:
        print("Invalid choice. Please choose again.")



