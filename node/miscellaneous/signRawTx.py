# create raw transaction from sratch
from web3.auto import w3
import sys

f_addr = open('addrs.txt', 'r')
f_priv = open('priv.txt', 'r')
addrs = f_addr.readlines()
keys = f_priv.readlines()
f_addr.close()
f_priv.close()
f = open('rawTxs.txt', 'w')
for i in range(300):
    transaction = {
        'to': w3.toChecksumAddress(addrs[-1][:-1]),
        'value': 10000000000, # 1 gwei
        'gas': 2000000,
        'gasPrice': 234567897654321,
        'nonce': int(sys.argv[1]),
        'chainId': 9527
    }
    signed = w3.eth.account.sign_transaction(transaction, keys[i][:-1])
    print(signed)
    rawTx = signed['rawTransaction'].hex()
    assert(w3.eth.account.recover_transaction(rawTx) == w3.toChecksumAddress(addrs[i][:-1]))
    f.write('eth_sendRawTransaction\t'+rawTx+'\n')
f.close()

# When you run sendRawTransaction, you get back the hash of the transaction:
#  w3.eth.sendRawTransaction(signed.rawTransaction)
