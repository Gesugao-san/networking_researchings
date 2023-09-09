import csv

def _read():
	with open('1.csv', 'r', newline='') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
		for row in spamreader:
			print(', '.join(row))


if __name__ == "__main__":
	_read()

