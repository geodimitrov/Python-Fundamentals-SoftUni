
tickets = input().split(", ")


winning_symbols = ['@', '#', '$', '^']
    
def is_jackpot(ticket):
    for winning_symbol in winning_symbols:
        if winning_symbol * 20 == ticket:
            print(f'ticket "{ticket}" - 10{winning_symbol} Jackpot!')
            return True
    return False

def is_valid(ticket):
    left_side = ticket[0:10]
    right_side = ticket[10:20]
    for winning_symbol in winning_symbols:
        if winning_symbol * 6 in left_side and winning_symbol * 6 in right_side:
            if left_side.count(winning_symbol) >= right_side.count(winning_symbol):
                count = right_side.count(winning_symbol)
            else:
                count = left_side.count(winning_symbol)
            print(f'ticket "{ticket}" - {count}{winning_symbol}')
            return True
    return False

for t in tickets:
    ticket = t.strip()
    
    if len(ticket) == 20:
        if is_jackpot(ticket):
            continue
        elif is_valid(ticket):
            continue
        else:
            print(f'ticket "{ticket}" - no match')
            
    else:
        print("invalid ticket")
