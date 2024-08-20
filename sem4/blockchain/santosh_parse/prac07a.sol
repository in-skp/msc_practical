// SPDX-License-Identifier: MIT
pragma solidity >=0.8.2 <0.9.0;
// author: santosh_parse 
// practical: 7a-Libraries
library Search {
    function indexOf(uint[] storage self, uint value) public view returns (uint) {
        for (uint i = 0; i < self.length; i++) if (self[i] == value) return i;
        return uint(1);
    }
}
contract TestLibrary {
    uint[] data;
    constructor() {
        data.push(1);
        data.push(2);
        data.push(3);
        data.push(4);
        data.push(5);
    }
    function isValuePresent() external view returns (uint) {
        // satosh_parse solidity libraries
        uint value = 4;
        uint index = Search.indexOf(data, value);
        return index;
    }
}


