## SQL commands
**Creating a single table:**<br/>
```sql
CREATE TABLE users (
    name VARCHAR(128),
    email VARCHAR(128)
)
```
<br/>**SQL Insert**<br/>
```sql
INSERT INTO users(name, email) VALUES ('prakalp','f20170137@pilani.bits-pilani.ac.in')
```
<br/>**SQL Delete**<br/>
Deletes a row from the table based on a selection criteria<br/>
```sql
DELETE FROM users WHERE email='f20170137@pilani.bits-pilani.ac.in'
```
<br/>**SQL Update**<br/>
Allows updating of a field with a where clause<br/>
```sql
UPDATE users SET name='Prakalp' WHERE email='f20170137@pilani.bits-pilani.ac.in'
```
**Note:** Without WHERE clause it would do for all the rows.<br/>
<br/>**SQL Select**<br/>
The select statement retrieves a group of records - you can either retrieve all the records or a subset of the records with a WHERE clause.<br/>
```sql
SELECT * FROM users
SELECT * FROM users WHERE email='f20170137@pilani.bits-pilani.ac.in'
```
<br/>**Sorting with order by**<br/>
ORDER BY clause used in SELECT statements to get the results sorted in ascending or descending order.<br/>
```sql
SELECT * FROM users ORDER BY name
```
