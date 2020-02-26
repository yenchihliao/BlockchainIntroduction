# extract geth encrypted private key from its keystore file
from web3.auto import w3
with open('/home/caideyi/node/ethdata/keystore/UTC--2020-02-10T07-21-00.293285700Z--8a82b0af305f9ca00519283dac2986788093abe8') as keyfile:
    encrypted_key = keyfile.read()
    # tip: do not save the key or password anywhere, especially into a shared source file
    private_key = w3.eth.account.decrypt(encrypted_key, 'your_private_key')
    print(private_key.hex())
