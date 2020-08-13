import random
import sqlite3

card_name = []


def creat_card():
    card_number = '400000' + str(random.randint(100000000, 999999999))
    card_fix = card_number
    for i in range(0, 16, 2):
        x = int(card_fix[i]) * 2
        if x <= 9:
            card_fix = card_fix[:i] + str(x) + card_fix[i + 1:]
        else:
            x -= 9
            card_fix = card_fix[:i] + str(x) + card_fix[i + 1:]
    if (10 - (sum([int(x) for x in card_fix]) % 10)) == 10:
        card_number = int(card_number + '0')
    else:
        card_number = int(card_number + str(10 - (sum([int(x) for x in card_fix]) % 10)))
    card_pin = random.randint(1000, 9999)
    print('\nYour card has been created')
    print('Your card number', card_number, sep="\n")
    print('Your card PIN:', card_pin, sep="\n")
    balance = 0
    card_name.append([str(card_number), str(card_pin)])
    with conn:
        cursor.execute('INSERT INTO card(number, pin, balance) VALUES(?, ?, ?)',
                       (str(card_number), str(card_pin), balance))


def chek_user():
    card_number = input('\nEnter your card number:')
    card_pin = input('Enter your PIN:')
    if [card_number, card_pin] in card_name:
        print('\nYou have successfully logged in!\n')
        return card_number, card_pin
    else:
        print('\nWrong card number or PIN!\n')


def main_input():
    return int(input('''1. Create an account
2. Log into account
0. Exit\n'''))


def activ_user_menu():
    return int(input('''1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit\n'''))


def balance(active_user_number):
    [balance], = cursor.execute('SELECT balance FROM card WHERE number=?', (active_user_number,))
    print(f'Balance: {balance}')


def add_income(active_user_number):
    with conn:
        incom = int(input('Enter income:'))
        [balance], = cursor.execute('SELECT balance FROM card WHERE number=?', (active_user_number,))
        incom += balance
        cursor.execute('UPDATE card SET balance=? WHERE number=?', (incom, active_user_number))
        print('Income was added!\n')


def do_transfer(active_user_number):
    with conn:
        to_card_number = input('Transfer\nEnter card number:')
        [balance], = cursor.execute('SELECT balance FROM card WHERE number=?', (active_user_number,))
        if active_user_number == to_card_number:
            print("You can't transfer money to the same account!")
        elif not chek_al_luna(to_card_number):
            print("Probably you made mistake in card number. Please try again!")
        elif to_card_number not in [x[0] for x in cursor.execute('SELECT number FROM card')]:
            print("Such a card does not exist.")
        else:
            money_to_transfer = int(input('Enter how much money you want to transfer:\n'))
            if money_to_transfer > balance:
                print('Not enough money!\n')
            else:
                cursor.execute('UPDATE card SET balance=? WHERE number=?',
                               (balance - money_to_transfer, active_user_number))
                [balance1], = cursor.execute('SELECT balance FROM card WHERE number=?', (to_card_number,))
                cursor.execute('UPDATE card SET balance=? WHERE number=?',
                               (balance1 + money_to_transfer, to_card_number))
                print('Success!')


def chek_al_luna(card_number):
    card_fix = card_number[0:-1]
    for i in range(0, 16, 2):
        x = int(card_fix[i]) * 2
        if x <= 9:
            card_fix = card_fix[:i] + str(x) + card_fix[i + 1:]
        else:
            x -= 9
            card_fix = card_fix[:i] + str(x) + card_fix[i + 1:]
    if (10 - (sum([int(x) for x in card_fix]) % 10)) == 10:
        last_num = '0'
    else:
        last_num = str(10 - (sum([int(x) for x in card_fix]) % 10))
    card_fix = card_number[0:-1]
    if card_fix + last_num == card_number:
        return True
    else:
        return False


def del_account(us_number):
    with conn:
        cursor.execute('DELETE FROM card WHERE number =?', (us_number,))
        print('The account has been closed!')


conn = sqlite3.connect('card.s3db')
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS card 
                  (`id` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL , number text, pin text,
                   balance integer)
               """)

while True:

    stat = main_input()
    if stat == 0:
        print('\nBay!')
        break
    elif stat == 1:
        creat_card()
    elif stat == 2:
        try:
            active_user_number, active_pin_user = chek_user()
        except TypeError:
            continue
        while True:
            us_in = activ_user_menu()
            if us_in == 1:
                balance(active_user_number)
            elif us_in == 2:
                add_income(active_user_number)
            elif us_in == 3:
                do_transfer(active_user_number)
            elif us_in == 4:
                del_account(active_user_number)
                break
            elif us_in == 5:
                break
            elif us_in == 0:
                print('\nBay!')
                exit()

    print()

conn.commit()
conn.close()
