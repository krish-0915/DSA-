from datetime import datetime

class BettingSystem:
    def __init__(self):
        self.events = {}
        self.history = []
        self.balance = 1000.0
        self.bet_id = 0
    
    def add_event(self, event_id, sport, team1, team2, odds1, odds2):
        self.events[event_id] = {
            'id': event_id,
            'sport': sport,
            'team1': team1,
            'team2': team2,
            'odds1': odds1,
            'odds2': odds2
        }
    
    def place_bet(self, event_id, amount, team_idx):
        if event_id not in self.events:
            return {'success': False, 'message': 'Event not found'}
        
        if amount > self.balance:
            return {'success': False, 'message': 'Not enough balance'}
        
        if amount <= 0:
            return {'success': False, 'message': 'Amount must be positive'}
        
        event = self.events[event_id]
        odds = event['odds1'] if team_idx == 0 else event['odds2']
        team = event['team1'] if team_idx == 0 else event['team2']
        
        self.balance -= amount
        self.bet_id += 1
        
        bet = {
            'id': self.bet_id,
            'event_id': event_id,
            'team': team,
            'amount': amount,
            'odds': odds,
            'potential_win': amount * odds,
            'date': datetime.now().strftime('%Y-%m-%d %H:%M')
        }
        
        self.history.append(bet)
        
        return {
            'success': True,
            'message': f'Bet placed on {team}',
            'balance': round(self.balance, 2),
            'potential_win': round(amount * odds, 2)
        }
    
    def get_all_events(self):
        return list(self.events.values())
    
    def get_history(self):
        return self.history
