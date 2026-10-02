@app.route('/payment-success')

def payment_success():

    user_id = session.get('email', 'dev@fixflow.test')

    user_hash = hashlib.sha256(user_id.encode()).hexdigest()

    conn = sqlite3.connect('users.db')

    cursor = conn.cursor()

    cursor.execute(

        'UPDATE users SET visits = 0 WHERE user_hash = ?',

        (user_hash,))

    conn.commit()

    conn.close()

    return 'Payment recorded; Code Fix unlocked.'
