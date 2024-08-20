// SPDX-License-Identifier: MIT
pragma solidity >=0.8.2 <0.9.0;
// author: santosh_parse 
// practical: 7b-Assembly
library Sum {
    function sumUsingInlineAssembly(uint[] memory _data) public pure returns (uint o_sum) {
        // santosh_parse solidity assembly
        for (uint i = 0; i < _data.length; ++i) 
        {
            assembly {
                o_sum := add(o_sum, mload(add(add(_data, 0x20), mul(i, 0x20))))
            }
        }
    }
}
contract TestAssembly {
    uint[] data;
    constructor() {
        data.push(1);
        data.push(2);
        data.push(3);
        data.push(4);
        data.push(5);
    }
    function sum() external view returns (uint) {
        // santosh_parse solidity assembly
        return Sum.sumUsingInlineAssembly(data);
    }
}


