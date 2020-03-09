# create send_transaction JSON RPC request
from web3.auto import w3
import sys

f_addr = open('addrs.txt', 'r')
addrs = f_addr.readlines()
f_addr.close()
if len(sys.argv) == 1:
    arg = 0
else:
    arg = int(sys.argv[1])
nonce = arg // 300
acc = arg % 300
# f = open('sendTranscation.csv', 'w')
# f.write("method\tparams\n")
#  transaction = "{'from':addrs[i][:-1],'to':w3.toChecksumAddress(addrs[-1][:-1]),'value':10000000000,#1gwei'gas':2000000,'gasPrice':234567897654321,'nonce':nonce,'chainId':9527}"
transaction = '{"from":"' + w3.toChecksumAddress(addrs[acc][:-1]) \
    + '","to":"' + w3.toChecksumAddress(addrs[-1][:-1]) \
    + '","value":"0x2540be400","gas":"0x1e8480","gasPrice":"0xd55698372431","chainId":9527}'
# f.write("eth_sendTransaction\t" + transaction + "\n")
print(transaction)


# When you run sendRawTransaction, you get back the hash of the transaction:
#  w3.eth.sendRawTransaction(signed.rawTransaction)
