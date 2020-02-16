pragma solidity ^0.4.16;

contract Test {
    
    function simpleInput(uint256 a, uint256 b) public constant returns (uint256 sum, uint mul) {
        sum = a + b;
        mul = a * b;
        
    }
    
    function testSimpleInput() public constant returns (uint sum, uint mul) {
        (sum, mul) = simpleInput({a:1, b:3});
    }
    
    function f() public constant returns (uint, bool, uint) {
        return (7, true, 2);
    }
    
    function g() public {
        var (x,y,z) = f();
    }
    
}