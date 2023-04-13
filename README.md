# showMongoDB.py


https://user-images.githubusercontent.com/35376790/231833685-74e6472a-7ceb-4a98-908b-01b5f3c7657c.mov


This Python script, [showMongoDB.py](showMongoDB.py), is designed to display the content of a MongoDB collection in real-time, including any changes made to the collection. 
The script connects to a MongoDB Atlas cluster, retrieves data from the specified database and collection, and continuously listens for any updates.

## Features

- Connects to a MongoDB Atlas cluster using a connection string
- Clears the terminal screen to display only the script
- Retrieves the total number of documents in a collection
- Prints the data in the collection with proper formatting
- Listens for changes in the collection and displays new data in real-time

## How to Use

1. Make sure you have installed the required packages listed in the [requirements.txt](requirements.txt) file. If not, run `pip install -r requirements.txt`.
2. Edit script to set up your MongoDB connection string. Replace `<USERNAME>`, `<PASSWORD>`, and `<CONNECTION>` with your own values.
3. Or set up your `.env` file with the MongoDB connection string. Replace `<USERNAME>`, `<PASSWORD>`, and `<CONNECTION>` with your own values.
4. Replace the `db` and `collection` placeholders with the desired database and collection names.
5. Run the script using `python showMongoDB.py`. The script will display the collection's data in the terminal and update it in real-time as changes occur.

## Dependencies

- `pymongo`: For connecting to and interacting with MongoDB
- `dotenv`: For loading environment variables from the `.env` file
- `bson.json_util`: For converting BSON data to JSON
- `pprint`: For pretty-printing the data
- `io.StringIO`: For capturing the output of `pprint`
- `os`: For clearing the terminal screen
- `sys`: For working with the standard output (`stdout`)

## Sample Output

```
SHOW DATA IN DATABASE_NAME.COLLECTION_NAME (TOTAL : 2)

DATA : N°1
{
    '_id': ObjectId('...'),
    'field1': 'value1',
    'field2': 'value2',
    ...
}
----------------------------
DATA : N°2
{
    '_id': ObjectId('...'),
    'field1': 'value1',
    'field2': 'value2',
    ...
}
----------------------------
