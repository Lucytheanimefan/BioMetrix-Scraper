from pymongo import MongoClient

def get_db():
    client = MongoClient('mongodb://heroku_lncvx2h4:1c9jb96b8dp0kr5vbo27kvqoju@ds161487.mlab.com:61487/heroku_lncvx2h4')
    db = client.heroku_rfsb5xrr
    return db