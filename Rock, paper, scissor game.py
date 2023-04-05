import random


def play():
    print(" ")
    get_imoji = print("To get Imoji press 'windows key' + ':' key ")
    print(" ")
    user = input("| (✊)rock , (✋)paper , (✌)scissor :\n").upper()
    computer = random.choice(['✊', '✋', '✌'])

    if user == computer:
        return 'It\'a tie'

    # r > s , s > p , p > r
    if is_win(user, computer):
        print(f"You put {user} and Computer put {computer}")
        return 'You won!'

    print(f"You put {user} and Computer put {computer}")
    return 'You lost!'

def is_win(player, opponent):
    # return true if player wins
    # r > s , s > p , p > r
    if (player == '✊' and opponent == '✌') or (player == '✌' and opponent == '✋') \
            or (player == '✋' and opponent == '✊'):
        return True
print(play())
