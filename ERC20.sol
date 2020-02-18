pragma solidity ^0.4.20;
// 代币开发必须遵守ERC20标准 但是当前写的不是最新的版本
contract ERC20Interface {
    string public name;
    string public symbol;
    uint8 public decimals;
    uint public totalSupply;

    // function name() public view returns (string);
    // function symbol() public view returns (string);
    // function decimals() public view returns (uint8);
    // function totalSupply() public view returns (uint256);
    function balanceOf(address _owner) public view returns (uint256 balance);
    function transfer(address _to, uint256 _value) public returns (bool success);
    function transferFrom(address _from, address _to, uint256 _value) public returns (bool success);
    function approve(address _spender, uint256 _value) public returns (bool success);
    function allowance(address _owner, address _spender) public view returns (uint256 remaining);
    event Transfer(address indexed _from, address indexed _to, uint256 _value);
    event Approval(address indexed _owner, address indexed _spender, uint256 _value);

}

contract ERC20 is ERC20Interface {

    // 状态变量 存储余额
    mapping (address => uint256) balanceOf;

    // 表示这个账号可以操控账号金额 的权限
    mapping (address => mapping(address => uint256)) internal allowed;

    constructor() public {
        name = "will TOKEN";
        symbol = "CHEN"; 
        decimals = 0;
        totalSupply = 100000000;
    }


    function balanceOf(address _owner) public view returns (uint256 balance){
        return balanceOf[_owner];
    }

    function transfer(address _to, uint256 _value) public returns (bool success){
        require(_to != address(0));
        require(balanceOf[msg.sender] >= _value);
        require(balanceOf[_to] + _value >= balanceOf[_to]);

        balanceOf[msg.sender] -= _value;
        balanceOf[_to] += _value;
        emit Transfer(msg.sender, _to, _value);
    }
    function transferFrom(address _from, address _to, uint256 _value) public returns (bool success){
        
        require(_to != address(0));
        require(balanceOf[_from] >= _value);
        require(allowed[_from][msg.sender] >= _value);
        require(balanceOf[_to] + _value >= balanceOf[_to]);



        balanceOf[_from] -= _value;
        balanceOf[_to] += _value;
        emit Transfer(_from, _to, _value);
        success = true;
    }

    function approve(address _spender, uint256 _value) public returns (bool success){
        
        allowed[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);
        success = true;
    }

    function allowance(address _owner, address _spender) public view returns (uint256 remaining){
        return allowed[_owner][_spender];
    }

}