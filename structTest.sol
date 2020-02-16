pragma solidity ^0.4.16;

contract structTest {
    struct Funder {
        address addr;
        uint256 amount;
    }
    
    // 使用结构体可以定义一个状态变量 
    Funder funder;
    
    function newFunder() public {
        funder = Funder({addr: msg.sender, amount: 10});
    }
    
    mapping(address => uint256) public balances;
    
    function updateBalance(uint256 newbalance) public {
        balances[msg.sender] = newbalance;
    }
}