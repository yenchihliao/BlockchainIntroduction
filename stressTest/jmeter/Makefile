.PONY: all clean run
all: clean run

clean:
		rm -rf report*
		rm jmeter.log
run:
		~/apache-jmeter-5.2.1/bin/jmeter.sh -n -t testRawTx.jmx
