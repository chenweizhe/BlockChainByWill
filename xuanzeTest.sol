pragma solidity ^0.4.16;

contract xuanzeTest {
    
    uint256 i = 0;
    uint256 sumofOdd = 0;
    uint256 sumofEven = 0;
    
    function testWhile() public constant returns(uint256, uint256) {
        while(true){
            i++;
            if(i > 10){
                break;
            }
            if(i % 2 == 0){
                sumofEven += i;
            }else {
                sumofOdd += i;
            }
        }
        return (sumofOdd, sumofEven);
    }
}