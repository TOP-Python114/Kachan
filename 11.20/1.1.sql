/*Задание 1
Создайте базу данных «Телефонный справочник». Эта
база данных должна содержать одну таблицу «Люди». В
таблице нужно хранить: ФИО человека, дату рождения,
пол, телефон, город проживания, страна проживания,
домашний адрес. Для создания базы данных используй-
те запрос CREATE DATABASE. Для создания таблицы
используйте запрос CREATE TABLE.*/

create database if not exists phonebook;
use phonebook;
create table if not exists `phonebook_table` (
	`id` mediumint unsigned not null auto_increment,
    `Name` varchar(30) not null,
    `Surname` varchar(30) not null,
     `Gender` varchar(1) not null,
     `Date` date not null,
     `Phone` varchar(20) not null,
     `City` varchar(30),
     `Country` varchar(30),
     `Adress` varchar(30),
    constraint `PK_id` primary key(`id`)
);