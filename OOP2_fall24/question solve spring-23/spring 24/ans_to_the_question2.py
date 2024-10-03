"""2.a

sentence = input("Enter a sentence: ")
vowels = ['a','e','i','o','u']
cnt = 0
for v in sentence.lower():
    if v in vowels:
        cnt +=1
print(f"The number of vowels in the sentence is {cnt}")
"""
"""
#2.b
def bookstore(num_of_books):
    total_cost = sum(num_of_books)
    if len(num_of_books) > 10:
        discount = 0.20
    elif 4 <= len(num_of_books) <= 10:
        discount = .10
    else:
        discount = 0

    total_payable = total_cost - (total_cost * discount)
    return total_cost, total_payable,discount
n = int(input("Enter the number of books: "))
num_of_books = []

for i in range(1, n+1):
    price = int(input(f"Enter the price of book-{i}: "))
    num_of_books.append(price)

total_cost, total_payable, discount = bookstore(num_of_books)

print(f"Total Cost: {total_cost}")
if discount > 0:
    print(f"Total Payable Cost: {total_payable}tk ({int(discount*100)}% discount applied for purchasing {len(num_of_books)} books)")
else:
    print(f"Total Payable Cost: {total_payable}tk (no discount)")

"""
#2.c
def recommendation_system(movies, user_genres):
    recommendation = {}
    for movie, genres in movies.items():
        matching_genres = len(set(genres) & set(user_genres))

        if matching_genres > 0:
            recommendation[movie] = matching_genres
    sorted_recommendations = sorted(recommendation, key=recommendation.get, reverse=True)
    return sorted_recommendations
movies = {
    "The Shawshank Redemption": ["drama"],
    "The Godfather": ["crime", "drama"],
    "The Dark Knight": ["action", "crime", "thriller"],
    "Fight Club": ["drama", "thriller"]
}

user_genres = ["action", "thriller"]
recommendation_movies = recommendation_system(movies, user_genres)
print("recommendations:", recommendation_movies)

