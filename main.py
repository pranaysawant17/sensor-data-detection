from sensor.configuration.mongodb_connection import MongoDBClient

if __name__ == "__main__":
    mongodb_cli=MongoDBClient()
    print("collection_name:", mongodb_cli.database.list_collection_names())