create table formEducation (
    id integer primary key,
    title varchar not null
);
create table groups (
    id integer primary key,
    title varchar not null
);

create table students (
    id integer primary key,
    firstName varchar not null,
    lastName varchar not null,
    middleName varchar,
    birthday date,

    numberGroup integer not null,
    groupID integer not null references groups (id),

    course integer not null,
    formEducationID integer not null references formEducation (id),

    login varchar unique not null,
    password varchar not null
);

insert into formEducation (title) values ('Бакалавриат');
insert into formEducation (title) values ('Магистратура');
insert into formEducation (title) values ('Специалитет');

insert into groups (title) values ('ПМИ');
insert into groups (title) values ('ФИТ');
insert into groups (title) values ('ИТХ');
insert into groups (title) values ('ИТС');
insert into groups (title) values ('КМБ');
insert into groups (title) values ('МММ');
