import sqlite3

# Verefication required to buy and sell automatically, project abandoned for meanwhile

con = sqlite3.connect("mercadata.db")
cur = con.cursor()

cur.execute("SELECT * FROM HYDRO_BTC ORDER BY EntryID DESC LIMIT 1")

all = cur.fetchall()
print(float(all[0][2]) + 21)

con.commit()
con.close()
