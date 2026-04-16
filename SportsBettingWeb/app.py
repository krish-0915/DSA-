from flask import Flask, render_template, request, jsonify
from betting_system import BettingSystem

app = Flask(__name__)
app.secret_key = 'simple_betting_key'

betting_system = BettingSystem()

# Add sample events
betting_system.add_event('E001', 'Basketball', 'Lakers', 'Celtics', 1.85, 2.10)
betting_system.add_event('E002', 'Football', 'Arsenal', 'Liverpool', 2.80, 1.45)
betting_system.add_event('E003', 'Tennis', 'Federer', 'Nadal', 1.95, 1.92)
betting_system.add_event('E004', 'Cricket', 'India', 'Australia', 1.70, 2.30)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/api/events')
def get_events():
    return jsonify(betting_system.get_all_events())

@app.route('/api/place-bet', methods=['POST'])
def place_bet():
    data = request.json
    result = betting_system.place_bet(
        data['event_id'],
        float(data['amount']),
        int(data['team_idx'])
    )
    if result['success']:
        return jsonify(result)
    return jsonify(result), 400

@app.route('/api/history')
def get_history():
    return jsonify(betting_system.get_history())

@app.route('/api/balance')
def get_balance():
    return jsonify({'balance': betting_system.balance})

if __name__ == '__main__':
    app.run(debug=True)
