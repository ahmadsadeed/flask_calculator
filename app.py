from flask import Flask, session, render_template, request
from calculator import Operation

app = Flask(__name__)
app.secret_key = 'best_secret'


@app.route('/')
def home():
    return render_template('calculate.html')


@app.route('/calculate')
def calculate():
    return render_template('calculate.html')


@app.route('/results', methods=['POST'])
def get_result():
    num1 = request.form['num1']
    num2 = request.form['num2']
    operator = request.form['operator']

    try:
        task = Operation(num1, num2, operator)
        task.operate()
        op = str(task.a) + " " + operator + " " + str(task.b) + " = " + str(task.result)

        # add the task to history dict which is in session
        if "history" in session.keys():
            dic = session.get("history")
            dic[op] = None
            session["history"] = dic
        else:
            session["history"] = dict()
            dic = dict()
            dic[op] = None
            session["history"] = dic

        return render_template('calculate.html', num1_flt=task.a, num2_flt=task.b,
                               operator=operator, output=task.result, has_result=True)

    except ZeroDivisionError:
        msg = "Can't divide by zero"
        return render_template('calculate.html', has_result=False, error=msg)

    except ValueError:
        msg = "Invalid input! Please enter numbers only."
        return render_template('calculate.html', has_result=False, error=msg)


@app.route('/history', methods=['POST', 'GET'])
def history():
    if request.method == 'POST':
        if 'clear' in request.form.keys():
            if "history" in session.keys():
                session.pop("history")
            return render_template('history.html', keys=None)
    else:
        if "history" in session.keys():
            return render_template('history.html', keys=session.get("history"))
        else:
            return render_template('history.html')


@app.errorhandler(404)
def page_not_found():
    return render_template('page404.html'), 404


if __name__ == '__main__':
    app.run()
