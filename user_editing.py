from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

DB_FILE = "users.db"

def access_row(username):
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username=?", (username,))
    user = cur.fetchone()
    conn.close()
    return user

def update_auth(username, new_auth):
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()

    cur.execute("SELECT * FROM users WHERE username=?", (username,))
    user = cur.fetchone()
    if not user:
        conn.close()
        return {"error": "User not found"}, 404

    cur.execute("UPDATE users SET auth=? WHERE username=?", (new_auth, username))
    conn.commit()

    cur.execute("SELECT * FROM users WHERE username=?", (username,))
    updated_user = cur.fetchone()
    conn.close()

    return {"username": updated_user[1], "year": updated_user[2], "auth": updated_user[3]}, 200

@app.route("/revise", methods=["GET"])
def edit_request():
    username = request.args.get("username")
    auth = request.args.get("auth")

    if not username:
        return {"error": "Missing username"}, 400

    user = access_row(username)

    if not user:
        return {"error": "User not found"}, 404

    if auth:
        response, status = update_auth(username, auth)
        return jsonify(response), status

    # If no auth update, just return user info
    return jsonify({"username": user[1], "year": user[2], "auth": user[3]}), 200

if __name__ == "__main__":
    app.run(debug=True)
