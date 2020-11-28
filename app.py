from flask import Flask, render_template, url_for, request, redirect
import secrets
import string

app = Flask(__name__)

def pass_generator(size: int) -> str:
	alphabet = string.ascii_letters + string.digits + string.punctuation
	while True:
		password = ''.join(secrets.choice(alphabet) for i in range(size))
		if (any(c.islower() for c in password) and 
			any(c.isupper() for c in password) and 
			sum(c.isdigit() for c in password)) >= size//2:
			break
	return password

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        if request.form['length'].isnumeric():
            length = int(request.form['length'])
            if length <= 2 :
                return render_template('index.html', error='The length of the password must be longer')
            else:    
                length_password = pass_generator(length)
                return render_template('index.html', length_password=length_password)   
        else:
            print(f"error the user input a letter {request.form['length']}")
            return render_template('index.html', error='please input a number')
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run()