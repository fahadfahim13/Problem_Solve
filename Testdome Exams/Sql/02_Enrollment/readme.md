## Question
A table containing the students enrolled in a yearly course has incorrect data 
in records with ids between _20 and 100 (inclusive)_.

```sql
TABLE enrollments
  id INTEGER NOT NULL PRIMARY KEY
  year INTEGER NOT NULL
  studentId INTEGER NOT NULL
```

Write a query that updates the field 'year' of every faulty record to 2015.