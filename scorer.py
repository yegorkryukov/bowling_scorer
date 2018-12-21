def converter(seq):
    seq = ''.join(seq.split('-'))
    score = 0
    for s in seq:
        if s.isdigit():
            score += int(s)
        else:
            score += 10
    return score
    
def scorer(sequence):
    Score = 0
    Frame = 0
    sequence += '00'
    i = 0
    for i in range(len(sequence)-2):
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
    print(f'For sequence "X-X-X-X-X-X-X-X-X-X-XX" the result should be "300".\n It is: {scorer("X-X-X-X-X-X-X-X-X-X-XX")}.')