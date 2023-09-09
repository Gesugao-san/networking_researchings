import csv
import time

db_in_schema = {
	"Protocols": None,
	"Subdomains": None,
	"SDLs": None,
	"TLDs": None,
	"Ports": None,
	"Pages": None,
}
db_gen_schema = {
	"I": None,
	"Time": None,
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
	i = 0
	db_gen1 = []
	print("row_iterations:", i)
	with open(path2, newline='') as csvfile2:
		reader2 = csv.DictReader(csvfile2, fieldnames=list(db_gen_schema.keys()), delimiter=';')
		for row in reader2:
			i += 1
			if row["Address"] == "Address": continue  # delete head from csv
			db_gen1.append({"I": int(row["I"]), "Time": int(row["Time"]), "Address": row["Address"], "Status": row["Status"], "Reason": row["Reason"]})
		print("row_iterations:", i)
	#if db_gen1[0]["Address"] == "Address": db_gen1.pop(0)
	return db_gen1


def generate_addresses(db_in, db_gen1):
	i = 0
	db_gen2 = []
	cur_time = int(time.time())

	for protocol in db_in["Protocols"]:
		for subdomain in db_in["Subdomains"]:
			for SDL in db_in["SDLs"]:
				for TLD in db_in["TLDs"]:
					for port in db_in["Ports"]:
						for page in db_in["Pages"]:
							i += 1
							gen_address = {'I': i, 'Time': cur_time, 'Address': protocol + "://" + subdomain + SDL + "." + TLD + port + page, 'Status': '', 'Reason': 'autogen'}
							already_generated = False

							#  Generate only missing addresses
							for addr_gen1 in db_gen1:
								if gen_address["Address"] == addr_gen1["Address"]:
									already_generated = True
									db_gen2.append(addr_gen1)

							if not already_generated:
								db_gen2.append(gen_address)
	return db_gen2
	#


"""
def cleanup_db(db_in):
	dirty_db = db_in
	clean_db = db_schema.copy()

	for d_k in dirty_db.keys():
		print("dirty_db_key", dirty_db[d_k])
		for key in dirty_db[d_k]:
			pass
"""

"""
def _write2(path, db):
	with open(path, 'w', newline='') as csvfile3:
		writer3 = csv.DictWriter(csvfile3, fieldnames=list(db_gen_schema.keys()), delimiter=';')
		writer3.writeheader()
		for db_gen2_row in db_gen2:
			writer3.writerow(db_gen2_row)
	#
 """


if __name__ == "__main__":
	print("run")
	print()
	dict_populate(db_in_schema, db_in)

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

	#db_gen2 = generate_addresses(db_in, db_gen1)
	#print()
	#print("db_gen2:", db_gen2)
	#_write('data/2.csv')

	#_write2('data/db_output.csv', db_gen2)

	print()
	print("stop")

