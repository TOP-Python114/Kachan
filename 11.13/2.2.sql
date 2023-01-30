use academy;


/*1. Вывести количество преподавателей кафедры “Software Development”.*/

select
count(distinct t.`id`) as count_teachers
    from `teachers` as t
    join `lectures`  as l on l.`teacherId` = t.`id`
    join `groupslectures` as gl on gl.`lectureid` = l.`id`
    join `groups` as gr on gr.`id` = gl.`groupid`
    join `departments` as d on d.`id` = gr.`departmentid`
where d.`name` = 'Software Development'
;


/*2. Вывести количество лекций, которые читает преподаватель “Dave McQueen”..*/

select
count(l.`id`) as count_lectures
    from `groupslectures` as gl
    join `lectures`as l on gl.`lectureid` = l.`id`
    join `teachers` as t on t.`id` = l.`teacherid`
where t.`name` = 'Dave' and t.`surname` = 'McQueen'
;


/*3. Вывести количество занятий, проводимых в аудитории “D201”.*/

select
count(l.`id`) as count_lectures
    from `lectures` as l
where l.`lectureroom` = 'D201'
;


/*4. Вывести названия аудиторий и количество лекций, проводимых в них */

select
l.`lectureroom`,
count(l.`id`) as count_lectures
    from `lectures` as l
group by l.`lectureroom`
;


/*5. Вывести количество студентов, посещающих лекции преподавателя “Jack Underhill”.*/

select
count( gs.`studentid`) as count_lectures
    from `groupslectures` as gl
    join `groupsstudents` as gs on gs.`groupid` = gl.`groupid`
    join `lectures`as l on gl.`lectureid` = l.`id`
    join `teachers` as t on t.`id` = l.`teacherid`
where t.`name` = 'Jack' and t.`surname` = 'Underhill'
;


/*6. Вывести среднюю ставку преподавателей факультета “Computer Science”. */

select
avg(t.`salary`) as salary_teacher
    from `groupslectures` as gl
    join `groups` as gr on gr.`id` = gl.`groupid`
    join `lectures`as l on gl.`lectureid` = l.`id`
    join `teachers` as t on t.`id` = l.`teacherid`
    join `departments` as d on d.`id` = gr.`departmentid`
    join `faculties` as f on f.`id` = d.`facultyid`
where f.`name` = 'Computer Science'
;


/*7. Вывести минимальное и максимальное количество студентов среди всех групп.*/

select 
    min(subq.`count_students`) as min_count_students,
    max(subq.`count_students`) as max_count_students
from (
    select
    count(`studentid`) as count_students,
    gs.`groupid`
        from `groupsstudents` as gs
        join `groups` as g on g.`id` = gs.`groupid`
    group by gs.`groupid`
) as subq
;


/*8. Вывести средний фонд финансирования кафедр.*/

select
    round(avg(d.`financing`),0) as avg_financing
from `departments` as d
;


/*9. Вывести полные имена преподавателей и количество читаемых ими дисциплин.*/

select distinct
count(l.`subjectid`) as count_subject,
t.`name` as teacher_name,
t.`surname` as teacher_surname
    from `lectures` as l
    join `teachers` as t on t.`id` = l.`teacherid`
group by t.`name`, t.`surname`
order by 1 desc
;


/*10. Вывести количество лекций в каждый день недели.*/

select 
count(l.`id`) as count_lecture,
dayofweek(`date`) as date_of_week
    from `lectures` as l
group by dayofweek(`date`)
order by dayofweek(`date`)
;


/*11. Вывести номера аудиторий и количество кафедр, чьи лекции в них читаются.*/

select
l.`lectureroom`,
count(distinct d.`id`) as count_departments
    from `groupslectures` as gl
    join `groups` as gr on gr.`id`= gl.`groupid`
    join `lectures`as l on gl.`lectureid` = l.id
    join `departments` as d on d.`id` = gr.`departmentid`
group by l.`lectureroom`
;


/*12. Вывести названия факультетов и количество дисциплин, которые на них читаются.*/

select
f.`name` as faculty_name,
count(distinct l.`subjectid`) as count_subjects
    from `groupslectures` as gl
    join `groups` as gr on gr.`id` = gl.`groupid`
    join `lectures`as l on gl.`lectureid` = l.`id`
    join `departments` as d on d.`id` = gr.`departmentid`
    join `faculties` as f on f.`id` = d.`facultyid`
group by f.`name`
;


/* 13. Вывести количество лекций для каждой пары преподаватель-аудитория.*/

select
l.`lectureroom`,
t.`name` as teacher_name,
t.`surname` as teacher_surname,
count(l.`id`) as count_lecture
    from `groupslectures` as gl
    join `groups` as gr on gr.`id` = gl.`groupid`
    join `lectures`as l on gl.`lectureid` = l.`id`
    join `departments` as d on d.`id` = gr.`departmentid`
    join `teachers` as t on t.`id` = l.`teacherid`
group by l.`lectureroom`, t.`name`, t.`surname`
;
