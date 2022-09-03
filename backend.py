import eel
import pymongo

eel.init('web')

client = pymongo.MongoClient('mongodb://localhost:27017')
database = client['TaskList']
collection = database['Tasks']
@eel.expose
def addTask(s):
    task = {
        "Task" : f"{s}"
    }
    collection.insert_one(task)


eel.start("index.html")
