import sqlite3
import datetime
class Database_controlinator():
    def __init__(self):
        self.conn = sqlite3.connect('database/songs.db')
        self.c = self.conn.cursor()
    #insterts new song into database
    def insert_song_into_db(self, song_name: str, song_link:str, first_played:datetime, played_by:int):
        #make query to database to insert song
        res = self.c.execute("INSERT INTO songs(song_name, song_link, first_played, played_by, skips) VALUES(?, ?, ?, ?, ?)", (song_name, song_link, first_played, played_by, 0))        
        self.conn.commit()
        print(res)
        if res.rowcount == 1:
            return True
        else:
            return False
    
    def add_song_skip(self, song_id:int):
        res = self.c.execute("UPDATE songs SET skips = skips + 1 WHERE rowid = ?", (song_id,))
        self.conn.commit()
        if res.rowcount == 1:
            return True
        else:
            return False
    
    def get_song_by_id(self, song_id:int):
        res = self.c.execute("SELECT * FROM songs WHERE rowid = ?", (song_id,))
        return res.fetchone()
    
    def check_if_song_link_exists(self, song_link:str):
        res = self.c.execute("SELECT rowid FROM songs WHERE song_link = ?", (song_link,))
        if res.rowcount == 0:
            return False
        else:
            return res.fetchone()[0]
    
    def get_all_songs(self):
        res = self.c.execute("SELECT * FROM songs")
        return res.fetchall()
    

