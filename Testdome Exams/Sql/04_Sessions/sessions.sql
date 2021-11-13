select userId, avg(duration) from sessions
group by userId
having count(userId) > 1;