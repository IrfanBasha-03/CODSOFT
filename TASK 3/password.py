import random

def generate_password(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    password = "".join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Simple Password Generator!")
    length = int(input("Enter the desired length of your password: "))
    
    if length < 6:
        print("Password length should be at least 6 characters for security.")
    else:
        password = generate_password(length)
        print(f"Your generated password is: {password}")

if __name__ == "__main__":
    main()
