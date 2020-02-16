pragma solidity ^0.4.16;

contract Test {
    
    uint public data;
    
    function f(uint a) private returns (uint ) {
        return a + 1;
    }
    
    function setData(uint a) internal {
        data = a;
    }
    
    function exSetData(uint a) external {
        data = a;
    }
    
    function testSetData() public {
        setData(1);
        this.exSetData(1);
    }
    
}


contract Test2 is Test {
    function setData(uint a) internal {
        data = a;
    }
}

contract D {
    
    function readData() public {
        Test test = new Test();
        test.exSetData(1);
    }
    
}