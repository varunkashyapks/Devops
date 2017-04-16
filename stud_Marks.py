class Stud_Marks:
	def __init__(self):
		self.in_file = open("data.csv","r")
		self.out_file = open("total.csv","w")
		self.subject1 = []
		self.subject2 = []
		self.subject3 = []
		self.subject4 = []
		self.subject5 = []
		

	def cal_total(self):
		count = 1
		for record in self.in_file:
			total = 0
			marks_split = record.split(",")
			subj1 = marks_split[1]
			self.subject1.append(subj1) 
			subj2 = marks_split[2]	
			self.subject2.append(subj2)
			subj3 = marks_split[3]
			self.subject3.append(subj3)
			subj4 = marks_split[4]
			self.subject4.append(subj4)
			subj5 = marks_split[5]
			#print(subj5)
			self.subject5.append(subj5)
			total = int(subj1)+int(subj2)+int(subj3)+int(subj4)+int(subj5)
			avg = (float(total))/5.0 
			#print(avg)
			message = str(count)+","+str(total)+","+str(avg)+",0"+"\n"
			self.out_file.write(message)
			count += 1

	
students = Stud_Marks()
students.cal_total()

