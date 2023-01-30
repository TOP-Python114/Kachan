use academy;


/*1. Вывести номера корпусов, если суммарный фонд финансирования расположенных в них кафедр превышает 100000.*/

select distinct
d.`building`
    from `departments` as d
    join (
        select
        d.`building`,
        f.`name`,
        sum(f.`financing`) as count_financing
            from `departments` as d
            join `faculties` as f on f.`id` = d.`facultyid`
        group by f.`name`
    -- КОММЕНТАРИЙ: подзапросам лучше всегда давать выделяющиеся псевдонимы, чтобы не путать с псевдонимами обычных таблиц
    ) as subq
    on subq.`building` = d.`building` and `count_financing` > 100000
;


/*2. Вывести названия групп 5-го курса кафедры “Software Development”, которые имеют более 10 пар в первую неделю.*/

select distinct
gr.`name` as name_group,
count(l.`id`) as count_lecture
    from  `groups` as gr
    join `departments` as d on d.`id` = gr.`departmentid`
    join `groupslectures` as gl on gr.`id` = gl.`groupid`
    join `lectures` as l on l.`id` = gl.`lectureid`
where d.name  = 'Software Development'
    and gr.`year` = 5
    and l.`date` between '2022-04-01' and '2022-04-07'
group by gr.`name`
having `count_lecture` > 3
;


/*3. Вывести названия групп, имеющих рейтинг (средний рейтинг всех студентов группы) больше, чем рейтинг группы “D221”.*/

with `rating` as (
    select
    avg(s.`rating`) as avg_raiting,
    gr.`name`
        from `groupsstudents` as gs
        join `groups` as gr on gr.`id` = gs.`groupid`
        join `students` as s on s.`id` = gs.`studentid`
    group by gr.`name`
)
select
`name`,
`avg_raiting`
    from `rating`
where `avg_raiting` > (
    select
    `avg_raiting`
        from `rating`
    where `name`= 'D221'
);


/*4. Вывести фамилии и имена преподавателей, ставка которых выше средней ставки профессоров.*/

with `teachers_salary` as (
    select
    t.`surname`,
    t.`name`,
    t.`salary`,
    t.`isprofessor`
        from `teachers` as t
)
select
`name`,
`surname`
    from `teachers_salary`
where `salary` > (
    select
    avg(`salary`)
        from `teachers_salary`
    where `isprofessor` = 1
);


/*5. Вывести названия групп, у которых больше одного куратора.*/

select
gr.`name`,
count(`curatorid`) as count_curators
    from `groupscurators` as gc
    join `groups` as gr on gr.`id` = gc.`groupid`
group by gr.`name`
having `count_curators` > 1
;


/*6. Вывести названия групп, имеющих рейтинг (средний рейтинг всех студентов группы) меньше, чем минимальный рейтинг групп 5-го курса.*/

with `rating` as (
    select
    avg(s.`rating`) as avg_raiting,
    gr.`year`,
    gr.`name`
        from `groupsstudents` as gs
        join `groups` as gr on gr.`id` = gs.`groupid`
        join `students` as s on s.`id` = gs.`studentid`
    group by gr.`name`, gr.`year`
)
select
`name`,
`avg_raiting`
    from `rating`
where `avg_raiting` < (
    select
    min(`avg_raiting`)
        from `rating`
    where `year` = 5
);


/*7. Вывести названия факультетов, суммарный фонд финансирования кафедр которых больше суммарного фонда финансирования кафедр факультета “Computer Science”.*/

with sum_financing as (
    select
    f.`name` as name_faculties,
    sum(d.`financing`) as count_financing
        from `departments` as d
        join `faculties` as f on f.`id` = d.`facultyid`
    group by f.`name`
)
select
`name_faculties`
    from `sum_financing`
where `count_financing` > (
    select
    `count_financing`
       from `sum_financing`
    where `name_faculties` = 'Computer Science'
);


/*8. Вывести названия дисциплин и полные имена преподавателей, читающих наибольшее количество лекций по ним.*/

with data as (
    select
    t.`name` as name_teacher,
    t.`surname` as name_surname,
    s.`name` as name_subject,
    count(l.`id`) as count_lectures
        from `subjects` as s
        join `lectures` as l on s.`id` = l.`subjectid`
        join `teachers` as t on t.`id` = l.`teacherid`
    group by t.`name`, t.`surname`, s.`name`
)
select
d.`name_teacher`,
d.`name_surname`,
d.`name_subject`
    from data as d
    join (
        select
        max(`count_lectures`) as max_lectures,
        `name_subject`
            from data
        group by `name_subject`
    ) as dm
    on dm.`max_lectures` = d.`count_lectures`
    and dm.`name_subject` = d.`name_subject`
;


/*9. Вывести название дисциплины, по которому читается меньше всего лекций.*/

with data as (
    select
    s.`name` as name_subject,
    count(l.`id`) as count_lectures
        from `subjects` as s
        join `lectures` as l on s.`id` = l.`subjectid`
    group by s.`name`
)
select
d.`name_subject`
    from data as d
    join (
        select
        min(`count_lectures`) as min_lectures,
        `name_subject`
            from data
        group by `name_subject`
    ) as dm
    on dm.`min_lectures` = d.`count_lectures`
    and dm.`name_subject` = d.`name_subject`
;


/*10. Вывести количество студентов и читаемых дисциплин на кафедре “Software Development”.*/

select 
count(distinct `subjectid`) as count_subjects,
count(distinct `studentid`) as count_students
    from `groupsstudents` as gs
    join `groups` as g on g.`id` = gs.`groupid`
    join `departments` as d on d.`id` = g.`departmentid`
    join `groupslectures` as gl on g.`id` = gl.`groupid`
    join `lectures` as l on l.`id` = gl.`lectureid`
where d.`name` = 'Software Development'
;


-- ИТОГ: отлично — 12/12