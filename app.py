from flask import Flask, request, jsonify
import subprocess
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Cache sederhana untuk menyimpan hasil pencarian sementara
cache = {
    "username": {},
    "email": {},
    "domain": {}
}

# Timeout untuk setiap proses (dalam detik)
TIMEOUT = 180

def run_sherlock(username):
    try:
        result = subprocess.run(
            ["sherlock", username, "--print-found"],
            capture_output=True,
            text=True,
            timeout=TIMEOUT
        )
        print(f"Output Sherlock untuk {username}:\n{result.stdout}")
        return result.stdout if result.stdout else "Tidak ditemukan."
    except Exception as e:
        print(f"Error Sherlock: {str(e)}")
        return f"Error: {str(e)}"

def run_holehe(email):
    try:
        result = subprocess.run(
            ["holehe", email],
            capture_output=True,
            text=True,
            timeout=TIMEOUT
        )
        print(f"Output Holehe untuk {email}:\n{result.stdout}")
        return result.stdout if result.stdout else "Tidak ditemukan."
    except Exception as e:
        print(f"Error Holehe: {str(e)}")
        return f"Error: {str(e)}"

def run_theharvester(domain):
    try:
        result = subprocess.run(
            ["python", "theHarvester.py", "-d", domain, "-b", "all"],
            capture_output=True,
            text=True,
            cwd="theHarvester",
            timeout=TIMEOUT
        )
        print(f"Output TheHarvester untuk {domain}:\n{result.stdout}")
        return result.stdout if result.stdout else "Tidak ditemukan."
    except Exception as e:
        print(f"Error TheHarvester: {str(e)}")
        return f"Error: {str(e)}"

@app.route("/")
def home():
    return "Welcome to OSINT API!"

@app.route("/search/username", methods=["GET"])
def search_username():
    username = request.args.get("username")
    if not username:
        return jsonify({"error": "Username diperlukan!"}), 400

    # Cek cache
    if username in cache["username"]:
        return jsonify({"username": username, "result": cache["username"][username]})
    
    result = run_sherlock(username)
    cache["username"][username] = result
    return jsonify({"username": username, "result": result})

@app.route("/search/email", methods=["GET"])
def search_email():
    email = request.args.get("email")
    if not email:
        return jsonify({"error": "Email diperlukan!"}), 400

    if email in cache["email"]:
        return jsonify({"email": email, "result": cache["email"][email]})
    
    result = run_holehe(email)
    cache["email"][email] = result
    return jsonify({"email": email, "result": result})

@app.route("/search/domain", methods=["GET"])
def search_domain():
    domain = request.args.get("domain")
    if not domain:
        return jsonify({"error": "Domain diperlukan!"}), 400

    if domain in cache["domain"]:
        return jsonify({"domain": domain, "result": cache["domain"][domain]})
    
    result = run_theharvester(domain)
    cache["domain"][domain] = result
    return jsonify({"domain": domain, "result": result})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
