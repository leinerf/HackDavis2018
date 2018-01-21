from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db = client['test-database']
posts = db.posts

# post = {
# 	'Name': "Freniel",
# 	'Math': [{'num':6,'denom':12},{'num':4,'denom':6},{'num':10,'denom':20}],
# 	'English': [{'num':1,'denom':10},{'num':2,'denom':10},{'num':3,'denom':10}],
# 	'Science': [{"num":2,"denom":10},{"num":3,"denom":10},{"num":4,"denom":5},{"num":1,"denom":3}]
# }

# post = {
# 	'Name': "Briana",
# 	'Math': [{'num':3,'denom':12},{'num':4,'denom':6},{'num':10,'denom':20}],
# 	'English': [{'num':1,'denom':10},{'num':8,'denom':10},{'num':9,'denom':16}],
# 	'Science': [{"num":2,"denom":20},{"num":7,"denom":10},{"num":4,"denom":8},{"num":3,"denom":3}]
# }

# post = {
# 	'Name': "Marty",
# 	'Math': [{'num':6,'denom':12},{'num':8,'denom':10},{'num':2,'denom':5}],
# 	'English': [{'num':3,'denom':8},{'num':13,'denom':17},{'num':3,'denom':10}],
# 	'Science': [{"num":3,"denom":10},{"num":6,"denom":12},{"num":12,"denom":15},{"num":1,"denom":3}]
# }

# post = {
# 	'Name': "Aziz",
# 	'Math': [{'num':5,'denom':8},{'num':2,'denom':5},{'num':10,'denom':20}],
# 	'English': [{'num':10,'denom':10},{'num':8,'denom':12},{'num':6,'denom':11}],
# 	'Science': [{"num":2,"denom":10},{"num":3,"denom":10},{"num":4,"denom":5},{"num":14,"denom":18}]
# }

post = posts.insert_one(post).inserted_id
print(post)

