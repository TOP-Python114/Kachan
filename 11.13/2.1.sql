/*1.Вывести все возможные пары строк преподавателей
и групп*/

use academy;

Select
distinct
gr.`name` as group_,
t.`name` as name_teacher,
t.`surname` as name_surname
	from `groupslectures` as gl
    join `groups` as gr on gr.`id` = gl.`groupid`
    join `lectures`as l on gl.`lectureid` = l.`id`
	join `teachers` as t on t.`id` = l.`teacherid`
;

/*2.Вывести названия факультетов, фонд финансирования
кафедр которых превышает фонд финансирования
факультета.*/

select
distinct
f.`name` as name_faculties
	from `departments` as d
	join `faculties` as f on f.`id` = d.`facultyid`
  where d.`financing` > f.`financing`
;

/*3. Вывести фамилии кураторов групп и названия групп,
которые они курируют.*/

select
cur.`surname` as surname_curator,
gr.`name` as name_group
	from `groupscurators` as gc
	join `curators` as cur on cur.`id` = gc.`curatorid`
	join `groups` as gr on gr.`id` = gc.`groupid`
;

/*4. Вывести имена и фамилии преподавателей, которые
читают лекции у группы “P107”. */

Select
distinct
gr.`name` as group_,
t.`name` as name_teacher,
t.`surname` as name_surname
	from `groupslectures` as gl
    join `groups` as gr on gr.`id` = gl.`groupid`
    join `lectures`as l on gl.`lectureid` = l.`id`
	join `teachers` as t on t.`id` = l.`teacherid`
where gr.`name` = 'P107'
;

/*5. Вывести фамилии преподавателей и названия фа-
культетов, на которых они читают лекции. */

Select
distinct
f.`name` as name_facility,
t.`name` as name_teacher,
t.`surname` as name_surname
	from `groupslectures` as gl
    join `groups` as gr on gr.`id` = gl.`groupid`
    join `lectures`as l on gl.`lectureid` = l.`id`
	join `teachers` as t on t.`id` = l.`teacherid`
    join `departments` as d on d.`id` = gr.`departmentid`
	join `faculties` as f on f.`id` = d.`facultyid`
;

/*6. Вывести названия кафедр и названия групп, которые
к ним относятся.*/

Select
distinct
gr.`name` as name_group,
d.`name` as name_department
	from  `groups` as gr
    join `departments` as d on d.`id` = gr.`departmentid`
;

/*7. Вывести названия дисциплин, которые читает пре-
подаватель “Samantha Adams”.*/

Select
distinct
s.`name` as name_subject
	from `lectures` as l
	join `teachers` as t on t.`id` = l.`teacherid`
    join `subjects` as s on s.`id` = l.`subjectid`
where t.`name` = 'Samantha' and t.`surname` = ' Adams'
;

/*8. Вывести названия кафедр, на которых читается дис-
циплина “Database Theory”..*/

Select
distinct
d.`name` as name_department
	from `groupslectures` as gl
    join `groups` as gr on gr.`id` = gl.`groupid`
    join `lectures`as l on gl.`lectureid` = l.`id`
    join `departments` as d on d.`id` = gr.`departmentid`
    join `subjects` as s on s.`id` = l.`subjectid`
where s.`name` = 'Database Theory'
;

/*9. Вывести названия групп, которые относятся к фа-
культету “Computer Science”.*/

Select
distinct
gr.`name` as name_group
	from  `groups` as gr
    join `departments` as d on d.`id` = gr.`departmentid`
	join `faculties` as f on f.`id` = d.`facultyid`
where f.name  = 'Computer Science' 
;

/*10. Вывести названия групп 5-го курса, а также название
факультетов, к которым они относятся */

Select
gr.`name` as name_group,
f.name as name_faculty
	from  `groups` as gr
    join `departments` as d on d.`id` = gr.`departmentid`
	join `faculties` as f on f.`id` = d.`facultyid`
where gr.`year`  = 5
;

/*11. Вывести полные имена преподавателей и лекции,
которые они читают (названия дисциплин и групп),
причем отобрать только те лекции, которые читаются
в аудитории “B103”.*/

Select
distinct
t.`name` as name_teacher,
t.`surname` as name_surname,
s.`name` as name_subject,
gr.`name` as name_group
	from `groupslectures` as gl
    join `groups` as gr on gr.`id` = gl.`groupid`
    join `lectures`as l on gl.`lectureid` = l.`id`
	join `teachers` as t on t.`id` = l.`teacherid`
	join `subjects`as s on l.`subjectid` = s.`id`
where l.`lectureroom` = 'B103'
;