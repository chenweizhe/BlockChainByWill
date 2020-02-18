pragma solidity ^0.4.16;

contract MyToken {
    
    // save the rest money of the address
    mapping(address => uint256) public balanceOf;
    
    
    constructor(uint256 initSupply) public {
        balanceOf[msg.sender] = initSupply;
    }
    
    // jiezhi zhuanyi 
    function transfer(address _to, uint256 _value) public {
        
        require(balanceOf[msg.sender] >= _value);
        require(balanceOf[_to] + _value >= balanceOf[_to]);
        
        balanceOf[msg.sender] -= _value;
        balanceOf[_to] += _value;
        
    }
    
}