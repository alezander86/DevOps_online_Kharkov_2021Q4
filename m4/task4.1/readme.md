# Task 4.1

*PART 1*

1 and 2. Install MySQL server on VM, configure it and create user:

sudo apt-get install mysql-server -y -- install

sudo mysql_secure_installation --configure

sudo mysql --login

* ![](screen/Screenshot_1.png)

3. Create database on the server:

* ![](screen/Screenshot_2.png)

4. Create tables:

create table client (id integer auto_increment Primary Key, lastName varchar(30), firstname varchar(30));

create table goods (id integer auto_increment Primary Key, goods_name varchar(30), goods_article int);

create table sell (id integer auto_increment Primary Key, client_id INT, goods_id INT, price decimal(10.2));

* ![](screen/Screenshot_3.png)

5. Fill in the tables:

insert into client (lastName, firstname) values ('Vazovski', 'Mike'), ('Ptihkin', 'Alexey'), ('Kylikov', 'Ivan');

insert into goods (goods_name, goods_article) values ('iphone 13', '1111'), ('ipad 3', '5453'), ('ipod', '4534'), ('galaxy s7', '1735');

insert into sell (client_id, goods_id, price) values ('1', '1', '10000'), ('2', '1', '10000'), ('2', '1', '6500'), ('1', '3', '3700'), ('3', '4', '4000'), ('1', '4', '4000');

6. Construct and execute SELECT operator with WHERE, GROUP BY and ORDER BY:

* ![](screen/Screenshot_4.png)

* ![](screen/Screenshot_5.png)

7. Execute other different SQL queries DDL, DML, DCL.

7.1 DDL create, alter, drop, truncate:

create table Iteams (id integer auto_increment Primary Key, Name varchar(30), Number varchar(30)); -- create table

* ![](screen/Screenshot_6.png)

alter tables Iteams ADD price INT NOT NULL; -- add column to table;

* ![](screen/Screenshot_7.png)

truncate table iteams; -- delete all record from table;

* ![](screen/Screenshot_8.png)

Drop table iteams; -- delete table;

* ![](screen/Screenshot_9.png)

7.2 DML insert, update, delete: 

insert into Iteams values (1 ,'chair','5'), (2, 'sofa','2'); -- used to insert data into a table.

* ![](screen/Screenshot_10.png)

update Iteams SET Name = 'bed' where id = 2; -- update existing data within a table.

* ![](screen/Screenshot_11.png)

delete from Iteams where = id '1'; -- delete records from a database table.

* ![](screen/Screenshot_12.png)

7.3 DCL GRANT, REVOKE, DENY:

create user 'taryraiev2'@'%' identified with mysql_native_password by 'Aa11223344+'; -- create user

grant create, alter on *.* to 'taryraiev2'@'%' with grant option; -- add rule create and alter

8. Create a database of new users with different privileges. Connect to the database :

create user 'taryraiev3'@'%' identified with mysql_native_password by 'Aa11223344+'; -- create user

grant drop, delete on *.* to 'taryraiev3'@'%' with grant option;  -- add rule drop and delete

create user 'taryraiev4'@'%' identified with mysql_native_password by 'Aa11223344+'; -- create user

grant select on *.* to 'taryraiev4'@'%' with grant option;  -- add rule select

create user 'taryraiev5'@'%' identified with mysql_native_password by 'Aa11223344+'; -- create user

grant insert, update on *.* to 'taryraiev5'@'%' with grant option;  -- add rule insert, update

flush privileges;

* ![](screen/Screenshot_13.png)

8.1 Verify that the privileges allow or deny certain actions:

* ![](screen/Screenshot_14.png)

9. Make a selection from the main table DB MySQL:

* ![](screen/Screenshot_15.png)

* ![](screen/Screenshot_16.png)

*PART 2*

10. Make backup of your database:

* ![](screen/Screenshot_17.png)

11. Delete the table and/or part of the data in the table.

* ![](screen/Screenshot_18.png)

* ![](screen/Screenshot_19.png)

12. Restore your database:

* ![](screen/Screenshot_20.png)

13. Transfer your local database to RDS AWS:

* ![](screen/Screenshot_21.png)

* ![](screen/Screenshot_22.png)

14. Connect to your database:

* ![](screen/Screenshot_23.png)

15. Execute SELECT operator similar step 6:

* ![](screen/Screenshot_24.png)

* ![](screen/Screenshot_25.png)

16. Create the dump of your database:

* ![](screen/Screenshot_26.png)

*PART 3*

17.Create an Amazon DynamoDB table:

* ![](screen/Screenshot_27.png)


18.Enter data into an Amazon DynamoDB table:

* ![](screen/Screenshot_28.png)

* ![](screen/Screenshot_29.png)

19.Query an Amazon DynamoDB table using Query and Scan:

* ![](screen/Screenshot_30.png)