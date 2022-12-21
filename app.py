from flask import Flask, render_template, request
import WebUtility as util

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')


@app.route('/scales', methods=['POST', 'GET'])
def scales():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"

    if request.method == 'POST':
        form_data = request.form
        form_data = dict(form_data)

        user_tuning = util.validate_tuning(form_data)
        if form_data['Root Note'] == '' or  form_data['Root Note'] == ' ':
            return render_template('base.html')

        if form_data['Tuning'] == '' or form_data['Tuning'] == ' ':
            return render_template('base.html')
        user_root = form_data['Root Note'].upper()

        form_data = util.web_data(user_root, user_tuning)

        return render_template('scales.html', form_data=form_data)


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
