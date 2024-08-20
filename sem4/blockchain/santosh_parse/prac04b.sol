// SPDX-License-Identifier: MIT
pragma solidity >=0.8.2 <0.9.0;
// author: santosh_parse 
// practical: 4b-Pure and View Functions
contract pure_function {
    function mul(uint a, uint b) public pure returns (uint) {
        // santosh_parse solidity pure function
        return  a * (b + 42);
    }
}

contract view_function {
    uint age = 10;
    function getter() public view returns (uint) {
        // santosh_parse solidity view function
        return age;
    }
}





