let str = 'select sum(e.salary) as total, d.department_name\n' +
    'from hr.employees e, hr.departments d\n' +
    'where e.department_id = d.department_id\n' +
    'group by (d.department_name);';

console.log(str.toUpperCase());