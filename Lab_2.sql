CREATE DATABASE if not exists Lab_2;
USE Lab_2;
create table if not exists Student(

	primary key(ID),
	ID char(10) not null,
	S_Name varchar(20),
	Gender varchar(10),
	age int,
	school_year int,
	class int
);

insert into Student values('0000000001', 'Tony', 'Male', 20, 2016, 1);
insert into Student values('0000000002', 'Tom', 'Male', 19, 2017, 2);
insert into Student values('0000000003', 'Jane', 'Female', 20, 2016, 3);
insert into Student values('0000000004', 'Nick', 'Male', 20, 2015, 4);
insert into Student values('0000000005', 'Mike', 'Male', 19, 2017, 3);
insert into Student values('0000000006', 'Sam', 'Male', 20, 2015, 4);
insert into Student values('0000000007', 'Marry', 'Female', 19, 2016, 5);
insert into Student values('0000000008', 'Pat', 'Female', 20, 2015, 6);
insert into Student values('0000000009', 'Shurjo', 'Male', 21, 2016, 6);
insert into Student values('0000000010', 'Vital', 'Male', 20, 2015, 6);
insert into Student values('0000000011', 'Trump', 'Male', 18, 2017, 7);
insert into Student values('0000000012', 'Melania', 'Female', 20, 2015, 7);
insert into Student values('0000000013', 'Pompeo', 'Male', 20, 2015, 8);
insert into Student values('0000000014', 'Matisse', 'Male', 19, 2016, 8);
insert into Student values('0000000015', 'Bush', 'Male', 19, 2016, 9);

create table if not exists Class(

	primary key(ID),
	ID char(7) not null,
	C_Name varchar(20),
	Teacher_ID char(5),
	Credit int,
	Suitable_Grade int,
	Cancel_Year int
);

insert into Class values('0000001', 'Chinese', '00001', 1, 2016, 2020);
insert into Class values('0000002', 'Math', '00002', 2, 2017, 2020);
insert into Class values('0000003', 'English', '00003', 1, 2016, 2020);
insert into Class values('0000004', 'Database', '00004', 2, 2016, 2020);
insert into Class values('0000005', 'CPP', '00005', 2, 2016, 2020);
insert into Class values('0000006', 'AI', '00006', 1, 2016, 2020);
insert into Class values('0000007', 'Algorithm', '00007', 2, 2016, 2020);

create table if not exists Teacher(

	primary key(ID),
	ID char(5) not null,
	T_Name varchar(20),
	Course varchar(20),
    Administrator int
);

insert into Teacher values('00001', 'Professor_Chan', 'Chinese', 1);
insert into Teacher values('00002', 'Professor_Yu', 'Database', 1);
insert into Teacher values('00003', 'Professor_Liu', 'Math', 2);
insert into Teacher values('00004', 'Professor_Xu', 'English', 1);
insert into Teacher values('00005', 'Professor_Zheng', 'CPP', 1);
insert into Teacher values('00006', 'Professor_Ng', 'AI', 2);
insert into Teacher values('00007', 'Professor_Yan', 'Algorithm', 1);


create table if not exists Choose(
	
	Student_ID char(10) not null,
	Course_ID char(7) not null,
	Teacher_ID char(5) not null,
	Choose_Year int,
	Grade int,
	foreign key(Student_ID) references Student(ID),
	foreign key(Course_ID) references Class(ID),
	foreign key(Teacher_ID) references Teacher(ID)
);

insert into Choose values('0000000001', '0000001', '00001', 2016, 95);
insert into Choose values('0000000002', '0000002', '00002', 2017, 92);
insert into Choose values('0000000003', '0000003', '00003', 2016, 95);
insert into Choose values('0000000004', '0000004', '00004', 2016, 89);
insert into Choose values('0000000005', '0000002', '00002', 2016, 87);
insert into Choose values('0000000006', '0000004', '00004', 2016, 94);
insert into Choose values('0000000007', '0000001', '00001', 2015, 67);
insert into Choose values('0000000008', '0000005', '00005', 2016, 95);
insert into Choose values('0000000009', '0000005', '00005', 2015, 78);
insert into Choose values('0000000010', '0000002', '00002', 2016, 67);
insert into Choose values('0000000011', '0000005', '00005', 2016, 59);
insert into Choose values('0000000012', '0000006', '00006', 2016, 86);
insert into Choose values('0000000013', '0000006', '00006', 2016, 87);
insert into Choose values('0000000014', '0000007', '00007', 2016, 95);
insert into Choose values('0000000015', '0000007', '00007', 2016, 92);





#No.1
update Student set age ="20"
where ID = "0000000001";



#No.2
#delete from Student where ID = 'XXXX';
#delete from Class where ID = 'XXXX';
#delete from Choose where (Student_ID = 'XXXXX' and Course_ID = 'XXXXX') or Student_ID = 'XXXXX' or Course_ID = 'XXXXX';

#No.3
select S.ID, S.	S_Name, S.Gender, S.age, S.school_year, S.class, Ch.Grade, Ch.Course_ID
from Student as S, Choose as Ch
where S.ID = Ch.Student_ID and 
	(S.S_Name = "Tony" or S.ID = "0000000001");

#No.4
select Ch.Grade
from Student as S, Choose as Ch, Class as Cl
where (S.S_Name = "XXXX" or 
		(S.ID = "XXXXXXXX" and Cl.C_Name) or
		Ch.Course_ID = "XXXXX") and
		S.ID = Ch.Student_ID and 
		Ch.Teacher_ID = Cl.Teacher_ID;

# No.5
select Cl.ID, Cl.C_Name, Cl.Teacher_ID, Te.T_Name, Cl.Credit, Cl.Suitable_Grade, Cl.Cancel_Year,Ch.Student_ID, St.S_Name, Ch.Choose_Year, Ch.Grade
from Class as Cl, Choose as Ch, Teacher as Te, Student as St
where (Cl.C_Name = "Chinese" or Cl.ID = "0000001") and (Cl.Teacher_ID=Te.ID) and (Ch.Student_ID=St.ID) and
		Cl.ID = Ch.Course_ID;

#No. 6
select *
from Teacher as T, Choose as Ch
where T.ID = Ch.Teacher_ID and 
		(T.T_Name = "XXXXXX" or T.ID = "XXXXX") ;
	
#No. 7.1 Average grade for one student
select avg(Ch.Grade)
from Choose as Ch
where Ch.Student_ID = "XXXXX";

#No. 7.2 Average grade for all students
select avg(Ch.Grade)
from Choose as Ch;

#No. 7.3 Average grade for a class
select avg(Ch.Grade)
from Choose as Ch, Student as S
where Ch.Student_ID = S.ID and
		S.class = "X";
        
select avg(Ch.Grade)
from Choose as CH
where Ch.Course_ID = "XXXXXX";
		
