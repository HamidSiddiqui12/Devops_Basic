# ATM Withdrawl Systemw

CURRENT_BALANCE = 5000

withdrawal_amount = int(input("Enter the amount to withdraw: "))

def atm_withdrawal(withdrawal_amount):
    if withdrawal_amount== 0:
        print(f"Error: Withdrawal amount must be greater than 0.\n AmountBalance: {CURRENT_BALANCE}")
    elif withdrawal_amount > 0:
        if withdrawal_amount>CURRENT_BALANCE:
            print(f"Sorry! Insufficient Amount. Balance: {CURRENT_BALANCE}")
        elif withdrawal_amount%500 == 0:
            temp_balance = CURRENT_BALANCE - withdrawal_amount
            print(f"Withdrawal successful. Amount: {withdrawal_amount}\nRemaining balance: {temp_balance}")
        elif withdrawal_amount%500 != 0:
            print("Error: Withdrawal amount must be multiple of 500")

atm_withdrawal(withdrawal_amount)