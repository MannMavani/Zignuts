contacts={
    "1":{
        "name":"John",
        "phone":"1234567890",
        "email":"john@example.com",
        "address":{
            "street":"123 Main St",
            "city":"Anytown",
            "state":"CA",
            "zip":"12345"
        }
    },
    "2":{
        "name":"Jane",
        "phone":"0987654321",
        "email":"jane@example.com",
        "address":{
            "street":"456 Main St",
            "city":"Anytown",
            "state":"CA",
            "zip":"12345"
        }
    },
    "3":{
        "name":"Jim",
        "phone":"1234567890",
        "email":"jim@example.com",
        "address":{
            "street":"789 Main St",
            "city":"Anytown",
            "state":"CA",
            "zip":"12345"
        }
    }
}
print("---------------------------------------------------------------")
print("All contacts:")
print(contacts)
print("---------------------------------------------------------------")
print("Contact 1:")
print(contacts["1"])
print("---------------------------------------------------------------")
print("Contact 1 address:")
print(contacts["1"]["address"])
print("---------------------------------------------------------------")
print("Contact 1 address street:")
print(contacts["1"]["address"]["street"])
print("---------------------------------------------------------------")
