create table students (
    id integer primary key,
    firstName varchar not null,
    lastName varchar not null,
    middleName varchar,

    formEducation varchar not null,
    course integer not null,

    directionEducation varchar not null,
    numberGroup integer not null,

    birthday date,
    passportID varchar not null,

    login varchar unique not null,
    password varchar not null
);
