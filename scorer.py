"""Main bowling scorer program"""

import sys

def main():
    script = sys.argv[0]
    try:
        sequence = sys.argv[1]
        print(f'Sequence: {sequence}, score: {scorer(sequence)}')
    except IndexError:
        print('Enter the sequence to evaluate: ')
        print(f'Score: {scorer(input())}')
        

def converter(seq):
    """
    Given a string of symbols, uses bowling rules to convert 'X' and '/' to '10' 
    and sums it up with other numbers in the string. 
    """
    seq = ''.join(seq.split('-'))
    score = 0
    for s in seq:
        if s.isdigit():
            score += int(s)
        else:
            score += 10
    return score
    
def scorer(sequence):
    """
    Bowling game calculator function. 
    DOES NOT check for validity.

    Input
    ------
    sequence : String of 'throws' 
    """
    Score = 0
    Frame = 0
    i = 0
    for i in range(len(sequence)):
        if Frame == 10: break
        throw = sequence[i] 
        if throw.isdigit():
            Score += int(throw)
        elif throw == '/':
            Score += (10-int(sequence[i-1])) + converter(sequence[i+2])
        elif throw == 'X':
            Score += 10 + converter(sequence[i+2:i+5])
        elif throw == '-':
            Frame += 1        
        i += 1
    return Score

if __name__ == '__main__':
    main()