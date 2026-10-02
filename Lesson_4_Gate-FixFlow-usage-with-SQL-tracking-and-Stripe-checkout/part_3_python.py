def initialize_database():

    conn = sqlite3.connect('users.db')

    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS users

        (id INTEGER PRIMARY KEY,

         user_hash TEXT UNIQUE,

         visits INTEGER)''')

    conn.commit()

    conn.close()



app = Flask(__name__)

initialize_database()  # creates users.db on first run
