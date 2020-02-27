.PONY: all run init clean
all: clean init run
run:
		geth --datadir="ethdata" --nodiscover console --allow-insecure-unlock --rpc --rpcport "8080" --rpcaddr "0.0.0.0" --rpccorsdomain "*" --rpcapi "eth,net,web3,miner,debug,personal,rpc" --nousb
		# geth --datadir="ethdata" --networkid 15 --nodiscover console --allow-insecure-unlock --rpc --rpcport "8080" --rpcaddr "0.0.0.0" --rpccorsdomain "*" --rpcapi "eth,net,web3,miner,debug,personal,rpc" --nousb
init:
		geth --nousb init --datadir ethdata genesis.json
clean:
		rm -rf ethdata/geth
testJRPC:
		curl localhost:8080 -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getBalance","params":["0x8a82b0af305f9ca00519283dac2986788093abe8", "latest"],"id":1}'
		curl localhost:8080 -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_sendTransaction","params":[{"from": "0x8a82b0af305f9ca00519283dac2986788093abe8","to":"0x1552c71754c619f8311e07686fd523250bf68b20","gas": "0x76c0", "gasPrice": "0x9184e72a000", "value":"0xffffffff"}],"id":1}'
