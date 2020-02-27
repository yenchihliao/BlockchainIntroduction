#lcreate raw transaction from sratch
from web3.auto import w3
import sys

f_priv = open('priv.txt', 'r')
keys = f_priv.readlines()
f_priv.close()
arg = int(sys.argv[1])
nonce = arg // 300
account = arg % 300
transaction = {
    'to': "0x0B05169977033095E722d4833099Ed18d52CB4e6",
    'value': 10000000000, # 1 gwei
    'gas': 2000000,
    'gasPrice': 234567897654321,
    'nonce': nonce,
    'chainId': 9527
}
signed = w3.eth.account.sign_transaction(transaction, keys[account][:-1])
#  print(signed)
print(signed['rawTransaction'].hex())

# When you run sendRawTransaction, you get back the hash of the transaction:
#  w3.eth.sendRawTransaction(signed.rawTransaction)
