import string
import secrets

def pass_generator(size: int) -> str:
	alphabet = string.ascii_letters + string.digits + string.punctuation
	while True:
		password = ''.join(secrets.choice(alphabet) for i in range(size))
		if (any(c.islower() for c in password) and 
			any(c.isupper() for c in password) and 
			sum(c.isdigit() for c in password)) >= size//2:
			break
	return password

if __name__ == "__main__":
	while True:
		try:
			size = int(input("input password size: "))
			print(f'\n* Password:\n{pass_generator(size)}')
			break
		except ValueError:
			print("wrong value, please input a numeric value")
