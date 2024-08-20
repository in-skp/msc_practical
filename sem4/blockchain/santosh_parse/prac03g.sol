// SPDX-License-Identifier: MIT
pragma solidity >=0.8.2 <0.9.0;
// author: santosh_parse 
// practical: 3g-Stucts
// Creating a contract
contract structtest {
    struct Book {
        string name;
        string writter;
        uint id;
        bool available;
    }
    // santosh_parse solidity structs
    Book book1;
    Book book2 = Book("Building Ethereum DApps", "Roberto Infante", 2, false);
    function set_book_detail() public {
        book1 = Book("Introducing Ethereum and Solidity", "Chris Dannen", 1, true);
    }
    function book_info() public view returns (string memory, string memory, uint, bool) {
        return(book2.name, book2.writter, book2.id, book2.available);
    }
    function get_details() public view returns (string memory, uint) {
        return (book1.name, book1.id);
    }
}




