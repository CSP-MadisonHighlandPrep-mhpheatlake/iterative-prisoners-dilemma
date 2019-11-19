####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'E6'
strategy_name = 'Collude until betrayed'
strategy_description = '''\
Collude first round. Collude, unless betrayed; then always betray.'''
    
def move(my_history, their_history, my_score, their_score):
    if len(my_history)==0:
        return 'c'
    elif len(my_history)<5 & len(my_history)>0:
        if my_history[-1]=='c' and their_history[-1]=='b':
            return 'b'
        else:
            return 'c'
            
    last6rounds = their_history[-6:]
    
    n = 0
    for c in last6rounds:
        n=n+1
        print(n)
    
    if n/6 < 0.5:
        return 'c' # Betray if severely punished last time,
    else:
        return 'b' # otherwise collude