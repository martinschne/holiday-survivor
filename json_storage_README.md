#Usage
## Create a new storage object
```python
storage = JSONStorage("data.json")
```

## Create
```python
storage.create("name", "John Doe")
storage.create("age", 30)
```

## Read
```python
print(storage.read("phone_number"))  # "491762546852"
print(storage.read("message"))  # "Hello, Philipp here.
```

## Update
```python
storage.update("message", "Hello, Ruslan here.)
print(storage.read("message"))  # "Hello Ruslan, here."
```

## Delete
```python
storage.delete("491762546852") # phone number is the key
```

## Get all data
```python
print(storage.all())  # {'age': 31}
```
# Discussion
- do we treat the phone_number as string or as int?
- after initializing the json storage we should update it directly with received data from sms api. A while loop could request all 5 seconds new sms data could be an option. And every time we have a new or changed entry we should write it to the json storage.