import MySQLdb
from xlsxwriter.workbook import Workbook


class backup_itms():
 def backup(self):
   user = 'root' # your username
   passwd = 'rhtdm2' # your password
   host = '127.0.0.1' # your host
   db = 'itms' # database where your table is stored
   table = 'itmsapp_managers' # table you want to save

   conn = MySQLdb.connect(user=user, passwd=passwd, host=host, db=db)
   cursor = conn.cursor()

   query = "SELECT * FROM %s;" % table
   cursor.execute(query)

   workbook = Workbook('/opt/backups/itms.xlsx')
   sheet = workbook.add_worksheet()


   for r, row in enumerate(cursor.fetchall()):
      for c, col in enumerate(row):
          sheet.write(r, c, col)

   cursor.close()
   workbook.close()
   conn.close()