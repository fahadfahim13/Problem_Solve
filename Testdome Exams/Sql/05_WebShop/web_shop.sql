select i.name, s.name from items as i, sellers as s
where s.id = i.sellerId and
s.rating > 4;

select items.name, sellers.name from items
join sellers on items.sellerId = sellers.id
where sellers.rating > 4;