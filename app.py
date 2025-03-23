from flask import Flask, request, jsonify

app = Flask(__name__)

# Przykładowe kody starterpacków
codes = {
    "A1B2C3": {"used": False, "user_id": 123456789012345678}
}

@app.route("/api/verify", methods=["POST"])
def verify():
    data = request.json
    nickname = data.get("nickname")
    code = data.get("code")

    if code not in codes or codes[code]["used"]:
        return jsonify({"message": "❌ Invalid or used code."})

    codes[code]["used"] = True

    print(f"✅ SPAWN STARTERPACK for {nickname}")

    return jsonify({"message": "✅ StarterPack will be delivered shortly. Stay still!"})

if __name__ == "__main__":
    app.run()
