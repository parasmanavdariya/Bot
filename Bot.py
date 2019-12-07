import datamodule as dm

#Banner
print("#"*50)
print('-'*10 + " BOT by Paras Manavdariya " + '-'*10)
print("#"*50)
#End Banner



auth=input("auth ")
des=input("des ")

Note = {
  "Auther":auth,
  "Description": des,
}

dm.add(Note)

dm.show()

