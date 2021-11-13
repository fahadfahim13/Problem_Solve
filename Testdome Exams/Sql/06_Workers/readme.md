## Question
The following data definition defines an organization's employee hierarchy.

An employee is a manager if any other employee has their `managerId` set to this 
employee's `id`. That means John is a manager if at least one other employee has 
their `managerId` set to John's `id`.

```sql
TABLE employees
  id INTEGER NOT NULL PRIMARY KEY
  managerId INTEGER REFERENCES employees(id)
  name VARCHAR(30) NOT NULL
```

Write a query that selects only the names of employees who are not managers.