from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
app.secret_key = "a good magician never reveals his secrets"


@app.route('/')
def index():
    # # checks if count is in session, increments by one when count is pressed
    # if 'count' in session:
    #     session['count'] += 1
    # else:
    #     session['count'] = 0

    # checks if count is in session, increments by TWO when count is pressed
    if 'count' in session:
        session['count'] += 2
    else:
        session['count'] = 0

    # returns template and count to index
    return render_template('index.html', count = session['count'])

# count by 1
@app.route('/count', methods=["POST"])
def count():
    print("this is the processing route")
    print(request.form)
    # redirect to index
    return redirect('/')

# count by 2
@app.route('/count2', methods=["POST"])
def count2():
    print("this is the processing route")
    print(request.form)
    # redirect to index
    return redirect('/')

# clears session
@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)