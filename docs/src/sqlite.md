# Sqlite

```
# Show table headers.
.headers ON

# Or beautify the output.
.mode columns

.tables

# Import sql file.
.read file.sql
```

### Dump

Ref: https://stackoverflow.com/a/199221

Dump to a CSV file.

```
.mode csv 
-- use '.separator SOME_STRING' for something other than a comma.
.headers on 
.out file.csv 
select * from MyTable;
```

Dump to SQL file.

```
.mode insert <target_table_name>
.out file.sql 
select * from MyTable;
```
