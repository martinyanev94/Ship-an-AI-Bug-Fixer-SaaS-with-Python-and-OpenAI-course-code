@app.route('/fix', methods=['POST'])

def fix_code():

    buggy_code = request.form['code']

    error_message = request.form['error']

    fix_messages = [{

        'role': 'user',

        'content': f'Fix this code. Error: {error_message}\n\n{buggy_code}'

    }]

    explain_messages = [{

        'role': 'user',

        'content': f'Explain this error in plain English. Error: {error_message}\n\n{buggy_code}'

    }]
