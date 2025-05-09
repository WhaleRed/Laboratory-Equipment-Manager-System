import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

db = mysql.connector.connect(
  host= os.getenv("DATABASE_HOST"),
  user = os.getenv("DATABASE_USER"),
  password= os.getenv("DATABASE_PASSWORD"),
  database= os.getenv("DATABASE_NAME")
)

#Must pass an Array of Values 
#On dates format must be 'YYYY-MM-DD'


def addBorrower(borrower):
  mycursor = db.cursor()
  try:
    mycursor.execute("INSERT INTO borrower VALUE (%s, %s, %s, %s, %s, %s)", borrower)
    db.commit()
    return 0
  except mysql.connector.IntegrityError as e:
    if e.errno == 1062:
      return 1
  finally:
    mycursor.close()

def addProfessor(professor):
  mycursor = db.cursor()
  try:
    mycursor.execute("INSERT INTO professor VALUE (%s, %s, %s)", professor)
    db.commit()
    return 0
  except mysql.connector.IntegrityError as e:
    if e.errno == 1062:
      return 1
  finally:
    mycursor.close()

def addEquipment(equipment):
  mycursor = db.cursor()
  try:
    mycursor.execute("INSERT INTO equipment VALUE (%s, %s, %s, %s)", equipment)
    db.commit()
    return 0
  except mysql.connector.IntegrityError as e:
    if e.errno == 1062:
      return 1
  finally:
    mycursor.close()

def addBorrowedEquipment(equipment):
  mycursor = db.cursor()
  try:
    mycursor.execute("INSERT INTO borrowed_equipment VALUE (%s, %s, %s)", equipment)
    db.commit()
    return 0
  except mysql.connector.IntegrityError as e:
    if e.errno == 1062:
      return 1
  finally:
    mycursor.close()

def addReplacedEquipment(equipment):
  mycursor = db.cursor()
  try:
    mycursor.execute("INSERT INTO replaced_equipment VALUE (%s, %s, %s)", equipment)
    db.commit()
    return 0
  except mysql.connector.IntegrityError as e:
    if e.errno == 1062:
      return 1
  finally:
    mycursor.close()

def addReturnedEquipment(equipment):
  mycursor = db.cursor()
  try:
    mycursor.execute("INSERT INTO returned_equipment VALUE (%s, %s, %s, %s)", equipment)
    db.commit()
    return 0
  except mysql.connector.IntegrityError as e:
    if e.errno == 1062:
      return 1
  finally:
    mycursor.close()