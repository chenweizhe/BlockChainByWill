pragma solidity ^0.4.16;

contract ArrayTest {
    
    uint256[] public u = [1,2,3];
    
    string s = "abcdefg";
    
    function h() public returns (uint256) {
        u.push(4);
        return u.length;
    }
    
    function f() public view returns (byte) {
        return bytes(s)[1];
    }
    
    // d tai动态 chuang jian创建memoryshu zu数组 
    function newM(uint256 len) constant public returns (uint256) {
        uint256[] memory a = new uint256[] (len);
        bytes memory b = new bytes(len);
        return a.length;
    }
    
    
    function g(uint256[3] _data) public constant {
        
    }
    
    
}
