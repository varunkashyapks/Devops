class Extraction_unchar:
	def __init__(self):
		self.inputfile = open("history.txt","r")
		self.date = []
		self.time = []
		self.url = []
		self.splithist = []
		self.outputfile = open("Domain_name_only.csv","w")

	def readfile(self):
		for record in self.inputfile:
			self.splithist = record.split(" ")
			self.date.append(self.splithist[0])
			Time_extract = str(self.splithist[1])
			self.splithist = []
			self.splithist = Time_extract.split("|")
			self.time.append(self.splithist[0])
			Website = str(self.splithist[1])
			website_split = Website.split("/")
			self.url.append(website_split[2])
		
	def writefile(self):
		for i in range(len(self.url)):
			domain_name = self.url[i]
			self.outputfile.write(domain_name)
			self.outputfile.write("\n")

Extract_file = Extraction_unchar()
Extract_file.readfile()
Extract_file.writefile()
