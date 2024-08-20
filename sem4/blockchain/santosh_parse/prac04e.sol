// SPDX-License-Identifier: MIT
pragma solidity >=0.8.2 <0.9.0;
// author: santosh_parse 
// practical: 4e-Cryptographic Functions
contract HashFunction {
    function hash(string memory _text, uint _num, address _addr) public pure returns (bytes32) {
        return keccak256(abi.encodePacked(_text, _num, _addr));
    }
    function collision(string memory _text, string memory _anotherText) public pure returns (bytes32) {
        return keccak256(abi.encodePacked(_text, _anotherText));
    }
}

contract GuesssTheMaigicWord {
    bytes32 public answer = 0x60298f78cc0b47170ba79c10aa3851d7648bd96f2f8e46a19dbc777c36fb0c00;
    // Magic word is "Solidity"
    // santosh_parse solidity cryptographic functions
    function guess(string memory _word) public view returns (bool) {
        return keccak256(abi.encodePacked(_word)) == answer;
    }
}


