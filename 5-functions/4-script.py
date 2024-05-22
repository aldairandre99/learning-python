import base64

def encrypt_pass(password):
  encoded_bytes = base64.b64encode(password.encode())
  print(f'\n{encoded_bytes}\n')

user_pass = input('\nEnter your password: ')

encrypt_pass(user_pass)