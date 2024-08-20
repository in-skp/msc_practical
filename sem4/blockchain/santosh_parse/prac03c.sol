// SPDX-License-Identifier: MIT
pragma solidity >=0.8.2 <0.9.0;
// author: santosh_parse 
// practical: 3c-Loops
contract loop {
    uint[4] public arr;
    uint public count;
    function looptest() public {
        // santosh_parse solidity loops
        while(count < arr.length) {
            arr[count] = count;
            count++;
        }
    }
}




