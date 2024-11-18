import json
data = {}
data["page"] = 1
data["total_users"] = 3
data["users"] = []

source_user = [
    {"id" : 1, "name": "alice", "email": "alice@exemple.com", "roles":["admin"]},
    {"id" : 2, "name": "Bob", "email": "Bob@exemple.com", "roles":["editor", "viewer"]},
    {"id" : 3, "name": "Bob33", "email": "Bob33@exemple.com", "roles":["editor", "viewer"]},
]

for user in source_user:
    data["users"].append(user)

print(data)

jsondata = json.dumps(data)

print(jsondata)