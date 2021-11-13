CREATE TABLE users_roles (
  userId INTEGER not null,
  roleId INTEGER not null,
  foreign key (userId) references users(id),
  foreign key (roleId) references roles(id),
  unique (userId, roleId)
);