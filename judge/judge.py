from web3 import Web3
import sys
import json
import os

# handle input
assert len(sys.argv) == 3
ID = sys.argv[1] # Student ID(ex: r07944023)
lang = sys.argv[2] # Use of language(ex:py|js|java)

# Connect to the contract 
w3 = Web3(Web3.HTTPProvider("https://ropsten.infura.io/v3/5b3e6a6f546f478eaf60bb110825f4dc")) 
f = open('PJ2_abi.json')
abi = json.load(f)
PJ2 = w3.eth.contract(address='0xC820cBdc60c879cB73Cdd895e7e89E796f6C6C16', abi=abi)

# Score on contract
print("grading:", ID)
total = 0
total += PJ2.functions.score(ID).call()
print("Score on contract(30+20):", total)

# Score for problem2 correctness 
import hashlib
hasher = hashlib.sha256()
score = 0
try:
    path = ID + '/problem2.' + lang
    f = open(path, 'rb')
    hasher.update(f.read())
    Hex = PJ2.functions.ID2P2Hex(ID).call()
    if(Hex != 0):
        if(hasher.hexdigest() != PJ2.functions.ID2P2Hex(ID).call()):
            score = 5
            print("problem2 hash value doesn't match")
        else:
            score = 20
    else:
        print("No hex value found")
except:
    print("No problem2." + lang + " found")
print("Score for problem2 correctness(20):", score)
total += score

# Score for problem3 function correctness
hasher = hashlib.sha256()
score = 0
try:
    path = ID + '/problem3.' + lang
    f = open(path, 'rb')
    hasher.update(f.read())
    Hex = PJ2.functions.ID2P3Hex(ID).call()
    if(Hex != 0):
        if(hasher.hexdigest() != PJ2.functions.ID2P3Hex(ID).call()):
            score = 5
            print("problem3 hash value doesn't match")
        else:
            score = 20
    else:
        print("No hex value found")
except:
    print("No problem3." + lang + " found")
print("Score for problem3 function correctness(20):", score)
total += score

# Score for problem3 contract correctness
score = 0
abiFile = 'problem3_abi'
command = 'solc ' + '--abi ' + ID + '/problem3.sol > ' + abiFile
try:
    assert(os.system(command) == 0)
    f = open(abiFile, 'r')
    for _ in range(4):
        abi = f.readline()[:-1]
    try:
        IDcontract = w3.eth.contract(PJ2.functions.ID2address(ID).call(), abi=abi)
        try:
            assert(IDcontract.functions.studentID().call() == ID)
            score = 30
        except:
            print("Problem3.sol function incorrect")
            score = 20
    except:
        print("Can't find problem3.sol in given address")
        score = 5
except:
    print("Fail to construct abi of problem3.sol")
print("Score for problem3 contract correctness(30):", score)
total += score

# Total score 
f = open("score.txt", 'a')
f.write(ID + " " + str(total) + "\n")
f.close()
print("Total score(100+20):", total)
