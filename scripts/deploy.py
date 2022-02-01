from brownie import FundMe, accounts, network, config
from scripts.helpful_scripts import get_account

def deploy_fundme():
    owner = get_account()
    FundMe.deploy({"from": owner})

def main():
    deploy_fundme()