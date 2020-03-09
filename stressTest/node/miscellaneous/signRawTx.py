# create raw transaction from file of private keys

from web3.auto import w3
import sys

f_addr = open('addrs.txt', 'r')
f_priv = open('priv.txt', 'r')
addrs = f_addr.readlines()
keys = f_priv.readlines()
f_addr.close()
f_priv.close()
f_rawTx = open('rawTxs.txt', 'w')
f_txHash = open('txHashs.txt', 'w')
if len(sys.argv) == 1:
    nonce = 0
else:
    nonce = sys.argv[1]
for i in range(3):
    transaction = {
        'to': w3.toChecksumAddress(addrs[-1][:-1]),
        'value': 10000000000, # 1 gwei
        'gas': 2000000,
        'gasPrice': 234567897654321,
        'nonce': nonce,
        'chainId': 9527
    }
    signed = w3.eth.account.sign_transaction(transaction, keys[i][:-1])
    rawTx = signed['rawTransaction'].hex()
    print(rawTx)
    assert(w3.eth.account.recover_transaction(rawTx) == w3.toChecksumAddress(addrs[i][:-1]))
    f_rawTx.write('eth_sendRawTransaction\t'+rawTx+'\n')
    f_txHash.write(signed['hash'].hex() + '\n')
f_rawTx.close()
f_txHash.close()

# When you run sendRawTransaction, you get back the hash of the transaction:
#  w3.eth.sendRawTransaction(signed.rawTransaction)
