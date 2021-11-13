select name from employees
where id not in
(select e1.id from employees as e1 join employees as e2 on e1.id = e2.managerId); -- Managers ids