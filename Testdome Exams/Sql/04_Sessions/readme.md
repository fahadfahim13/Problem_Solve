## Question
App usage data are kept in the following table:

```sql
TABLE sessions
id INTEGER PRIMARY KEY,
userId INTEGER NOT NULL,
duration DECIMAL NOT NULL
```

Write a query that selects userId and average session duration for each user who has more than one session.

Suggested testing environment:
http://sqlite.online/
