import csv

def _read_all(path):
	with open(path, 'r', newline='') as csvfile:
		csvreader = csv.reader(csvfile, delimiter=';', quotechar='|')
		for row in csvreader:
			print('; '.join(row))

def _read2(path):
	with open(path, newline='') as csvfile:
		reader = csv.DictReader(csvfile, delimiter=';')
		for row in reader: #Protocol;Subdomain;SDL;TLD;Port;Page
			print(row)
			#print(row['Protocol'], row['Subdomain'], row['SDL'], row['TLD'], row['Port'], row['Page'])

def _write(path):
	with open(path, 'w', newline='') as csvfile:
		csvreader = csv.writer(
			csvfile,
			delimiter=';',
			quotechar='|',
			quoting=csv.QUOTE_MINIMAL
		)
		csvreader.writerow(['Spam'] * 5 + ['Baked Beans'])
		csvreader.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

def _write2(path):
	with open(path, 'w', newline='') as csvfile:
		fieldnames = ['first_name', 'last_name']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')

		writer.writeheader()
		writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
		writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
		writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})

if __name__ == "__main__":
	#_read_all('data/1.csv')
	_read2('data/1.csv')
	_write('data/2.csv')
	_write2('data/3.csv')

