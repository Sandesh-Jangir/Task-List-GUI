import eel
import pymongo

eel.init('web')

client = pymongo.MongoClient('mongodb://localhost:27017')
database = client['TaskList']
collection = database['Tasks']
task = {
    "Task" : "Sample Task"
}
collection.insert_one(task)

eel.start("index.html")