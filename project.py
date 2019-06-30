import pymysql
import csv
PreviousOrderId = []

db = pymysql.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="kunalrocks123",  # your password
                     db="xeno2")



with db.cursor() as cursor:
    # Create a new record
    with open('Orders.csv', newline='') as csvfile:
        Order = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in Order:
            Units = csv.reader(row, delimiter = ',', quotechar='|')
            for Unit in Units:
                OrderId = Unit[0]
                CustomerPhoneNumber = Unit[1]
                ProductAmount = Unit[2]
                OrderTime = Unit[3]
                StoreLocation = Unit[4]
                ProductId = Unit[5]
                ProductName = Unit[6]
                ProductCategory = Unit[7]
                Quantity = Unit[8]

                if OrderId not in PreviousOrderId:
                    sql1 = "INSERT INTO `Orders` (`OrderId`, `CustomerPhoneNumber`, `TotalOrderAmount`, `OrderTime`, `StoreLocation`) VALUES (%s, %s, %s, %s, %s)"
                    cursor.execute(sql1, (OrderId, CustomerPhoneNumber, ProductAmount, OrderTime, StoreLocation))
                    sql2 = "INSERT INTO `OrderDetails` (`OrderId`, `ProductId`, `ProductName`, `ProductCategory`, `ProductAmount`, `Quantity`) VALUES (%s, %s, %s, %s, %s, %s)"
                    cursor.execute(sql2, (OrderId, ProductId, ProductName, ProductCategory, ProductAmount, Quantity))
                    PreviousOrderId.append(OrderId)
                else:
                    sql1 = "Update `Orders` Set TotalOrderAmount = TotalOrderAmount + %s where OrderId = %s"
                    cursor.execute(sql1, (ProductAmount, OrderId))
                    sql2 = "INSERT INTO `OrderDetails` (`OrderId`, `ProductId`, `ProductName`, `ProductCategory`, `ProductAmount`, `Quantity`) VALUES (%s, %s, %s, %s, %s, %s)"
                    cursor.execute(sql2, (OrderId, ProductId, ProductName, ProductCategory, ProductAmount, Quantity))

db.commit()




    # connection is not autocommit by default. So you must commit to save
    # your changes.

#CREATE TABLE Orders(  OrderId varchar(10) NOT NULL, CustomerPhoneNumber varchar(10) NOT NULL, TotalOrderAmount INT NOT NULL,  OrderTime varchar(50) NOT NULL, StoreLocation VARCHAR(250) , Primary key(OrderId) );
#CREATE TABLE OrderDetails(Id INT AUTO_INCREMENT,  OrderId varchar(10) NOT NULL, ProductId varchar(100) NOT NULL, ProductName varchar(250) NOT NULL,  ProductCategory varchar(50) NOT NULL, ProductAmount INT NOT NULL, Quantity varchar(10) NOT NULL, Primary key(Id) );
