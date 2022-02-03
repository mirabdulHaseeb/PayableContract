from brownie import FundMe, accounts, network, config
from scripts.helpful_scripts import get_account

def run_fund_me():
    account = get_account()
    fund_me = FundMe[-1]
    print(f"Version: {fund_me.getVersion()}")
    print(f"Eth Price (per dollar): {fund_me.getConversionRate(1)}")
    print(f"Balance: {fund_me.balance()}")
    amount_funded = 50000000000000000
    print(f"Funding {amount_funded} ...")
    fund_me.fund({"from": account, "value": amount_funded})
    print(f"Balance: {fund_me.balance()}")
    print("Withdraw funds ...")
    fund_me.withdraw({"from": account})
    print(f"Balance: {fund_me.balance()}")


def main():
    run_fund_me()