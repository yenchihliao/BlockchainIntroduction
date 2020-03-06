# JMX

* This directory stores different kinds of jmeter test configuration.
* To modify JMX files, search for num_threads, script, and filename.

## countBeanShellSimple.jmx

* Effect: Paradigm of BeanShell using counter config element.
* Dependency: data/mixJRPC.csv
* Report: (only shown in console in the form of)

```bash
0001
eth_getBalance
0002
eth_sendTransaction
0003
eth_getBalance
```

## pythonBeanShellSimple.jmx

* Effect: Paradigm of BeanShell calling external Python script.
* Dependency: ./script/signRawTx.py(it's absolute path hard-coded in jmx file)
* Report: (only shown in console in the form of)
```bash
0xf86d0186d55698372431831e8480940b05169977033095e722d4833099ed18d52cb4e68502540be40080824a91a08865c39eb6e53d5e906ef2885ebfa33e6bb0f3958562d52afd598da1dfffd9aaa071dff8449ad3cace0e77362237f27e6b14b75341c2947dbbe1e2fe0e2a085e93
```

## rawTxCSV.jmx

* Effect: Send signed raw transactns read from file by JSON RPC.
* Dependency: data/rawTx.csv
* Report: ./report/reportTable.csv, ./report/reportTree.xml, ./report/response*

## rawTxPython.jmx

* Effect: Send signed raw transactns python using external python script.
* Dependency: ./script/signRawTx.py(it's absolute path hard-coded in jmx file)
* Report: ./report/reportTable.csv, ./report/reportTree.xml, ./report/response, ./report/debug*

## TxPython.jmx

<!-- to be continued -->
