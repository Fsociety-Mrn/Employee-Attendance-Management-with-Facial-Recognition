# import required modules
from pickle import FALSE, TRUE
import mysql.connector
from datetime import datetime

host="localhost"
user="root"
password=""
database="cognate1"


# conection of databse
data = mysql.connector.connect(host=host, user=user, password=password,database=database)

cursor = data.cursor()
        
# show all tables
def __listOfTables(index):
	cursor.execute("SHOW TABLES")
	
	listTableName= []
	results = cursor.fetchall()
	for x in results:
		removeComa = str(x).replace(",","")
		removeApo = removeComa.replace("'","")
		removeParentL = removeApo.replace("(","")
		removeParentR = removeParentL.replace(")","")
		listTableName.append(removeParentR)
    
	return listTableName.count(index)

# create table
def createTable():
    try:
        
        # check if table is exist
        if __listOfTables(str(datetime.today().strftime('%Y-%m-%d'))) == 0:
        
            data._open_connection()
            cursor.execute("CREATE TABLE `" + 
            str(datetime.today().strftime('%Y-%m-%d')) + 
            "` (Name VARCHAR(255) PRIMARY KEY, TimeIn VARCHAR(255), TimeOut VARCHAR(255));")
            print("New table created")
            data.close()
            
            return True
    except mysql.connector.Error as Err:
        # print(Err)
        return False
     

def updateRow(Name):
    try:
        data._open_connection()
        cursor.execute("UPDATE `"+
            str(datetime.today().strftime('%Y-%m-%d')) +
        	"` SET `TimeOut` = '" + str(datetime.now().strftime('%I:%M %p')) + "' WHERE Name = '" + Name + "'")
        data.commit()
        print("Success updated")
        data.close()
        return cursor.rowcount
  
    except mysql.connector.Error as Err:
        print(Err)

def addRow(Name):
    try:
        data._open_connection()
        cursor.execute("INSERT INTO `" +
            str(datetime.today().strftime('%Y-%m-%d')) + 
            "` (`Name`, `TimeIn`) VALUES ('" + Name + "','" + str(datetime.now().strftime('%I:%M %p')) + "')")
        data.commit()
        print("Success insert")
        data.close()
        return False
  
    except mysql.connector.Error as Err:
        # print(Err)
        updateRow(Name)
        return True
        
def __addupdateRow(Name):
    try:
        if addRow(Name,str(datetime.now().strftime('%I:%M %p'))):
            updateRow(Name, str(datetime.now().strftime('%I:%M %p')))       
    except Exception as e: 
        print(e)

        
# delete table
def __deleteTable(tableName):
    cursor.execute("DROP TABLE " + tableName + ";")

# create table mano mano
def __createTassble():
    try:
        cursor.execute("CREATE TABLE `MASTERLIST` (`ID` INT NOT AUTO_INCREMENT, PRIMARY KEY, username VARCHAR(255), password VARCHAR(255));")
        print("New table created")
        return True
    except mysql.connector.Error as Err:
        print(Err)
        return False

# SELECT specific row and column MASTERLISt
def selectTable(ID):
    try:
        data._open_connection()
        cursor.execute("SELECT `Name` FROM `masterlist` WHERE ID=" + ID + ";")
        
        print(cursor.fetchone()[0])
        # cursor.execute("set session wait_timeout=300;")
        data.close()
        return 1
    except Exception as Err:
        data.close()
        return 0

# login details
def login(usrname,psswrd):
    try:
        # data._open_connection()
        cursor.execute("SELECT `ID` FROM admin WHERE username='"+ usrname +"' AND password='" + psswrd +"';")
        
        print(cursor.fetchone()[0])
        # data.close()
        return True
    except Exception as Err:
        print(Err)
        return False

def insert(ID,Name):
    try:
        data._open_connection()
        cursor.execute("INSERT INTO `masterlist` (ID,Name) VALUES ('" + ID + "','"+ Name+"');")
        data.commit()
        print("Success insert")
        data.close()
        return 1
    except Exception as Err:
        print(Err)
        return 0
    

