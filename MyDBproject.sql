create database project;
use project;
create table customer(
customer_id varchar(10) NOT NULL,
  customer_fname varchar(15) NOT NULL,
  customer_lname varchar(15) NOT NULL,
  mail varchar(25) NOT NULL,
  mobile varchar(12) NOT NULL,
  country char(15) NOT NULL,
  Address varchar(45) NOT NULL,
  PRIMARY KEY (`customer_id`));
  
 insert INTO customer(customer_id,customer_fname,customer_lname,mail,mobile,country,Address) values(57896,'alex','robin','alex@gmail.com',8765432101,'USA','12 chapel st new haven');
insert INTO customer(customer_id,customer_fname,customer_lname,mail,mobile,country,Address) values(32529,'max','peter','max@gmail.com',8546357642,'USA','13 wing st bridgeport');
insert INTO customer(customer_id,customer_fname,customer_lname,mail,mobile,country,Address) values(85289,'arun','reddy','arun@gmail.com',2104568243,'USA','14 chapel st new haven');
insert INTO customer(customer_id,customer_fname,customer_lname,mail,mobile,country,Address) values(25332,'michal','jackson','jackson@gmail.com',4521789654,'USA','15 wing st bridgeport');
insert INTO customer(customer_id,customer_fname,customer_lname,mail,mobile,country,Address) values(85287,'viay','Rao','vijay@gmail.com',7549632154,'USA','120 chapel st new haven');
insert INTO customer(customer_id,customer_fname,customer_lname,mail,mobile,country,Address) values(25338,'harish','naidu','harish@gmail.com',5450012364,'USA','131 wing st bridgeport');
 
 create table products(
   product_id varchar(10) NOT NULL,
   product_name varchar(10) NOT NULL,
   product_color varchar(15) NOT NULL,
   quality_type  varchar(5) NOT NULL,
   price  decimal NOT NULL,
   model_no int NOT NULL,
  PRIMARY KEY (`product_id`));
  
