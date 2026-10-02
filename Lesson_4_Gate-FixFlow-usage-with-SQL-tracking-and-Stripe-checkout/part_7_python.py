# inside Code Fix, after user_hash = H1

conn = sqlite3.connect('users.db')

cursor = conn.cursor()

cursor.execute(

    'SELECT visits FROM users WHERE user_hash = ?',

    (user_hash,))

row = cursor.fetchone()

conn.close()

visits = row[0] if row else 0

if visits >= 3:

    return redirect('/checkout')  # no model calls

record_visit(user_hash)

# then staged fix + explain completions
