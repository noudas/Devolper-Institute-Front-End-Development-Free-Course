'''
Write the following Python code to do the following (complete ALL of these using list comprehension).

1 Given a list [1,2,3,4], print out all the values in the list.

2 Given a list [1,2,3,4], print out all the values in the list multiplied by 20.

3 Given a list [“Elie”, “Tim”, “Matt”], return a new list with only the first letter ([“E”, “T”, “M”]).

4 Given a list [1,2,3,4,5,6] return a new list of all the even values ([2,4,6]).

5 Given two lists [1,2,3,4] and [3,4,5,6], return a new list that is the intersection of the two ([3,4]).

6 Given a list of words [“Elie”, “Tim”, “Matt”] return a new list with each word reversed and in lower case ([‘eile’, ‘mit’, ‘ttam’]).

7 Given two strings “first” and “third”, return a new string with all the letters present in both words ([“i”, “r”, “t”]).

8 For all the numbers between 1 and 100, return a list with all the numbers that are divisible by 12 ([12, 24, 36, 48, 60, 72, 84, 96]).

9 Given the string “amazing”, return a list with all the vowels removed ([‘m’, ‘z’, ‘n’, ‘g’]).

10 Generate a list with the value [[0, 1, 2], [0, 1, 2], [0, 1, 2]].

11 Generate a list with the value:

[
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
]

'''

list_1 = [1, 2, 3, 4]
print([x for x in list_1])


print([x * 20 for x in list_1])


list_2 = ["Elie", "Tim", "Matt"]
first_letters = [name[0] for name in list_2]
print(first_letters)


list_3 = [1, 2, 3, 4, 5, 6]
evens = [x for x in list_3 if x % 2 == 0]
print(evens)


list_4a = [1, 2, 3, 4]
list_4b = [3, 4, 5, 6]
intersection = [x for x in list_4a if x in list_4b]
print(intersection)


reversed_words = [word[::-1].lower() for word in list_2]
print(reversed_words)


string_1 = "first"
string_2 = "third"
common_letters = [char for char in string_1 if char in string_2]
print(common_letters)


div_by_12 = [x for x in range(1, 101) if x % 12 == 0]
print(div_by_12)


string_3 = "amazing"
vowels = "aeiou"
no_vowels = [char for char in string_3 if char not in vowels]
print(no_vowels)


list_10 = [[x for x in range(3)] for _ in range(3)]
print(list_10)

list_11 = [[x for x in range(10)] for _ in range(10)]
print(list_11)