# Initialize an empty dictionary
phone_book = {}

# Read number of entries
n = int(input())

# Read the entries and populate the dictionary
for _ in range(n):
    entry = input().split()
    name = entry[0]
    phone_number = entry[1]
    phone_book[name] = phone_number

# Read and process queries
queries = []
while True:
    try:
        query = input().strip()
        if query:
            queries.append(query)
        else:
            break
    except EOFError:
        break

# Output the results
for query in queries:
    if query in phone_book:
        print(f"{query}={phone_book[query]}")
    else:
        print("Not found")
