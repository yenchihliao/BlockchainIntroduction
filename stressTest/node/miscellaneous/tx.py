<<<<<<< Updated upstream
# create send_transaction JSON RPC request from file of private keys

=======
# create send_transaction JSON RPC request
>>>>>>> Stashed changes
from web3.auto import w3
import sys

f_addr = open('addrs.txt', 'r')
addrs = f_addr.readlines()
f_addr.close()
if len(sys.argv) == 1:
    nonce = 0
else:
    nonce = sys.argv[1]
# f = open('sendTranscation.csv', 'w')
f.write("method\tparams\n")
for nonce in range(100):
    for i in range(300):
        #  transaction = "{'from':addrs[i][:-1],'to':w3.toChecksumAddress(addrs[-1][:-1]),'value':10000000000,#1gwei'gas':2000000,'gasPrice':234567897654321,'nonce':nonce,'chainId':9527}"
        transaction = '{"from":' + w3.toChecksumAddress(addrs[i][:-1]) \
            + ',"to":' + w3.toChecksumAddress(addrs[-1][:-1]) \
            + ',"value":10000000000,"gas":2000000,"gasPrice":234567897654321,"nonce":' \
            + str(nonce) + ',"chainId":9527}'
        # f.write("eth_sendTransaction\t" + transaction + "\n")
        print(transaction)


# When you run sendRawTransaction, you get back the hash of the transaction:
#  w3.eth.sendRawTransaction(signed.rawTransaction)
