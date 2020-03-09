# use geth command to import account private key into go-ethereum node

for((i=1 ; i <= 300; i++)){
	sed -n "${i}p" ./priv.txt > tmp
	geth --nousb account import --datadir ../ethdata --password ../pwd tmp
}
rm tmp
