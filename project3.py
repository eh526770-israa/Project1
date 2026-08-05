import random
import string


def get_password_length():
    while True:
        user_input = input("Enter the desired password length: ").strip()
        try:
            length = int(user_input)
            if length < 4:
                print("Password length must be at least 4 characters.")
                continue
            return length
        except ValueError:
            print("Please enter a valid number.")


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    return password


def main():
    print("===== RANDOM PASSWORD GENERATOR =====")

    length = get_password_length()
    password = generate_password(length)

    print("\nYour generated password is:")
    print(password)


if __name__ == "__main__":
    main()
