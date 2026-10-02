user_id = session.get('email', 'dev@fixflow.test')

user_hash = hashlib.sha256(user_id.encode()).hexdigest()  # H1



def record_visit(user_hash):

    conn = sqlite3.connect('users.db')

    cursor = conn.cursor()

    cursor.execute(

        'SELECT visits FROM users WHERE user_hash = ?',

        (user_hash,))

    row = cursor.fetchone()

    if row is None:

        cursor.execute(

            'INSERT INTO users (user_hash, visits) VALUES (?, ?)',

            (user_hash, 1))

    else:

        cursor.execute(

            'UPDATE users SET visits = ? WHERE user_hash = ?',

            (row[0] + 1, user_hash))

    conn.commit()

    conn.close()
