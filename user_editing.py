from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DATABASE = "users.db"

def access_row(username):
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute("SELECT id, username, auth FROM users WHERE username = ?", (username,))
    row = cur.fetchone()
    conn.close()
    return row

def update_auth(username, new_auth):
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute("UPDATE users SET auth = ? WHERE username = ?", (new_auth, username))
    conn.commit()
    updated = cur.rowcount
    conn.close()
    return updated > 0

@app.route("/revise", methods=["GET"])
def edit_request():
    username = request.args.get("username")
    auth = request.args.get("auth")

    if not username:
        return jsonify(["Error", "Missing username"]), 400

    user = access_row(username)
    if not user:
        return jsonify(["Error", "User not found"]), 404

    if auth:
        if update_auth(username, auth):
            return jsonify([user[0], username, auth]), 200
        else:
            return jsonify(["Error", "Failed to update auth"]), 400

    return jsonify(list(user)), 200

if __name__ == "__main__":
    app.run(debug=True)

