// 版本申明 尖括号表示能兼容0.4.0以上的版本
pragma solidity ^0.4.0;
// this is a contract
// 合约声明
contract Test {
    // 状态变量
    uint a;
    // int 和 int256是等价的
    int256 b = 20;
    int256 c = 40;

    function testAdd() public constant returns (int) {
       if (b < c) {
           return b + c;
       } else if (b == c){
           return b * c;
       }else {
           return b << 2;
       }
    }
    
    function testLiterals() public constant returns (int) {
        return 123 + 1.5e10;
    }
    
    function testStringLiterals() public constant returns (string) {
        return "abc";
    }
    
    function testHexLiterals() public constant returns (bytes2) {
        return hex"abcd";
    }
    
    // 地址常量 
    

}

