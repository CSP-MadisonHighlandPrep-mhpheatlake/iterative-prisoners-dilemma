####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'E8'
strategy_name = 'Use early history'
strategy_description = '''\
Randomly select to collude or betry. Compare the previous example betrayed, 
then betray every time. Unless their previous history is collude then collude, 
until betrayed.
'''
    
def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''
    if len(my_history)==0: # It's the first round: collude
        return 'c'
    while len(my_history)>=1:
        # If the round is anyround other than the first round,
        # either randomly pick if their history is c otherwise b
        
        # Reference last round
        recent_round_them = their_history[-1]
        recent_round_me = my_history[-1]
                    
        # Look at rounds before that one
        for round in range(len(my_history)-1):
            prior_round_them = their_history[round]
            prior_round_me = my_history[round]
            # If one matches
            if (prior_round_me == recent_round_me) and \
                    (prior_round_them == recent_round_them):
                return their_history[round]
        # No match found
        while 'c' == their_history:
            if their_history == 'c':
                import random 
                return random.choice('cb') # Betray if they were severely punished last time
            else:
                return 'b'
       
        while 'b' == their_history:
            return 'b'
    