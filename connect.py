from library import *

server = "DESKTOP-IJ0SBSB"
database = "GP-GUI"
tableName = 'Data'
connectionString = f'DRIVER=SQL SERVER;SERVER={server};DATABASE={database};'


def updateDatabase(imagePath, name, date):
    conn = pyodbc.connect(connectionString)

# Create a cursor from the connection
    cursor = conn.cursor()
    with open(imagePath, 'rb') as f:
        imageData = f.read()            # Cnvert Image To Byte Array Because Put On The Database 
    dataToInsert = (imageData, name, date)  # Replace with actual values

# Use parameterized query to prevent SQL injection
    insertQuery = f"INSERT INTO {tableName} (images, Name, Date) VALUES (?, ?, ?)"
    cursor.execute(insertQuery, dataToInsert)

# Commit the transaction
    conn.commit()

# Close the cursor and connection
    cursor.close()
    conn.close()
    print(f"Close connection to this server: {server}\nand the database: {database}")

