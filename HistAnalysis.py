class HistAnalysis:
	def __init__(self):
		self.input_file = open("m1.csv","r")
		self.output_file = open("web_countnew.csv","w")
		self.word_count = {}

	def read_file(self):
		for record in self.input_file:
			string_split = record.split(",")
			word = str(string_split[2])
			self.Word_count(string_split[2])
			#print(string_split[2],string_split[3])
		for key in self.word_count:
			message = key + "," + str(self.word_count[key])
			self.output_file.write(message)
			self.output_file.write("\n")

	def Word_count(self,key):
		if not key  in self.word_count:
			self.word_count[key] = 1
		else:
			self.word_count[key] = 1 + int(self.word_count[key])



H = HistAnalysis()
H.read_file()
