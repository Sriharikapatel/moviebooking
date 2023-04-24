import MySQLdb

class util:
    def get_connection():
        connection =  MySQLdb.connect(host='127.0.0.1', user='root', passwd='bckk', db='cinemaebooking')
        return connection