// 版本申明 尖括号表示能兼容0.4.0以上的版本
pragma solidity ^0.4.0;
// import 可以导入合约文件
import "solidity_for_import.sol"

// this is a contract
// 合约声明
contract Test {
    // 状态变量
    uint a;
    // int 和 int256是等价的
    int256 b = 20;
    int256 c = 30;

    function testAdd() public constant returns (int) {
       if (b > c) {
           return b + c;
       } else if (b == c){
           return b * c;
       }else {
           return b << 2;
       }
    }

    function  

    // 布尔类型
    bool boola = true;
    bool boolb = false;




    function testBool1() public returns (bool) {
        return boola && boolb;
    }
    function testBool2() public returns (bool) {
        return boola || boolb;
    }



    // 定义函数
    function setA(uint x) public {
        a = x;
        // 事件的触发
        emit Set_A(x)
    }

    // 事件定义
    event Set_A(uint a);

    // 定义结构类型
    struct Pos {
        int lat;
        int lng;
    }

    address public ownerAddr;

    // 函数修改器的定义 可以修改函数的行为
    modifier owner() {
        require(msg.sender == ownerAddr);
        _;
    }
    // 这里的函数修改器即是 只有这个合约的owner才能调用这个函数
    function mine() public owner {
        a += 1;
        // 系统会将a+=1插入到下划线的位置
    }

}

