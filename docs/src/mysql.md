# MySQL

## Show character set

Show client connection character set.

```
SHOW VARIABLES LIKE 'character_set%';
```

Show character set for a database.

```
SELECT default_character_set_name FROM information_schema.SCHEMATA
WHERE schema_name = "db_name";
```

Show character set for a table

```
SELECT CCSA.character_set_name FROM information_schema.`TABLES` T,
       information_schema.`COLLATION_CHARACTER_SET_APPLICABILITY` CCSA
WHERE CCSA.collation_name = T.table_collation
  AND T.table_schema = "db_name"
  AND T.table_name = "table_name";
```

Show character set for a column

```
SELECT character_set_name FROM information_schema.`COLUMNS`
WHERE table_schema = "db_name"
  AND table_name = "table_name"
  AND column_name = "column_name";
```

## Show table status of a database

```
SHOW TABLE STATUS FROM <db_name>;
```

## Show columns

```
SHOW FULL COLUMNS FROM <table_name>;
```

## Connect to mysql-server with customized character set

```
mysql -uroot -ppassword --default-character-set=utf8
```

## Show client connection collation

```
SHOW VARIABLES LIKE 'collation%';
```

## Create database

```
CREATE DATABASE dbname;
CREATE DATABASE IF NOT EXISTS dbname CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE DATABASE dbname CHARACTER SET utf8 COLLATE utf8_general_ci;
```

## Manage table

```
SHOW INDEX FROM table_name

# This can show table constraints.
SHOW CREATE TABLE table_name;

# This can delete a table constraint.
ALTER TABLE table_name
  DROP INDEX index_name;
```

### Add column

```
ALTER TABLE table_name ADD COLUMN column_name INT NOT NULL;

# Add several columns. `column_name_1` will be the last column of the table.
# `column_name_2` will be the first column. `column_name_3` will be after the
# column named by `an_existing_column`.
ALTER TABLE table_name
  ADD COLUMN column_name_1 VARCHAR(255),
  ADD COLUMN column_name_2 DATETIME FIRST,
  ADD COLUMN column_name_3 VARCHAR(255) AFTER an_existing_column;

ALTER TABLE table_name
  ADD COLUMN column_name INT NOT NULL,
  ADD FOREIGN KEY staff_id_fk(staff_id) REFERENCES staff(id);

ALTER TABLE staff ADD COLUMN downloaded bit(1) NOT NULL DEFAULT b'0';
```

Ref: https://www.mysqltutorial.org/mysql-add-column/

### Modify column

```
ALTER TABLE table_name MODIFY column_name BIGINT(20) DEFAULT NULL;
```

## Index/Constraints

```
ALTER TABLE table_name ADD CONSTRAINT constraint_name UNIQUE (column_1, column_2, column_3);
```

## Insert/Update/Delete

```
insert into table_name(column1, column2) values('foo', 'bar');

update table_name set column1 = 1, column2 = 'foo' where id = 1;

delete from table_name where id = 1;
```

## Execute MySQL command by docker

For docker on Mac, use `host.docker.internal` to connect to the host.

```
alias mysql="docker run --rm --network host mysql:5.7.32 mysql"
alias mysqldump="docker run --rm --network host mysql:5.7.32 mysqldump"
```

## MySQL Dump

### Dump schema

```
# Dump a complete database with data.
# This doesn't include a `CREATE DATABASE` statement.
mysqldump -u$USER -h "$HOST" -p$PASSWORD "$DBNAME" >dump.sql

# Dump a complete database without data.
mysqldump "$DBNAME" --no-data >dump.sql

# Dump specific tables of a database.
mysqldump "$DBNAME" table1 table2 ... >dump.sql

# By specifying `--databases` option, it include a `CREATE DATABASE` statement.
mysqldump --databases "$DBNAME1" >dump.sql

# Add `DROP DATABASE` statement before `CREATE DATABASE` statement.
mysqldump --databases "$DBNAME1" --add-drop-database >dump.sql

# Dump several databases.
mysqldump --databases "$DBNAME1" "$DBNAME2" ... >dump.sql

# Dump all databases.
mysqldump --all-databases >dump.sql
```

### Dump data only

```
# Dump all tables data of a database.
mysqldump "$DBNAME" --no-create-info >dump.sql

# Dump specifc tables data.
mysqldump "$DBNAME" table1 table2 ... --no-create-info >dump.sql

# Dump specifc table data with query.
mysqldump "$DBNAME" table1 --no-create-info --where="id <= 10" >dump.sql

# If you add `--databases` option, you also need to add `--no-create-db` to not
# generate `CREATE DATABASE` statement.
mysqldump --databases "$DBNAME" --no-create-db --no-create-info >dump.sql
```

### Load the dump

```
mysql "$DBNAME" <dump.sql
mysql -e "source /path-to-dump.sql" "$DBNAME"
```

## Transaction

Use read-only transaction.

```
# This only works for MySQL 5.6+. By using this, statements like dropping
# tables, deleting columns will not be able to execute.
SET SESSION TRANSACTION READ ONLY;
```
