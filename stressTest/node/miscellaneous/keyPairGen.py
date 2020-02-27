# Generate ethereum account and its private key from scratch
import sha3
from ecdsa import SigningKey, SECP256k1
f_addr = open('addrs.txt', 'a')
f_priv = open('priv.txt', 'a')
for i in range(1):
    keccak = sha3.keccak_256()
    private = SigningKey.generate(curve=SECP256k1)
    public = private.get_verifying_key().to_string()
    keccak.update(public)
    address = "0x{}".format(keccak.hexdigest()[24:])
    print(public.hex())
    print(address)
    print(private.to_string().hex())
    f_addr.write(address+'\n')
    f_priv.write(private.to_string().hex() + '\n')
f_addr.close()
f_priv.close()
