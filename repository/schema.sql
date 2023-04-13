create table students (
    id integer primary key,
    firstName varchar not null,
    lastName varchar not null,
    middleName varchar,

    formEducation varchar not null,
    course integer not null,

    directionEducation varchar not null,
    numberGroup integer not null,

    birthday varchar not null,
    passportID varchar not null,

    login varchar unique not null,
    password varchar not null
);

create table teachers (
    id integer primary key,
    firstName varchar not null,
    lastName varchar not null,
    middleName varchar,

    department varchar not null,
    subject varchar not null,

    birthday varchar not null,
    email varchar not null,

    login varchar unique not null,
    password varchar not null
);

create table ratings (
    id integer primary key,
    studentId integer not null references students (id),

    subject varchar not null,
    topic varchar not null,
    rate_real varchar,
    rate_min varchar not null,
    rate_max varchar not null
);