Tasks on 0x14-mysql

## Installtion of mysql 5.7
First go to site dev.mysql.com and copy the PGP PUBLIC KEY just immediately under the Notice section to your clipboard.

Create a new file in your terminal with a .key extension and paste the PGP PUB KEY copied to clipboard.

-- Then do follow the steps below
$ sudo apt-key add name_of_file.key
OK

# adding it to the apt repo
$ sudo sh -c 'echo "deb http://repo.mysql.com/apt/ubuntu bionic mysql-5.7" >> /etc/apt/sources.list.d/mysql.list'

# updating the apt repo to add the url i added earlier
$ sudo apt-get update

# now check your available versions
$ sudo apt-cache policy mysql-server
mysql-server:
  Installed: (none)
  Candidate: 8.0.31-0ubuntu0.20.04.2
  Version table:
     8.0.31-0ubuntu0.20.04.2 500
        500 http://us-east-1.ec2.archive.ubuntu.com/ubuntu focal-updates/main amd64 Packages
     8.0.31-0ubuntu0.20.04.1 500
        500 http://security.ubuntu.com/ubuntu focal-security/main amd64 Packages
     8.0.19-0ubuntu5 500
        500 http://us-east-1.ec2.archive.ubuntu.com/ubuntu focal/main amd64 Packages
     5.7.40-1ubuntu18.04 500
        500 http://repo.mysql.com/apt/ubuntu bionic/mysql-5.7 amd64 Packages

# Now am installing mysql 5.7.*
$ sudo apt-get install -f mysql-client=5.7* mysql-community-server=5.7* mysql-server=5.7* -y

## Creating a user and Granting Priviledges in mysql
$ mysql -root -p
Password:	/* Type root password

mysql> CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';

mysql> GRANT GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';

mysql> FLUSH PRIVILEGES;

## Creating DAtabase, Tables and adding Data to the Tables
mysql> CREATE DATABASE tyrell_corp;

-- To verify if db is created
mysql> SHOW DATABASES;

mysql> tyrell_corp;

mysql> CREATE TABLE nexus6 (
    -> id INT,
    -> name VARCHAR(100));
-- you can add as many columns as you want. I added two columns(id and name)

mysql> INSERT INTO table_name VALUES (1, Leon);

-- Verify if data was added succesfully do
mysql> SELECT id, name FROM nexus6;

## Setting Up MySQL Replication
mysql> CREATE USER 'replica_user'@'%' IDENTIFIED BY 'replica_user_pwd';

mysql> GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';

mysql> FLUSH PRIVILEGES;

mysql> exit

## Next up you go to the /etc/mysql/mysql.conf.d/mysqld.cnf and comment the bind address and then add this lines to it
# By default we only accept connections from localhost
# bind-address = 127.0.0.1
server-id = 1
log_bin = /var/log/mysql/mysql-bin.log
binlog_do_db = tyrell_corp

## Then you enable incoming connection to port 3306 and restart mysql-server
$ sudo ufw allow from 'replica_server_ip' to any port 3306

$ sudo service mysql restart

## Now log back in to mysql-server to lock db and prepare binary file for replication.
$ mysql -uroot -p
password:


mysql> 

mysql> FLUSH TABLES WITH READ LOCK;

mysql> SHOW MASTER STATUS;
#Take note of the binary log and the position, jot it down or you leave this window open and you open another window to continue

## you then export the db from myql-server to local machine and then copy this db to replica machine
$ mysqldump -uroot -p db_name > export_db_name.sql

$ scp -i _idenetity_file_ export_db_name.sql user@machine_ip:location

## Then ssh to replica machine ip_adress to import this tables to replica mysql-server
$ mysql -uroot -p 
password:


mysql> CREATE DATABASE db_name;

mysql>exit
bye

$ mysql -uroot p db_name < export_db_name.sql
password:

# Now edit the config file in /etc/mysql/mysql.conf.d/mysqld.cnf and then reload mysql-server

```bash

server-id = 2
log_bin = /var/log/mysql/mysql-bin.log
binlog_do_db = db_name_from_master_mysql-server
relay_log = /var/log/mysql/mysql-relay-bin.log

$ sudo service mysql restart

## Login to mysql server in replica to configure replication


$ mysql -uroot -p
password:


mysql>

mysql> CHANGE MASTER TO
    -> MASTER_HOST='source_host_name',
    -> MASTER_USER='replication_user_name',
    -> MASTER_PASSWORD='replication_password',
    -> MASTER_LOG_FILE='recorded_log_file_name',
    -> MASTER_LOG_POS=recorded_log_position;

-- Then you start slave
mysql> START SLAVE;
