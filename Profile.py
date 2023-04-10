class Profile:
    def __init__(self,name,address,study,number,date_of_birth):
        self.name=name
        self.address=address
        self.study=study
        self.number=number
        self.date_of_birth=date_of_birth
    def Public(self):
        print("Name: "+self.name,"Address: "+self.address,"Study: "+self.study)
    def Friend(self):
        print("Birthday: "+self.date_of_birth)
    def Only_me(self):
        print("Contact Number: "+self.number)
     

sadiya={"Sadiya Akter","Khulna","Khulna Mohila Polytechnic Institute","017********","19-02-2000"}
aysha={"Aysha Siddika Rimpa","Bagerhat","Khulna Mohila Polytechnic Institute","013********","23-10-2003"}
shanto={"Mostakim Mojammel Shanto","Khulna","hjdsfgsdvbshdfg","016********","16-01-1997"}
sonia={"Sonia Akter","Khulna","Azam Khan Govt. Commerce College","019********","12-06-1997"}
hira={"Hira Akter","Barishal","Khulna Mohila Polytechnic Institute","017********","18-07-2002"}
nadiya={"Nadiya Khatun","Mongla","Khulna Govt. Girls College","019********","27-05-2001"}
tamanna={"Tamanna Akter Joti","Khulna","Khulna Mohila Polytechnic Institute","017********","19-10-2003"}

sadiya.Public()
sadiya.Friend()
sadiya.Only_me()

print("****************************************************")

aysha.Public()
aysha.Friend()
aysha.Only_me()

print("****************************************************")

shanto.Public()
shanto.Friend()
shanto.Only_me()

print("****************************************************")

sonia.Public()
sonia.Friend()
sonia.Only_me()

print("****************************************************")

hira.Public()
hira.Friend()
hira.Only_me()

print("****************************************************")

nadiya.Public()
nadiya.Friend()
nadiya.Only_me()

print("****************************************************")

tamanna.Public()
tamanna.Friend()
tamanna.Only_me()
