from bson.json_util import dumps
from pymongo import MongoClient, cursor

client = MongoClient("MONGODB--URL")
db=client.test
col = db.userpayments

JoinAndQuery = db.userpayments.aggregate(
    [        
        {
            "$lookup":{
                "from": "users",       
                "localField": "userId",       
                "foreignField": "_id",      
                "as": "joined_collections"   
            },         
        }
        ,
        {
          "$match":
            {
                "appType": { "$eq":  "android" },
                "receipt": { "$ne": None},
                "productId": { "$ne": None},

            }
        },
        {
          "$project":
            {
                "appType": 1,
                "productId": 1,
                "joined_collections.customer_id": 1 ,
                "receipt.purchaseToken": 1,
                "_id": 0,
                
            }
        }
    ]
)

list_cur = list(JoinAndQuery)
json_data = dumps(list_cur, indent= 2)        

with open('androidOutput.json', 'w') as file:
   file.write(json_data)
