"""
python like different programming languages 
have 0 based indexing
1st element at 0th index
2nd element at 1st index

positive indexing 
left to right
1st element at 0th index

negative indexing
right to left
-1st element at -1st index
-2nd element at -2nd index

updating elements using list
assigning new value to existing index
"""

marks = [10, 20, 30, 40, 50]
print(f"Original list: {marks}")
marks[0] = 15  # Updating the first element
marks[-1] = 55  # Updating the last element
print(f"Updated list: {marks}")

"""

create a list of five of ur favorite movies
print 1st last and middle movie from your list
using positive and negative indexing
n/2 = something 9.6
n//2 = something 9

"""

movies = ["Inception", "The Matrix", "Interstellar", "The Dark Knight", "Pulp Fiction"]
len_movies = len(movies)
if len_movies % 2 == 0:
    middle_index = len_movies // 2 - 1
else:
    middle_index = len_movies // 2
    
print(f"First movie (positive indexing): {movies[0]}")

print(f"Middle movie (positive indexing): {movies[middle_index]}")

print(f"Last movie (negative indexing): {movies[-1]}")
