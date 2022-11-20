﻿-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/a4u9hc
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.

-- Modify this code to update the DB schema diagram.
-- To reset the sample schema, replace everything with
-- two dots ('..' - without quotes).

CREATE TABLE "fips" (
    "countyname" varchar   NOT NULL,
    "fips" int   NOT NULL
);

CREATE TABLE "modality" (
    "countyname" varchar   NOT NULL,
    "fips" int   NOT NULL,
    "learning_modality" varchar   NOT NULL,
    "state" varchar   NOT NULL,
    "year" int   NOT NULL,
    "avg_student_count" int   NOT NULL
);

CREATE TABLE "covid" (
    "countyname" varchar   NOT NULL,
    "fips" int   NOT NULL,
    "state" varchar   NOT NULL,
    "year" int   NOT NULL,
    "cases_count" int   NOT NULL,
    "deaths_count" int   NOT NULL
);


SELECT * FROM "fips";

SELECT * FROM "covid";

SELECT * FROM "modality";