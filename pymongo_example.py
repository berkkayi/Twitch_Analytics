import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
twitchdb = myclient["TwitchChatDB"]
twitchusers = twitchdb["TwitchUsers"]
print(myclient.list_database_names())

with open("chat.log", "r") as file:
    chats = file.read()
#print(chats.split("\n\n")[50:51])
#print(chats.split("\n\n")[51:52])
#columns = [col.strip() for col in chats.split("\n\n").split(':') if col]
#print(columns)
#mydict = {"_id":0,"name":"Berk","surname":"Kayı"}
#mydict2 = {"channel":"Clumsykitty","username":"berk_owich"}
#x = twitchusers.insert_one(mydict)
z = twitchusers.find()

for rows in z:
    print(rows)
