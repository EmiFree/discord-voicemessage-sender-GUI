def get_token():
    with open("user_token.txt", "r") as f:
        token = f.read().strip()  # .strip() removes any extra whitespace/newlines
    return token

def save_token(token):
    with open("user_token.txt", "w") as f:
        f.write(token.strip())  # Save token, stripping any extra whitespace/newlines