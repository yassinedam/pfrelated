#! /pyscript /puthon3
with open("/pyscript/data.txt") as stream:
	for line in stream.readlines():
		line.strip()
