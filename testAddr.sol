pragma solidity ^0.4.16;

contract AddrTest {
    
    // yi ge一个 han shu函数 neng能 jie shou接受 yi tai以太 bi币 xu yao需要 payable关键字 
    function deposit() public payable {
        
    }
    
    function getBalance() public constant returns (uint256) {
        return this.balance;
    }
    // zhuan yi转移 yi tai以太 
    function transferEther(address towho) public {
        towho.transfer(10);
    }
}