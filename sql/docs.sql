create table doctors
(
id number  primary key,
name varchar2(50) not null,
speciality varchar2(100),
hospital varchar2(50),
city varchar2(50),
consultation_fee number
);

insert into doctors values (1, 'Dr. Shashank', 'Ayurveda', 'Apollo Hospital', 'Bangalore', 2500);
insert into doctors values (2, 'Dr. Abdul', 'Homeopathy', 'Fortis Hospital', 'Bangalore', 2000);
insert into doctors values (3, 'Dr. Shwetha', 'Homeopathy', 'KMC Hospital', 'Manipal', 1000);
insert into doctors values (4, 'Dr. Murphy', 'Dermatology', 'KMC Hospital', 'Manipal', 1500);
insert into doctors values (5, 'Dr. Farhana', 'Physician', 'Gleneagles Hospital', 'Bangalore', 700);
insert into doctors values (6, 'Dr. Maryam', 'Physician', 'Gleneagles Hospital', 'Bangalore', 1500);

-- From the doctors table, fetch the details of 
-- doctors who work in the same hospital but in different specialty.


SELECT 
    a.*
FROM
    doctors a
        INNER JOIN
    doctors b ON a.hospital = b.hospital
        AND a.speciality != b.speciality


