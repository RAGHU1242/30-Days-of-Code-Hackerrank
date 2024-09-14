import re

if __name__ == '__main__':
    N = int(input().strip())
    gmail_users = []
    
    for _ in range(N):
        firstName, emailID = input().split()
        # Regular expression to check for gmail.com domain
        if re.search(r'@gmail\.com$', emailID):
            gmail_users.append(firstName)
    
    # Sort the list alphabetically
    gmail_users.sort()
    
    # Print each name on a new line
    for user in gmail_users:
        print(user)
