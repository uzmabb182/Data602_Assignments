-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/a4u9hc
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.

-- Modify this code to update the DB schema diagram.
-- To reset the sample schema, replace everything with
-- two dots ('..' - without quotes).

CREATE TABLE "fips_df" (
    "stcountyfp" int   NOT NULL,
    "countyname" varchar   NOT NULL,
    "zip" int   NOT NULL,
    CONSTRAINT "pk_fips_df" PRIMARY KEY (
        "stcountyfp"
     )
);

CREATE TABLE "modality_df" (
    "countyname" varchar   NOT NULL,
    "stcountyfp" int   NOT NULL,
    "learning_modality" varchar   NOT NULL,
    "operational_schools" int   NOT NULL,
    "state" varchar   NOT NULL,
    "zip_code" int   NOT NULL,
    "year" int   NOT NULL,
    "month" int   NOT NULL,
    "avg_student_count" int   NOT NULL
);

CREATE TABLE "covid_df" (
    "county" varchar   NOT NULL,
    "fips" int   NOT NULL,
    "state" varchar   NOT NULL,
    "year" int   NOT NULL,
    "month" int   NOT NULL,
    "cases_count" int   NOT NULL,
    "deaths_count" int   NOT NULL
);

ALTER TABLE "modality_df" ADD CONSTRAINT "fk_modality_df_stcountyfp" FOREIGN KEY("stcountyfp")
REFERENCES "fips_df" ("stcountyfp");

ALTER TABLE "covid_df" ADD CONSTRAINT "fk_covid_df_fips" FOREIGN KEY("fips")
REFERENCES "fips_df" ("stcountyfp");

