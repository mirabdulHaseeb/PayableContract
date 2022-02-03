from brownie import FundMe, MockV3Aggregator, accounts, network, config
from scripts.helpful_scripts import (
    get_account, 
    deploy_mocks, 
    LOCAL_BLOCKCHAIN_ENVIRONMENTS
)

def deploy_fundme():
    account = get_account()
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["network"][network.show_active()]["eth_usd_price_feed"]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address
        

    FundMe.deploy(
        price_feed_address, 
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify")
    )

def main():
    deploy_fundme()