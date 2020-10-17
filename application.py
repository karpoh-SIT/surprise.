from flask import Flask , render_template, request, redirect

application = app = Flask(__name__)
@app.route('/')
def home():
    return render_template('login.html')

@app.route('/validate', methods=['GET','POST'])
def validate():
        if request.method == "POST":
            username = request.form['username']
            password = request.form['password']

            if username == 'chowqing' and password == "karpoh" :
                return render_template('index.html')
        return render_template('login.html')


if __name__ == '__main__':
    app.run()
