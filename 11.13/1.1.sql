use academy;


insert into `curators`
    (`name`, `surname`)
values
    ('Иван', 'Паровозов'),
    ('Григорий', 'Иванов'),
    ('Сергей', 'Усов'),
    ('Ольга', 'Гвоздикова'),
    ('Петр', 'Толстов'),
    ('Анна', 'Макарова'),
    ('Антон', 'Сидоров'),
    ('Константин', 'Лунев'),
    ('Алексей', 'Петров'),
    ('Агата', 'Сидорова'),
    ('Игнат', 'Самсонов'),
    ('Константин', 'Агапов'),
    ('Алексей', 'Некрасов'),
    ('Сабина', 'Юсупова'),
    ('Артемий', 'Троицкий'),
    ('Федор', 'Долгополов'),
    ('Александр', 'Маринин'),
    ('Константин', 'Крюков'),
    ('Иван', 'Чемезов'),
    ('Аркадий', 'Чемендряков'),
    ('Александр', 'Баранов'),
    ('Антон', 'Чесментский'),
    ('Петр', 'Маршалов'),
    ('Ирина', 'Лепова'),
    ('Эльвира', 'Лапова'),
    ('Мария', 'Бекаева'),
    ('Ольга', 'Дроздова'),
    ('Татьяна', 'Бельская'),
    ('Дарья', 'Павлихина'),
    ('Люсьена', 'Овечкина');
            
insert into `departments`
    (`building`, `financing`, `name`, `facultyid`)
values
    (1, 200000, 'Кафедра агроэкономики', 7),
    (1, 200000, 'Кафедра иностранных языков', 8),
    (1, 200000, 'Software Development', 1),
    (1, 200000, 'Кафедра конкурентной и промышленной политики', 7),
    (1, 200000, 'Кафедра макроэкономической политики и стратегического управления', 7),
    (1, 200000, 'Кафедра маркетинга', 2),
    (1, 300000, 'Кафедра математических методов анализа экономики', 6),
    (1, 300000, 'Кафедра мировой экономики', 3),
    (1, 300000, 'Кафедра народонаселения', 7),
    (1, 300000, 'Кафедра политической экономии', 10),
    (2, 300000, 'Кафедра прикладной институциональной экономики', 10),
    (2, 300000, 'Кафедра статистики', 4),
    (2, 200000, 'Кафедра управления организацией', 10),
    (2, 200000, 'Кафедра управления рисками и страхования', 10),
    (2, 500000, 'Кафедра учета, анализа и аудита', 10),
    (2, 500000, 'Кафедра философии и методологии экономики', 5),
    (2, 500000, 'Кафедра финансов и кредита', 10),
    (2, 1000000, 'Кафедра экономики для естественных и гуманитарных факультетов', 9),
    (2, 500000, 'Кафедра экономики инноваций', 10),
    (2, 500000, 'Кафедра экономики природопользования', 9),
    (2, 500000, 'Кафедра экономики труда и персонала', 10),
    (2, 1000000, 'Кафедра экономической информатики', 10);
                
insert into `faculties`
    (`financing`, `name`)
values
    ('1000000', 'Исторический факультет'),
    ('1000000', 'Факультет маркетинга'),
    ('1000000', 'Факультет мировой экономики'),
    ('1000000', 'Факультет статистики'),
    ('1000000', 'Филологический факультет'),
    ('1000000', 'Математический факультет'),
    ('2000000', 'Факультет сельского хозяйства'),
    ('2000000', 'Факультет иностранных языков'),
    ('2000000', 'Факультет естественных наук'),
    ('3000000', 'Computer Science');
  
insert into `groups`
    (`name`, `year`, `departmentid`)
values
    ('ИН-22', 1, 2),
    ('ИН-21', 2, 2),
    ('ИН-20', 3, 2),
    ('ИН-19', 4, 2),
    ('ИН-18', 5, 2),
    ('P107', 1, 19),
    ('ЭИ-21', 2, 19),
    ('ЭИ-20', 3, 19),
    ('ЭИ-19', 4, 19),
    ('ЭИ-18', 5, 19),
    ('МЭ-22', 1, 3),
    ('МЭ-21', 2, 3),
    ('МЭ-20', 3, 3),
    ('МЭ-19', 4, 3),
    ('МЭ-18', 5, 3),
    ('ПЭ-22', 1, 10),
    ('ПЭ-21', 2, 10),
    ('ПЭ-20', 3, 10),
    ('ПЭ-19', 4, 10),
    ('ПЭ-18', 5, 10),
    ('НХ-22', 1, 1),
    ('НХ-21', 2, 1),
    ('НХ-20', 3, 1),
    ('НХ-19', 4, 1),
    ('НХ-18', 5, 1),
    ('УА-22', 1, 10),
    ('УА-21', 2, 10),
    ('УА-20', 3, 10),
    ('УА-19', 4, 10),
    ('УА-18', 5, 10);
                
