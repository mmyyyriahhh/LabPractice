import pytest

from bank import Account

def test_initial_balance():
    account = Account("test", 5)
    assert(account.get_balance == 5)

def test_deposit():
    account = Account("test", 20)
    assert(account.deposit(20) == 40)
    assert(account.deposit(3) == 43)
    with pytest.raises(ValueError, match="Deposit amount must be positive"):
        account.deposit(-5)
    
def test_withdraw():
    account = Account("test", 20)
    with pytest.raises(ValueError, match="Insufficient funds"):
        (account.withdraw(25))
    assert(account.withdraw(5) == 15)