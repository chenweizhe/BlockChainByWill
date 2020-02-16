pragma solidity ^0.4.16;

contract errorTest {
     
    // jiang qian yiqie wei er  yaoqiu qi neng beizhengchu
     function sendHalf(address addr) public payable returns (uint256 balance) {
        
         require(msg.value % 2 == 0);
         return this.balance;
     }
     
     
}
