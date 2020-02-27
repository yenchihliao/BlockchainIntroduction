# Second Term Project

Transactions and Smart Contract

## Introduction

Instead of reading papers, we are now going to interact with blockchain to understand it better. In this project, we are going to have fun with Ethereum smart contract.

Project Goal: Know better how smart contract and transactions in Ethereum work.

## Problems

* PJ2 smart contract address: 0xC820cBdc60c879cB73Cdd895e7e89E796f6C6C16
* Environment: Ropsten Ethereum Tesetnet
* PJ2 related [files](https://github.com/yenchihliao/BlockchainIntroduction)
* There are 3 problems and 1 bonus in this homework

### Problem1

Send a transaction to the function, Problem1, in PJ2.sol with any tools you prefer.

* The input will be your **studentID**: e.g. "b00902000"
* You need to pay at least 3 gwei in this transaction.

### Problem2

Write a program to send transaction to the function, Problem2, in PJ2.sol.

* The input includes your **stedentID** and the **hexdigest of sha256 hash** of the program.
* You need to pay at least 3 gwei in this transaction.
* Hint: You can't hard code the hash value into your program yet still be able to send the correct hash value in the transaction.

### Problem3

Write a program that deploys a contract than send a transaction to the function, Problem3, in PJ2.sol.

* The contract only requires one public function named studentID that takes no input and outputs your studentID. e.g. b00906000.
* The input includes your **studentID**, the **hexdigest of sha256 hash** of the program, and **address** of the contract you deployed.

### Bonus

* Please trace the PJ2.sol to find it.
* Do not use brute-force search to get to the answer. Make guesses within reasonable ranges.


## Submission

* deadline Nov.29 2019, 23:59:59.
* Upload [studentID].zip to Ceiba including:
	* The program that solves problem2, <span style="color=orange">problem2.[py/js/...]</span>, that matches the hash value in the transaction to problem2.
	* The program that solves problem3, <span style="color=orange">problem3.[py/js/...]</span>, that matches the hash value in the transaction to problem3.
	* The smart contract you deployed in problem3, <span style="color=orange">problem3.[sol/vy/...]</span>.
	* Write a report.txt that describe how you solve bonus and any other feedbacks.

## Spec.

1. First alphabet in input of studentID should <span style="color=red">not</span> be capitalized.
2. To obtain the hash value of your programs, please use the checkFile.py provided by `$python checkFile.py [filename]`
3. Strictly follows the naming convention specified in [Submission](#Submission) section.

## Some recommandations

1. Although you can use the solution of problem2 to solve problem1, you may want to try out some sophisticated tools to send transactions such as [MetaMask](https://metamask.io/) with [Remix](https://remix.ethereum.org/).
2. It's convenient to get Ropsten testnet coin by using the [faucet](https://faucet.metamask.io/) if you are using MetaMask. (remember to switch to ropsten testnet instead of the mainnet)
3. When you are implementing the smart contract, you can test he correctness of your code on Remix with MetaMask with ease.
4. If you don't know how to write a smart contract, [here](https://cryptozombies.io/) is a solidity tutorial.
5. To write programs that interact with chains, the package, web3, is usually the choice.
6. To send transaction via web3 api, you need to have a web3 provider. You can either construct your own node using tools like [go-ethereum](https://geth.ethereum.org/) or use other fullnodes such as [infura](https://infura.io/).
7. To get the abi/byteCode from the compiled smart contracts, you can either download the command, solc, to compile locally or copy the result from Remix.
