from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DB_FILE = "users.db"

def access_row(username):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT id, username, year, auth FROM users WHERE username = ?", (username,))
    row = cursor.fetchone()
    conn.close()
    return row

def update_auth(username, new_auth):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET auth = ? WHERE username = ?", (new_auth, username))
    conn.commit()
    cursor.execute("SELECT id, username, year, auth FROM users WHERE username = ?", (username,))
    row = cursor.fetchone()
    conn.close()
    return row

@app.route("/")
def index():
    return jsonify({"message": "Welcome to the users database"})

@app.route("/revise", methods=["GET"])
def revise():
    username = request.args.get("username")
    new_auth = request.args.get("auth")

    if not username:
        return jsonify({"error": "No username provided"}), 400

    row = access_row(username)

    if row:
        if new_auth:
            updated_row = update_auth(username, new_auth)
            return jsonify({
                "id": updated_row[0],
                "username": updated_row[1],
                "year": updated_row[2],
                "auth": updated_row[3]
            })
        else:
            return jsonify({
                "id": row[0],
                "username": row[1],
                "year": row[2],
                "auth": row[3]
            })
    else:
        return jsonify({"error": "User not found", "username": username}), 404

if __name__ == "__main__":
    app.run(debug=True)

