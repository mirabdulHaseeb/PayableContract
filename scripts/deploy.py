from brownie import FundMe, accounts

def deploy_fundme():
    owner = accounts[0]
    FundMe.deploy({"from": owner})

def main():
    deploy_fundme()