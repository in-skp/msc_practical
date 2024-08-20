// SPDX-License-Identifier: MIT
pragma solidity >=0.8.2 <0.9.0;
// author: santosh_parse 
// practical: 3e-Strings & Enum
// Creating a contract
contract stringtest {
    string public str = "Santosh Parse";
    enum my_enum { geeks_, _for, _geeks }
    function Enum() public pure returns(my_enum) {
        // santosh_parse solidity string & enum
        return my_enum._geeks;
    }

}



