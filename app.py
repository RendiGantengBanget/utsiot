from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Route untuk menampilkan halaman HTML
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# Route untuk menyediakan data JSON
@app.route('/api/data', methods=['GET'])
def get_data():
    data = {
        "suhumax": 36,
        "suhumin": 21,
        "suhurata": 28.35,
        "nilai_suhu_max_humid_max": [
            {
                "idx": 101,
                "suhu": 36,
                "humid": 36,
                "kecerahan": 25,
                "timestamp": "2010-09-18 07:23:48"
            },
            {
                "idx": 226,
                "suhu": 36,
                "humid": 36,
                "kecerahan": 27,
                "timestamp": "2011-05-02 12:29:34"
            }
        ],
        "month_year_max": [
            {
                "month_year": "9-2010"
            },
            {
                "month_year": "5-2011"
            }
        ]
    }
    return jsonify(data)

# Menjalankan aplikasi
if __name__ == '__main__':
    app.run(debug=True)
