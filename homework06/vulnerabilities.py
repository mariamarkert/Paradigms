#!/usr/bin/env python3


# Any import statement you need
import sys
import csv

# Your class definitions go here
class CVE(object):

	def __init__(self, name, cve_id, date_of_report, cve_type, root_cause, total_impacted_files, code_churn, bugtrack_url):
		super().__init__()
		self.name = name
		self.cve_id = cve_id
		self.date_of_report = date_of_report
		self.cve_type = cve_type
		self.root_cause = root_cause
		self.total_impacted_files = total_impacted_files
		self.code_churn = code_churn
		self.bugtrack_url = bugtrack_url
		
class PHP(CVE):
	def get_name(self):
		return "PHP"
class Thunderbird(CVE):
	def get_name(self):
		return "Thunderbird"
	#name = "Thunderbird"
class Chromium(CVE):
	def get_name(self):
		return "Chromium"
	#name = "Chromium"


# Implement the parsing of CSV
def loadObjects(csv_file1, csv_file2, csv_file3):

	vulnerabilities = []

	for fp in [csv_file1, csv_file2, csv_file3]:
		with open(fp) as csvfile:
			reader = csv.reader(csvfile, delimiter=',', quotechar='"')
			for row in reader:
				if fp == "chromium-dataset.csv":
					temp = Chromium(fp[:-4], row[0], row[1], row[2], row[3], row[5], row[6], row[7])
				elif fp == "php-dataset.csv":
					temp = PHP(fp[:-4], row[0], row[1], row[2], row[3], row[5], row[6], row[7])
				else:
					temp = Thunderbird(fp[:-4], row[0], row[1], row[2], row[3], row[5], row[6], row[7])

				vulnerabilities.append(temp)
				
		
	  # Your implementation here
	return vulnerabilities



# Implement the queries
def query1(vulnerabilities):
	count = 0
	for i in vulnerabilities:
		if i.cve_type == "TACTICAL":
			count+=1

	return count

def query2(vulnerabilities):
	count = 0
	for i in vulnerabilities:
		if i.name == "php-dataset" and i.cve_type == "NON-TACTICAL":
			count+=1
	
	return count

def query3(vulnerabilities):
	summ = 0
	count = 0
	for v in vulnerabilities:
		if v.cve_type =="TACTICAL":
			summ = summ + int(v.code_churn)
			count += 1
	return summ/count

def query4(vulnerabilities):
	tact_sum = 0
	tact_count = 0
	non_sum = 0
	non_count = 0

	for v in vulnerabilities:
		if v.cve_type =="TACTICAL":
			tact_sum = tact_sum + int(v.total_impacted_files)
			tact_count += 1
		elif v.cve_type =="NON-TACTICAL":
			non_sum = non_sum + int(v.total_impacted_files)
			non_count += 1

	
	if (tact_sum / tact_count) == (non_sum/non_count):
		return "BOTH"
	elif (tact_sum / tact_count) > (non_sum/non_count):
		return "TACTICAL"
	else:
		return "NON-TACTICAL"
	return "String"

def query5(vulnerabilities):
	
	counts = {}
	for v in vulnerabilities:
		counts[type(v).__name__] = counts.get(type(v).__name__, 0) + 1

	return max(counts, key = counts.get)
	#return "String"



def main():
	# parse program arguments
	csv_file1, csv_file2, csv_file3 = sys.argv[1],sys.argv[2],sys.argv[3]
	
	# load objects
	vulnerabilities = loadObjects(csv_file1, csv_file2, csv_file3)

	# Print 
	print("Query1=",query1(vulnerabilities))
	print("Query2=",query2(vulnerabilities))
	print("Query3=",query3(vulnerabilities))
	print("Query4=",query4(vulnerabilities))
	print("Query5=",query5(vulnerabilities))


if __name__ == '__main__':
	main()
