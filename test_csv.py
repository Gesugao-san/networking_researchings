import csv

db_in_schema = {
	"Protocols": None,
	"Subdomains": None,
	"SDLs": None,
	"TLDs": None,
	"Ports": None,
	"Pages": None,
}
db_gen_schema = {
	"Address": None,
	"Status": None,
	"Reason": None,
}
db_in = {}
db_gen1 = {}


def dict_populate(schema, dict):
	for key in schema.keys():
		dict[key] = []


def read_db_in(path1):
	[i, ik, success, skip] = [0, 0, 0, 0]
	print("row_iterations:", i, "db_iterations:", ik, "success:", success, "skip:", skip)
	with open(path1, newline='') as csvfile1:
		reader1 = csv.DictReader(csvfile1, delimiter=';')
		for row in reader1:
			i += 1
			if i == 1:  # forcing adding spaces in, if in first places
				for key in db_in.keys():
					db_in[key].append(row[key])
				continue

			for key in db_in.keys():
				ik += 1
				if not row[key]:
					skip += 1
					print("Skipped key:", i, key)
				else:
					success += 1
					db_in[key].append(row[key])
		print("row_iterations:", i, "db_iterations:", ik, "success:", success, "skip:", skip)
	return db_in


def read_db_gen(path2):
	[i, ik] = [0, 0]
	print("row_iterations:", i, "db_iterations:", ik)
	with open(path2, newline='') as csvfile2:
		reader2 = csv.DictReader(csvfile2, delimiter=';')
		for row in reader2:
			i += 1
			for key in db_gen1.keys():
				ik += 1
				db_gen1[key].append(row[key])
		print("row_iterations:", i, "db_iterations:", ik)
	return db_gen1


def generate_addresses(db_in):
	db_gen2 = []
	for protocol in db_in["Protocols"]:
		for subdomain in db_in["Subdomains"]:
			for SDL in db_in["SDLs"]:
				for TLD in db_in["TLDs"]:
					for port in db_in["Ports"]:
						for page in db_in["Pages"]:
							db_gen2.append(protocol+"://"+subdomain+SDL+"."+TLD+port+page)
					return db_gen2
	#for key in db_in.keys():
	#	for kkey in key:
	#		pass


"""
def cleanup_db(db_in):
	dirty_db = db_in
	clean_db = db_schema.copy()

	for d_k in dirty_db.keys():
		print("dirty_db_key", dirty_db[d_k])
		for key in dirty_db[d_k]:
			pass
"""


def _write2(path, db):
	with open(path, 'w', newline='') as csvfile3:
		fieldnames1 = list(db_gen_schema.keys()) #['Num', 'Address', 'Status', 'Reason']
		writer3 = csv.DictWriter(csvfile3, fieldnames=fieldnames1, delimiter=';')

		writer3.writeheader()
		for address in db_gen2:
			writer3.writerow({'Address': address, 'Status': None, 'Reason': 'autogen'})
		#writer.writerow({'Address': 'Baked', 'Status': '', 'Reason': ''})
		#writer.writerow({'Address': 'Lovely', 'Status': '', 'Reason': ''})



if __name__ == "__main__":
	print("run")
	print()
	dict_populate(db_in_schema, db_in)
	dict_populate(db_gen_schema, db_gen1)

	db_in = read_db_in('data/db_input.csv')
	print()
	print("db_in:", db_in)
	print()
	print("Protocols:", db_in["Protocols"])
	print("Protocols 0:", db_in["Protocols"][0])
	print()

	db_gen1 = read_db_gen('data/db_output.csv')
	print()
	print("db_gen1:", db_gen1)
	print()

	db_gen2 = generate_addresses(db_in)
	print()
	print("db_gen2:", db_gen2)
	#_write('data/2.csv')

	_write2('data/db_output.csv', db_gen2)

	print()
	print("stop")