insert into products(product_id, product_name, product_color, quality_type, price, model_no) values(112,'mobile','blue',1,999,2546585);
insert into products(product_id, product_name, product_color, quality_type, price, model_no) values(785,'bag','Red',1,400,694442);
insert into products(product_id, product_name, product_color, quality_type, price, model_no) values(786,'ipad','Red',1,400,694442);
insert into products(product_id, product_name, product_color, quality_type, price, model_no) values(562,'charger','white',1,39,415415);
insert into products(product_id, product_name, product_color, quality_type, price, model_no) values(222,'T shirt','green',1,100,649795);
insert into products(product_id, product_name, product_color, quality_type, price, model_no) values(8745,'pant','black',1,200,916494);
insert into products(product_id, product_name, product_color, quality_type, price, model_no) values(652,'cap','black',1,20,9411645);

  
  create table  orders (
   order_id int NOT NULL,
   customer_id varchar(10) NOT NULL,
   product_id varchar(10) NOT NULL,
   payment_method varchar(10) NOT NULL,
   delivery_date  date NOT NULL,
   order_date  date NOT NULL,
   total_amount  decimal NOT NULL,
   cart_id  varchar(10) NOT NULL,
  PRIMARY KEY (`order_id`));
  
  insert into orders(order_id,customer_id,product_id,payment_method,delivery_date,order_date,total_amount,cart_id) values(7845854,57896,112,'debit card',01/01/2021,12/26/2020,1000,44);
  insert into orders(order_id,customer_id,product_id,payment_method,delivery_date,order_date,total_amount,cart_id) values(7845855,32529,785,'debit card',01/012/2022,01/19/2022,400,45);
  insert into orders(order_id,customer_id,product_id,payment_method,delivery_date,order_date,total_amount,cart_id) values(7845856,57896,786,'debit card',01/01/2021,12/26/2020,300,46);
  insert into orders(order_id,customer_id,product_id,payment_method,delivery_date,order_date,total_amount,cart_id) values(7845857,57529,562,'debit card',01/01/2021,12/26/2020,100,47);
  insert into orders(order_id,customer_id,product_id,payment_method,delivery_date,order_date,total_amount,cart_id) values(7845858,57896,652,'debit card',01/01/2021,12/26/2020,200,48);
  
   create table shop(
   shop_id varchar(15) NOT NULL,
   shop_name varchar(15) NOT NULL,
   category varchar(15) NOT NULL,
   available  text(10) NOT NULL,
   product_id  varchar(10) NOT NULL,
  PRIMARY KEY (`shop_id`));
  
  insert into shop(shop_id, shop_name, category, available, product_id) values(1012,'maxxy','electronics','yes',112);
  insert into shop(shop_id, shop_name, category, available, product_id) values(1013,'wonderland','bags','yes',785);
  insert into shop(shop_id, shop_name, category, available, product_id) values(1014,'earth','furniture','yes',445);
  insert into shop(shop_id, shop_name, category, available, product_id) values(1015,'luck','watches','yes',530);
  
  create table shopManagement(
    management_id varchar(10) NOT NULL,
    username  varchar(10) NOT NULL,
   passwordd  varchar(15) NULL,
   fullname  varchar(15) NOT NULL,
   shop_id  varchar(10) NOT NULL,
  PRIMARY KEY (`management_id`));
  
  insert into shopManagement(management_id, username, passwordd, fullname, shop_id) values(16,'salmankhan','salman123','salman khan',1012);
  insert into shopManagement(management_id, username, passwordd, fullname, shop_id) values(13,'sharukh','sharukh123','sharukh khan',1013);
  insert into shopManagement(management_id, username, passwordd, fullname, shop_id) values(14,'babyshark','shark123','salman khan',1014);
  insert into shopManagement(management_id, username, passwordd, fullname, shop_id) values(15,'Aeron','Aeron123','Aeron Redd',1015);
  
  
  create table Discounts (
   discount_id varchar(10) NOT NULL,
   offer_startdate  date NOT NULL,
   offer_enddate  date NOT NULL,
   disc  int NOT NULL,
   product_id  varchar(10) NOT NULL,
   shop_id  varchar(15) NOT NULL,
  PRIMARY KEY (`discount_id`));
  
  insert into Discounts(discount_id, offer_startdate, offer_enddate,  disc, product_id, shop_id) values(789,01/10/2022,01/30/2022,20 ,452,1012);
  insert into Discounts(discount_id, offer_startdate, offer_enddate,  disc, product_id, shop_id) values(788,01/10/2022,01/30/2022,30 ,452,1012);
  insert into Discounts(discount_id, offer_startdate, offer_enddate,  disc, product_id, shop_id) values(787,01/10/2022,01/30/2022,50 ,452,1012);
  insert into Discounts(discount_id, offer_startdate, offer_enddate,  disc, product_id, shop_id) values(786,01/10/2022,01/30/2022,10 ,452,1014);
  
  create table login(
  username char(15) NOT NULL,
  login_password varchar(15) NOT NULL,
  mobile int(15),
  mail varchar(25) NOT NULL,
  Customer_id varchar(10) NOT NULL);
  
  insert into login(username, login_password, mobile, mail, customer_id) values('alex12hi','alexking',789658585,'alex@gmail.com',57896);
  insert into login(username, login_password, mobile, mail, customer_id) values('maxykun','maxxy223',789654545,'max@gmail.com',32529);
  
  create table payments(
  payment_id varchar(20) NOT NULL,
  payment_type varchar(25),
  card_no varchar(16) NOT NULL,
  name_on_card char(20) NOT NULL,
  sec_no varchar(3) NOT NULL,
  customer_id varchar(10));
  
  insert into payments(payment_id, payment_type, card_no, name_on_card, sec_no, customer_id) values(123456789,'debit',4456885256544421,'alex peter',235,57896);
  
  create table paymentConfirmations(
  payment_id varchar(20) NOT NULL,
  payment_type varchar(25),
  Bill_no varchar(10) NOT NULL,
  name_on_card char(20) NOT NULL,
  sec_no varchar(5) NOT NULL,
  customer_id varchar(10) NOT NULL
  );
  
  
  
  create table deliverys(
  delivery_id int NOT NULL,
  customer_id varchar(10) NOT NULL,
  customer_name char(10) NOT NULL,
  product_id varchar(15) NOT NULL,
  order_id varchar(10) NOT NULL
  );
  
 select * from customer;

 alter table customer ADD gender varchar(10); 
 
 select * from customer;
 
update customer set customer_fname='vinod',country='USA' where    customer_id='85289';
update customer set customer_fname='Shiva',country='UK' where   customer_id='85287';

select * from customer;

update customer set gender='male' where customer_id='25332';
update customer set gender='male' where customer_id='25338';
update customer set gender='male' where customer_id='32529';
update customer set gender='male' where customer_id='57896';
update customer set gender='male' where customer_id='85287';

select * from customer;

 delete from customer where customer_id='85289';
 delete from customer where customer_id='25332';
 
 select * from customer;
 
Select orders.order_id, customer.customer_fname,customer.customer_lname
From orders
RIGHT JOIN customer
On orders.customer_id = customer.customer_id
ORDER BY orders.order_id;

select * from customer;
Select orders.order_id, customer.customer_fname,customer.customer_lname
From orders
LEFT JOIN customer
On orders.customer_id = customer.customer_id
ORDER BY orders.order_id;

select * from customer where customer_id = '32529';