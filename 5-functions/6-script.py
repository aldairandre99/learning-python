import base64

def decrypt_pass(password):
  decoded_bytes = base64.b64decode(password)
  print(f'\n{decoded_bytes}\n')

user_pass = input('\nEnter your password: ')

decrypt_pass(user_pass)