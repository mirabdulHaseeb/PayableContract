//SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract FundMe {

    address public owner;
    address[] public funders;
    mapping(address => uint256) public addressToAmountFunded;
    AggregatorV3Interface public priceFeed;

    constructor(address _priceFeed) public {
        priceFeed = AggregatorV3Interface(_priceFeed);
        owner = msg.sender;
    }

    function fund() public payable {
        uint256 minUSD = 50 * 1e18;
        require(getConversionRate(msg.value) >= minUSD, "Not enough funds");
        addressToAmountFunded[msg.sender] += msg.value;
        funders.push(msg.sender);
    }

    function getVersion() public view returns(uint256) {
        return priceFeed.version();
    }

    function getPrice() public view returns(uint256) {
        (,int256 answer,,,) = priceFeed.latestRoundData();
        // answer returns 10^8
        // wei statndard is 10^18 i.e. 1 eth = 10^18 wei
        return uint256(answer * 1e10);
    }

    function getConversionRate(uint256 ethAmount) public view returns(uint256) {
        uint256 ethPrice = getPrice();
        uint256 ethAmountInUsd = (ethPrice * ethAmount) / 1e18;
        return ethAmountInUsd;
    }

    function getEntranceFee() public view returns(uint256) {
        uint256 minimumUSD = 50 * 1e18;
        uint256 price = getPrice();
        uint256 precision = 1 * 10 * 1e18;
        return (minimumUSD * precision) / price;
    }

    modifier onlyOwner {
        require(msg.sender == owner, "Only the owner can withdraw");
        _;
    }

    function withdraw() payable onlyOwner public {
        payable(msg.sender).transfer(address(this).balance);
        for (uint256 funderIndex=0; funderIndex<funders.length; funderIndex++) {
            address funder = funders[funderIndex];
            addressToAmountFunded[funder] = 0;
        }   
        funders = new address[](0);
    }
}