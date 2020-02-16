pragma solidity ^0.4.16;

contract Test {
    uint internal data;
    
    constructor (uint a) public {
        data = a;
    }
    
    event EVENTA(uint a);
    
    
    function testView() public view returns (uint ) {
        // emit EVENTA(1);
        return data;
    }
    
    
    function f() public pure returns (uint ) {
        return 1 * 2 + 3;
    }
    
    function () public payable {
        
    }
    
}