insert into `groupscurators`
    (`curatorid`, `groupid`)
values
    (23, 23),
    (24, 24),
    (25, 25),
    (26, 26),
    (27, 27),
    (28, 28),
    (29, 29),
    (30, 30),
    (14, 14),
    (15, 15),
    (16, 16),
    (17, 17),
    (18, 18),
    (19, 19),
    (20, 20),
    (21, 21),
    (22, 22),
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
    (9, 9),
    (10, 10),
    (11, 11),
    (12, 12),
    (13, 13);
  
insert into `groupslectures`
    (`groupid`, `lectureid`)
values
    (1, 30),
    (2, 1),
    (3, 5),
    (4, 8),
    (5, 9),
    (6, 11),
    (7, 30),
    (8, 28),
    (9, 22),
    (10, 21),
    (11, 8),
    (12, 9),
    (1, 5),
    (3, 4),
    (12, 6),
    (4, 4),
    (8, 7),
    (1, 8),
    (12, 9),
    (14, 1),
    (18, 2),
    (10, 3),
    (12, 5),
    (3, 15),
    (4, 22),
    (5, 23),
    (7, 31),
    (7, 27),
    (1, 6),
    (4, 16);

insert into `groupslectures`
    (`groupid`, `lectureid`)
values
    (1, 30),
    (2, 1),
    (3, 5),
    (4, 8),
    (5, 9),
    (6, 11),
    (7, 30),
    (8, 28),
    (9, 22),
    (10, 21),
    (11, 8),
    (12, 9),
    (1, 5),
    (3, 4),
    (12, 6),
    (4, 4),
    (8, 7),
    (1, 8),
    (12, 9),
    (14, 1),
    (18, 2),
    (10, 3),
    (12, 5),
    (3, 15),
    (4, 22),
    (5, 23),
    (7, 31),
    (7, 27),
    (1, 6),
    (4, 16);

insert into `lectures`
    (`date`, `lectureroom`, `subjectid`, `teacherid`)
values
    ('01.04.2022', 'D201', 20, 1),
    ('01.04.2022', 'B100', 21, 1),
    ('01.04.2022', 'B101', 22, 10),
    ('01.05.2022', 'B102', 23, 14),
    ('01.05.2022', 'B103', 24, 2),
    ('01.05.2022', 'B104', 25, 3),
    ('01.06.2022', 'D221', 26, 4),
    ('01.06.2022', 'D221', 27, 2),
    ('01.07.2022', 'D221', 28, 2),
    ('01.07.2022', 'B108', 29, 6),
    ('01.07.2022', 'B109', 30, 6),
    ('01.08.2022', 'B110', 1, 5),
    ('01.08.2022', 'B111', 2, 5),
    ('01.09.2022', 'B112', 3, 7),
    ('01.09.2022', 'B113', 4, 9),
    ('01.10.2022', 'B114', 5, 4),
    ('01.10.2022', 'B115', 6, 1),
    ('01.03.2022', 'B116', 7, 13),
    ('01.03.2022', 'B117', 8, 10),
    ('01.03.2022', 'D201', 9, 7),
    ('01.02.2022', 'B119', 10, 4),
    ('01.02.2022', 'D221', 11, 5),
    ('01.02.2022', 'B121', 12, 6),
    ('01.03.2022', 'B122', 13, 3),
    ('01.04.2022', 'B123', 14, 4),
    ('01.05.2022', 'B124', 15, 5),
    ('01.09.2022', 'B125', 16, 11),
    ('01.07.2022', 'B126', 31, 12),
    ('01.07.2022', 'B127', 18, 13),
    ('01.08.2022', 'D201', 19, 1);

insert into `subjects`
    (`name`)
