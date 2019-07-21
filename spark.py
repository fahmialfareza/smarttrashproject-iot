from pymongo import MongoClient
from bson.objectid import ObjectId
import json
import time

while True:
	# Mongo 1
	client = MongoClient('mongodb://192.168.56.121') #bisa berparameter domain dan port tujuan
	db = client.skt
	collection = db.sensor2

	documents = collection.find({})
	for document in documents:
		temp = document

	data1 = dict(temp)
	operasi = 100 - ((data1['t_sampah']/data1['t_total'])*100)

	#id = str(data1['_id']).replace("ObjectId(","")
	#id = id.replace()
	#print(data1['_id'])
	filter_document = {
	    "_id" : ObjectId(str(data1['_id']))
	}
	set_new_document = {
	    "$set": {
	        "persentase": operasi
	    }
	}
	result = collection.update(filter_document, set_new_document, upsert=False, multi=True)
	print(result)

	documents = collection.find({})
	for document in documents:
		temp = document

	data1 = dict(temp)
	print(data1)

	# Mongo 2
	client1 = MongoClient("mongodb://192.168.56.122") #bisa berparameter domain dan port tujuan
	db1 = client1.skt
	collection1 = db1.sensor2

	documents1 = collection1.find({})
	for document1 in documents1:
		temp1 = document1

	data2 = dict(temp1)
	operasi1 = 100 - ((data2['t_sampah']/data2['t_total'])*100)

	#id = str(data1['_id']).replace("ObjectId(","")
	#id = id.replace()
	#print(data1['_id'])
	filter_document1 = {
	    "_id" : ObjectId(str(data2['_id']))
	}
	set_new_document1 = {
	    "$set": {
	        "persentase": operasi1
	    }
	}
	result1 = collection1.update(filter_document1, set_new_document1, upsert=False, multi=True)
	print(result1)

	documents1 = collection1.find({})
	for document1 in documents1:
		temp1 = document1

	data2 = dict(temp1)
	print(data2)

	# Mongo 3
	client2 = MongoClient("mongodb://127.0.0.1") #bisa berparameter domain dan port tujuan
	db2 = client2.skt
	collection2 = db2.sensor2

	documents2 = collection2.find({})
	for document2 in documents2:
		temp2 = document2

	data3 = dict(temp2)
	operasi2 = 100 - ((data3['t_sampah']/data3['t_total'])*100)

	#id = str(data1['_id']).replace("ObjectId(","")
	#id = id.replace()
	#print(data1['_id'])
	filter_document2 = {
	    "_id" : ObjectId(str(data3['_id']))
	}
	set_new_document2 = {
	    "$set": {
	        "persentase": operasi2
	    }
	}
	result2 = collection2.update(filter_document2, set_new_document2, upsert=False, multi=True)
	print(result2)

	documents2 = collection2.find({})
	for document2 in documents2:
		temp2 = document2

	data3 = dict(temp2)
	print(data3)

	time.sleep(1)
