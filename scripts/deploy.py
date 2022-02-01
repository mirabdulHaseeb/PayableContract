from brownie import FundMe, accounts, network, config

def deploy_fundme():
    owner = get_account()
    FundMe.deploy({"from": owner})

def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def main():
    deploy_fundme()