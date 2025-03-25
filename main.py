users = [
    {"nickname": "Alex", "age": 50, "rating": 4.3},
    {"nickname": "Yulia", "age": 26, "rating": 3.2},
    {"nickname": "Sveta", "age": 32, "rating": 5.0},
    {"nickname": "Katya", "age": 23, "rating": 4.8},
    {"nickname": "Sasha", "age": 84, "rating": 1.2}
]

for user in users:
    if user["age"] > 80:
        user["premium"] = True
