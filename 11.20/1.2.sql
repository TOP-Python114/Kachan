/*2. Создайте базу данных «Продажи». База данных должна содержать информацию о продавцах, покупателях, продажах. Необходимо хранить следующую информацию:
 - о продавцах: ФИО, email, контактный телефон;
 - о покупателях: ФИО, email, контактный телефон;
 - о продажах: покупатель, продавец, название товара, цена продажи, дата сделки.*/

create database if not exists sales;

use sales;

create table if not exists `Sellers` (
    `Id` mediumint unsigned not null auto_increment,
    `Name` varchar(30) not null,
    `Surname` varchar(30) not null,
    `Phone` varchar(20) not null,
    `Email` varchar(30),
    constraint `PK_id` primary key (`Id`),
    constraint `CH_Sellers_Name` check (`Name` <> ''),
    constraint `CH_Sellers_Surname` check (`Surname` <> '')
    -- ДОБАВИТЬ: ограничение `телефон` <> '' — если указываете для столбца not null, то это очень часто также подразумевает отсутствие пустого значения
);

create table if not exists `Buyers` (
    `Id` mediumint unsigned not null auto_increment,
    `Name` varchar(30) not null,
    `Surname` varchar(30) not null,
    `Phone` varchar(20) not null,
    `Email` varchar(30),
    constraint `PK_id` primary key (`Id`),
    constraint `CH_Buyers_Name` check (`Name` <> ''),
    constraint `CH_Buyers_Surname` check (`Surname` <> '')
);

create table if not exists `Sale` (
    `Id` mediumint unsigned not null auto_increment,
    `Date` date not null,
    `Name` varchar(30) not null,
    `Price` decimal(8,2) not null,
    `SellerId` mediumint unsigned not null,
    `BuyerId` mediumint unsigned not null,
    constraint `PK_id` primary key (`id`),
    constraint `CH_Sales_Name` check (`Name` <> ''),
    constraint `CH_Sales_Price` check (`Price` > 0)
);

alter table `Sale` 
    add constraint `FK_Sale_SellerId`
        foreign key (`SellerId`)
        references `Sellers` (`Id`),
    add constraint `FK_Sale_BuyerId`
        foreign key (`BuyerId`)
        references `Buyers` (`Id`);


-- ИТОГ: очень хорошо — 7/8
