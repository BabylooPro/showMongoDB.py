from dotenv import load_dotenv
from pymongo import MongoClient
from bson.json_util import loads
from pprint import pprint
from io import StringIO
import sys
import os

load_dotenv()

# CONFIGURING CONNECTION TO MONGODB | REPLACE <USERNAME>, <PASSWORD> AND <CONNECTION> BY YOURS
uri = "mongodb+srv://<USERNAME>:<PASSWORD>@<CONNECTION>.rrvp2xw.mongodb.net/?retryWrites=true&w=majority"
mongodb_uri = uri
client = MongoClient(mongodb_uri)
db = client[""] # enter database name client
collection = db[""] # enter collection name database

# SHOW ONLY SCRIPT IN TERMINAL
def clear_terminal():
    if os.name == 'nt': #Windows
        os.system('cls')
    else:
        os.system('clear') #Linux | macOS
clear_terminal()

# GET TOTAL NUMBER DOCUMENTS IN COLLECTION
def get_total_documents():
    return collection.count_documents({})

# DISPLAY COLLECTION DATA
def show_data(counter=1):
    name_db = db.name
    name_collection = collection.name
    data = collection.find()

    print()
    print(f"SHOW DATA IN {name_db.upper()}.{name_collection.upper()} (TOTAL : {get_total_documents()})")
    print()

    for data in data:
        data_text = f"DATA : N°{counter}"

        # USE STRINGIO TO CAPTURE OUTPUT PPRINT
        temp_stdout = StringIO()
        sys.stdout = temp_stdout
        pprint(data)
        sys.stdout = sys.__stdout__

        # CALCULATE LENGTH OF LONGEST LINE IN THE PPRINT OUTPUT
        longest_line = max(len(line) for line in temp_stdout.getvalue().split('\n'))

        print(data_text)
        print(temp_stdout.getvalue().rstrip()) # DISPLAY PPRINT OUTPUT WITHOUT LAST LINE BREAK
        print("-" * longest_line)
        counter += 1

    return counter

# DISPLAY NEW DATA
def show_new_data(new_data, counter):
    clear_terminal()
    counter_initial = show_data(counter - 1)  # SHOW PREVIOUS DATA
    print(f"NEW DATA : N°{counter}")
    pprint(new_data)
    return counter + 1

# LISTEN CHANGES IN COLLECTION
def listen_modify(counter_initial):
    counter = counter_initial
    try:
        with collection.watch() as stream:
            while stream.alive:
                try:
                    update = stream.next()
                    new_data_id = update['documentKey']['_id']
                    new_data = collection.find_one({'_id': new_data_id})
                    counter = show_new_data(new_data, counter)
                except StopIteration:
                    pass
    except KeyboardInterrupt:
        clear_terminal()
        filename = os.path.basename(__file__)
        print(f"CLOSING OF {filename.upper()}")
        sys.exit(0)

counter_initial = show_data() # DISPLAY INITIAL DATA OF COLLECTION
listen_modify(counter_initial) # LISTEN CHANGES IN COLLECTION
