#
#
# Project Name:     AntMarch
# Programmer:    Woodrow Jackson
#
#
# Description: a program that tells a lyric of ants marching
def chorus(number,activity):
    print('the ants go marching', number, 'by', str(number) + ', hurrah hurrah')
    print('the ants go marching', number, 'by', str(number) + ', hurrah hurrah')
    print('the ants go marching', number, 'by', str(number) + ',')
    print('the little one stops to', activity + ',')
    print(' and they all go marching down...')
    print('In the ground...')
    print('to get out...')
    print('Of the rain.')

def main():
    numbers = [ 'one', 'two','three','four','five','six','seven','eight','nine','ten']
    activities = ['suck his thumb','tie his shoe','climb a tree','shut the door',
                  'take a dive','pick up sticks','go to heaven','shut the gate',
                  'scratch his spine','say "THE END"']

    for i in range(10):
        chorus(numbers[i], activities[i])

main()