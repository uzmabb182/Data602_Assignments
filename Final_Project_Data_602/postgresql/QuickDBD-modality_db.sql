-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/a4u9hc
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.

-- Modify this code to update the DB schema diagram.
-- To reset the sample schema, replace everything with
-- two dots ('..' - without quotes).

CREATE TABLE "states" (
    "States" varchar   NOT NULL,
    "Abbreviation" varchar   NOT NULL
);

CREATE TABLE "modality" (
    "learning_modality" varchar   NOT NULL,
    "year" int   NOT NULL,
    "state" varchar   NOT NULL,
    "student_count" int   NOT NULL
);

CREATE TABLE "covid" (
    "state" varchar   NOT NULL,
    "cases" int   NOT NULL,
    "deaths" int   NOT NULL,
    "year" int   NOT NULL
);


SELECT * 
FROM states;

SELECT * 
FROM covid;

SELECT * 
FROM modality;