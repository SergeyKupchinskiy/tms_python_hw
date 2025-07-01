create table users (
id int unsigned primary key auto_increment,
username varchar(64) unique not null,
password varchar(64) not null,
email varchar(64) default 'email не указан' not null
);

create table orders (
id int unsigned primary key auto_increment,
user_id int unsigned not null,
product_id int unsigned not null,
count int unsigned not null,

foreign key (user_id) references users(id)
);

create table products (
id int unsigned primary key auto_increment,
name varchar(64) not null,
cost int unsigned not null,
count int unsigned not null,
seller_id int unsigned not null
);

alter table orders add foreign key (product_id) references products(id);

create table seller (
id int unsigned primary key auto_increment,
company varchar(64) unique not null,
phone varchar(20) default 'Телефон не указан' not null
);

alter table products add foreign key (seller_id) references seller(id);