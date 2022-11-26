﻿-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/a4u9hc
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.

-- Modify this code to update the DB schema diagram.
-- To reset the sample schema, replace everything with
-- two dots ('..' - without quotes).

CREATE TABLE "states_df" (
    "States" varchar   NOT NULL,
    "Abbreviation" varchar   NOT NULL
);

CREATE TABLE "modality_df" (
    "learning_modality" varchar   NOT NULL,
    "year" int   NOT NULL,
    "student_count" int   NOT NULL,
    "state" varchar   NOT NULL,
    "population" int   NOT NULL,
    "abbreviation" varchar   NOT NULL,
    "student_count_per_10K" int   NOT NULL
);

CREATE TABLE "covid_df" (
    "cases" int   NOT NULL,
    "deaths" int   NOT NULL,
    "year" int   NOT NULL,
    "state" varchar   NOT NULL,
    "population" int   NOT NULL,
    "abbreviation" varchar   NOT NULL,
    "cases_per_10k" int   NOT NULL,
    "deaths_per_10k" int   NOT NULL
);

