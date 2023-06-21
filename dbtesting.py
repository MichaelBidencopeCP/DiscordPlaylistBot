import sqlite3

con = sqlite3.connect('/home/mike/github/DiscordPlaylistBot/songs.db')

cur = con.cursor()

res = cur.execute("SELECT name FROM sqlite_master WHERE type='table';")

#print all tables
print(res.fetchone())
