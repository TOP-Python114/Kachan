/*1. Создайте базу данных «Телефонный справочник». Эта база данных должна содержать одну таблицу «Люди». В таблице нужно хранить: ФИО человека, дату рождения, пол, телефон, город проживания, страна проживания, домашний адрес.*/

create database if not exists phonebook;

use phonebook;

create table if not exists `phonebook_table` (
    `id` mediumint unsigned not null auto_increment,
    `Name` varchar(30) not null,
    `Surname` varchar(30) not null,
    -- ИСПОЛЬЗОВАТЬ: в данном случае как раз оптимальнее char, чтобы не хранить лишний байт длины строки
    `Gender` char(1) not null,
    `Date` date not null,
    -- ИСПРАВИТЬ: номер телефона скорее всего тоже записывается строкой фиксированной длины
    `Phone` varchar(20) not null,
    `City` varchar(30),
    `Country` varchar(30),
    `Address` varchar(30),
    constraint `PK_id` primary key (`id`)
);


-- ИТОГ: очень хорошо — 5/6
