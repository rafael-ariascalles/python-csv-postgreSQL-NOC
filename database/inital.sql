create database noc_search_engine;

\c noc_search_engine;

create table NOC_GROUP(
    GROUP_CODE varchar PRIMARY KEY, 
    GROUP_TITLE varchar, 
    GROUP_DEFINITION varchar
);

create table NOC_MAJOR(
    MAJOR_CODE varchar PRIMARY KEY, 
    MAJOR_TITLE varchar, 
    MAJOR_DEFINITION varchar
);

create table NOC_MINOR(
    MINOR_CODE varchar PRIMARY KEY, 
    MINOR_TITLE varchar, 
    MINOR_DEFINITION varchar
);

create table NOC_UNIT(
    UNIT_CODE varchar PRIMARY KEY, 
    UNIT_TITLE varchar, 
    UNIT_DEFINITION varchar
);

create table NOC_UNIT_EXAMPLE(
    UNIT_EXAMPLE_ID SERIAL,
    UNIT_CODE varchar, 
    TEXT_DESCRIPTION varchar
);


create table NOC_UNIT_INCLUSION(
    UNIT_INCLUSION_ID SERIAL,
    UNIT_CODE varchar, 
    TEXT_DESCRIPTION varchar
);

create table NOC_UNIT_EXCLUSION(
    UNIT_EXCLUSION_ID SERIAL,
    UNIT_CODE varchar, 
    TEXT_DESCRIPTION varchar
);

create table NOC_UNIT_MAIN_DUTIES(
    UNIT_MAIN_DUTIES_ID SERIAL,
    UNIT_CODE varchar, 
    TEXT_DESCRIPTION varchar
);

create table NOC_UNIT_EMPLOYMENT_REQUIREMENTS(
    UNIT_EMPLOYMENT_REQUIREMENTS SERIAL,
    UNIT_CODE varchar, 
    TEXT_DESCRIPTION varchar
);

create table NOC_UNIT_ADITIONAL_INFORMATION(
    UNIT_ADITIONAL_INFORMATION SERIAL,
    UNIT_CODE varchar, 
    TEXT_DESCRIPTION varchar
);