values
    ('Русский язык'),
    ('История'),
    ('Иностранный язык'),
    ('Экономическая теория'),
    ('Социология'),
    ('Философия'),
    ('Экология'),
    ('Психология'),
    ('Охрана труда'),
    ('Физическая культура'),
    ('Введение в экономику'),
    ('Микроэкономика'),
    ('Статистика'),
    ('Бухгалтерский учет'),
    ('Маркетинг'),
    ('Менеджмент'),
    ('Финансы и фондовый рынок'),
    ('Банки и банковская деятельность'),
    ('Управление рисками и страхование'),
    ('Аудит'),
    ('Макроэкономика'),
    ('Радиотехника'),
    ('Инфокоммуникационные технологии и системы связи'),
    ('Конструирование и технология электронных средств'),
    ('Электроника и наноэлектроника'),
    ('Приборостроение'),
    ('Оптотехника'),
    ('Фотоника и оптоинформатика'),
    ('Биотехнические системы и технологии'),
    ('Лазерная техника и лазерные технологии'),
    ('Database Theory');

insert into `teachers`
    (`name`, `isprofessor`, `surname`, `salary`)
values
    ('Samantha', 0, ' Adams', 60000),
    ('Jack', 0, 'Underhill', 50000),
    ('Екатерина', 0, 'Сопельцева', 70000),
    ('Анастасия', 0, 'Близнюк', 30000),
    ('Татьяна', 1, 'Солнцева', 100000),
    ('Виктория', 0, 'Сонина', 50000),
    ('Dave', 0, 'McQueen', 50000),
    ('Оксана', 0, 'Ушакова', 50000),
    ('Карина', 0, 'Макеева', 50000),
    ('Юлия', 0, 'Судакова', 50000),
    ('Ольга', 1, 'Спивак', 100000),
    ('Наталия', 0, 'Орлова', 70000),
    ('Леонид', 0, 'Воронин', 70000),
    ('Ольга', 0, 'Путинцева', 60000);
                
insert into `students`
    (`name`, `rating`, `surname`)
values
    ('Екатерина', 0, 'Александрова'),
    ('Денис', 1, 'Котов'),
    ('Александр', 2, 'Ильин'),
    ('Филипп', 3, 'Павлов'),
    ('Егор', 4, 'Васильев'),
    ('Жанна', 5, 'Журавлева'),
    ('Татьяна', 5, 'Кева'),
    ('Антон', 1, 'Новоселов'),
    ('Артем', 2, 'Барышев'),
    ('Антон', 3, 'Медведев'),
    ('Михаил', 0, 'Стремоусов'),
    ('Алексей', 5, 'Дементьев'),
    ('Алексей', 4, 'Челпанов'),
    ('Никита', 1, 'Кочуров'),
    ('Александр', 0, 'Вершинин'),
    ('Антон', 2, 'Заельцов'),
    ('Семен', 3, 'Макаров'),
    ('Константин', 1, 'Паршаков'),
    ('Анатолий', 2, 'Ефаров'),
    ('Кирилл', 3, 'Шишкин'),
    ('Артем', 4, 'Нефедя'),
    ('Максим', 2, 'Ухов'),
    ('Сергей', 3, 'Петров'),
    ('Александр', 1, 'Игнатьев'),
    ('София', 0, 'Морозова'),
    ('Кристина', 4, 'Муравьева'),
    ('Елена', 2, 'Абрикосова'),
    ('Анна', 3, 'Кузнецова'),
    ('Павел', 5, 'Потапов'),
    ('Любовь', 0, 'Мороз');

insert into `groupstudent`
    (`groupid`, `studentid`)
values
    (1, 22),
    (2, 23),
    (5, 24),
    (7, 25),
    (8, 26),
    (9, 27),
    (19, 28),
    (6, 29),
    (16, 1),
    (3, 2),
    (4, 3),
    (5, 4),
    (28, 5),
    (28, 6),
    (1, 7),
    (1, 8),
    (4, 9),
    (5, 10),
    (4, 11),
    (4, 12),
    (5, 13),
    (6, 14),
    (7, 15),
    (8, 16),
    (9, 17),
    (6, 18),
    (10, 19),
    (1, 20),
    (2, 21);

-- КОММЕНТАРИЙ: в MySQL Workbench и MySQL Shell по умолчанию включен autocommit
commit;


-- ИТОГ: отлично — 6/6
