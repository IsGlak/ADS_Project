# Compression Algorithms
## Introduction
This lab consist in diferent demos of compression algorithms we are going to exemplifie this ones with some algorithms and toy examples.
## Huffman algorithm
Huffman coding is a greedy algorithm used for lossless data compression. The basic principle of Huffman coding is to compress and encode data, assigning variable-length codes to input characters depending on characters frequency on the text. It builds a binary tree of nodes, where each node represents a character and it's frequency. The tree is constructed by merging the two trees with lowest frequency until just one node is left. In this way the most frequent character gets the smallest code and the least frequent the largest one. The codes assigned are prefixed codes, meaning that they are assigned in such a way that the code assigned to one character is not the prefix of the code assigned to any other character. With this system the code makes sure there is no ambiguity when decoding. 

![](media/huffman.gif)
## Lempel-Ziv-Welch algorithm
LZW algorithm works by reading sequences of symbols, grouping them by strings and converting these strings into codes which take less space. The code uses a compression table 4096 number of table entries choices. Codes 0-255 are always assigned to represent single bytes from input data. 
When the encoding begins the rest of entries of the table are blanck and the compression is achived by useing codes 256-4096 to respresent sequences of bytes. WHen the LZW identifies repeated sequences in the input file it add them to the code table. The decoding process is achieved on the other way, each code from the compressed file is taken and translated through the table to what character or characters it represents. 
