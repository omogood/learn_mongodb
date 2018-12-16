from pymongo import MongoClient

class TestMongo:
    """ MongoDB のテスト """
    __client = None
    __db = None

    def __init__(self, host, port, db_name):
        # MongoDB に接続.
        self.__client = MongoClient(host, port)
        # テスト用のデータベースを指定
        self.__db = self.__client[db_name]

    def write_one(self, collection_name, document):
        """ 単一のドキュメントをコレクションに書き込む """
        # コレクションに接続
        collection = self.__db[collection_name]
        result = collection.insert_one(document)
        print(result)

    def write_many(self, collection_name, document):
        """ 複数のドキュメントをコレクションに書き込む """
        # コレクションに接続
        collection = self.__db[collection_name]
        result = collection.insert_many(document)
        print(result)

    def read_one(self, collection_name, key):
        """ コレクションからドキュメントを取得する"""
        collection = self.__db[collection_name]
        return collection.find_one(key)

    def read_all(self, collection_name, key):
        """ コレクションからドキュメントを取得する"""
        collection = self.__db[collection_name]
        return collection.find(key)

def main():
    host = 'localhost'
    port = 27017
    db_name = 'test-database'
    collection = 'test-collection'

    testdb = TestMongo(host, port, db_name)

    test_documents = [{
                        "age":"20",
                        "sex":"men",
                        "from":"oosaka"
                    },
                    {
                        "age":"25",
                        "sex": "wemon",
                        "from": "tokyo"
                    },
                    {
                        "age":"50",
                        "sex": "men",
                        "from": "kyoto"
                    },
                    {
                        "age":"45",
                        "sex": "wemen",
                        "from": "kobe"
                    }]

    # テスト用データの挿入
    #testdb.write_many(collection, test_documents)

    for i in testdb.read_all(collection, {"sex":"men"}):
        print(i)

if __name__ == '__main__':
    main()
