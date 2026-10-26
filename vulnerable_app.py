import sqlite3

# FAKE AWS KEY (Our Secret Scanning tool should catch this later)
AWS_ACCESS_KEY_ID = "AKIA5HTUX2R4B5JW7C9Y"

def get_user_data(username):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # VULNERABILITY: SQL Injection (Our SAST tool should catch this later)
    query = f"SELECT * FROM users WHERE username = '{username}'"
    
    cursor.execute(query)
    return cursor.fetchall()

if __name__ == "__main__":
    print(get_user_data("admin"))