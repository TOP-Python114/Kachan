/*3. Создайте базу данных «Музыкальная коллекция». База данных должна содержать информацию о музыкальных дисках, исполнителях, стилях. Необходимо хранить следующую информацию:
 - о музыкальном диске: название диска, исполнитель, дата выпуска, стиль, издатель;
 - о стилях: названия стилей;
 - об исполнителях: название;
 - об издателях: название, страна;
 - о песнях: название песни, название диска, длительность песни, музыкальный стиль песни, исполнитель.*/

create database if not exists music;

use music;

create table if not exists `Disks` (
    `Id` mediumint unsigned not null auto_increment,
    `Name` varchar(30) not null,
    `ArtistId` mediumint unsigned not null,
    `PublisherId` mediumint unsigned not null,
    `GenreId` mediumint unsigned not null,
    -- ИСПРАВИТЬ: not null обязателен — каждый диск совершенно определённо выпущен в какую-то дату (хотя для музыкальных альбомов обычно ограничиваются указанием года выпуска), таким образом дата является неотъемлемым атрибутом
    `Date` date,
    constraint `PK_id` primary key (`Id`),
    constraint `CH_Disks_Name` check (`Name` <> '')
);

create table if not exists `Songs` (
    `Id` mediumint unsigned not null auto_increment,
    `Name` varchar(30) not null,
    `DiskId` mediumint unsigned not null,
    `ArtistId` mediumint unsigned not null,
    -- ИСПРАВИТЬ: для хранения отрезков времени есть тип time: https://dev.mysql.com/doc/refman/8.0/en/time.html
    -- ИСПРАВИТЬ: not null обязателен — трека без длительности не должно существовать, это неотъемлемый атрибут
    `Duration` smallint,
    `GenreId` mediumint unsigned not null,
    constraint `PK_id` primary key (`Id`),
    constraint `CH_Songs_Name` check (`Name` <> '')
    -- ДОБАВИТЬ: ограничение `длительность` > 0
);

create table if not exists `Genres` (
    `Id` mediumint unsigned not null auto_increment,
    `Name` varchar(30) not null,
    constraint `PK_id` primary key (`Id`),
    constraint `CH_Genres_Name` check (`Name` <> '')
);

create table if not exists `Artists` (
    `Id` mediumint unsigned not null auto_increment,
    `Name` varchar(30) not null,
    constraint `PK_id` primary key (`Id`),
    constraint `CH_Artists_Name` check (`Name` <> '')
);

create table if not exists `Publishers` (
    `Id` mediumint unsigned not null auto_increment,
    `Name` varchar(30) not null,
    -- ИСПРАВИТЬ: not null обязателен — полагаю, любой издатель существует в определённой юрисдикции, а значит и в стране
    `Country` varchar(30),
    constraint `PK_id` primary key (`Id`),
    constraint `CH_Publishers_Name` check (`Name` <> '')
    -- ДОБАВИТЬ: ограничение `страна` <> ''
);

alter table `Disks` 
    add constraint `FK_Disks_ArtistId`
        foreign key (`ArtistId`)
        references `Artists` (`Id`),
    add constraint `FK_Disks_PublisherId`
        foreign key (`PublisherId`)
        references `Publishers` (`Id`),
    add constraint `FK_Disks_GenreId`
        foreign key (`GenreId`) 
        references `Genres` (`Id`);

alter table `Songs` 
    add constraint `FK_Songs_ArtistId`
        foreign key (`ArtistId`)
        references `Artists` (`Id`),
    add constraint `FK_Songs_DiskId` 
        foreign key (`DiskId`)
        references `Disks` (`Id`),
    add constraint `FK_Songs_GenreId`
        foreign key (`GenreId`)
        references `Genres` (`Id`);


-- ИТОГ: очень хорошо — 10/12
