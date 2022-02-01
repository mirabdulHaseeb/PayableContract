from brownie import FundMe, accounts, network, config
from scripts.helpful_scripts import get_account

def run_fund_me():
    account = get_account()
    fund_me = FundMe[-1]
    print(f"Version: {fund_me.getVersion()}")
    print(f"Eth Price (per dollar): {fund_me.getConversionRate(1)}")

def main():
    run_fund_me()