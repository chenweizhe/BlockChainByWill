pragma solidity ^0.4.16;

contract apiTest {
    
    
    constructor() payable {
        
    }
    
    function testApi() public constant returns (uint256) {
        // return msg.sender;
        // return msg.value;
        // kuang g矿工 di zhi地址 
        // block.coinbase;
        // return block.difficulty;
        return block.number;
        // block.timestamp;
        // now(uint256);
        // tx.gasprice;
    }
}