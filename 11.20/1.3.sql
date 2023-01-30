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
    `Date` date,
    constraint `PK_id` primary key (`Id`),
    constraint `CH_Disks_Name` check (`Name` <> '')
);

create table if not exists `Songs` (
    `Id` mediumint unsigned not null auto_increment,
    `Name` varchar(30) not null,
    `DiskId` mediumint unsigned not null,
    `ArtistId` mediumint unsigned not null,
    `Duration` smallint,
    `GenreId` mediumint unsigned not null,
    constraint `PK_id` primary key (`Id`),
    constraint `CH_Songs_Name` check (`Name` <> '')
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
    `Country` varchar(30),
    constraint `PK_id` primary key (`Id`),
    constraint `CH_Publishers_Name` check (`Name` <> '')
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
