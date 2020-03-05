# pip install mysql-connector
import mysql.connector

"""
table prepare

CREATE DATABASE demo;
CREATE TABLE `demo`.`grade` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT='年級';

INSERT INTO demo.grade (id, name) VALUES
(1,'一年級'),(2,'二年級'),(3,'三年級'),(4,'四年級'),(5,'五年級'),
(6,'六年級'),(7,'十年級'),(8,'八年級');
"""

# 設定DB連線資訊
demodb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "666666",
    database = "demo"
)

# SELECT
cursor = demodb.cursor()
cursor.execute("SELECT * FROM grade")
result = cursor.fetchall()
for row in result:
    print(row)

# UPDATE
update_grade = "UPDATE grade SET name = '七年級' WHERE id = 7"
cursor.execute(update_grade)
demodb.commit()

cursor.execute("SELECT * FROM grade")
result = cursor.fetchall()
for row in result:
    print(row)