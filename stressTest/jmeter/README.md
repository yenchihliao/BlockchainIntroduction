# Jmeter

* Execute jmeter command in this directory by `jmeter -nt jmx/[yourTestCase].jmx`
* Delete all the report files by `make clean`
* `./data`: puts the file jmeter potentially reads.
* `./jmx`: puts all the jmeter configuration files.
* `./script`: puts all the external script jmeter potentially invokes.
* `./*.txt`: private and public keys read by programs in `./script`.
