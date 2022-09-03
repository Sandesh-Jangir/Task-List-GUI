import eel
import pymongo


client = pymongo.MongoClient('mongodb://localhost:27017')
database = client['TaskList']
collection = database['Tasks']
@eel.expose
def addTask(s):
    task = {
        "Task" : f"{s}"
    }
    collection.insert_one(task)

@eel.expose
def fetchDocuments():
    documents = collection.find({})
    task_arr = []
    for document in documents:
        task_arr.append(document)
    return task_arr

eel.init('web')

eel.start("index.html")
