# Backend SQL Scripts Overview

## EDA.sql
- Overview of the data model.
- Creates temporary tables for data analysis.
- Retrieves viewing data, combining information from different sources.
- Aggregates data by Enhetstyp to summarize total views.

## marts_content.sql
- Establishes the marts schema and creates tables for viewing data.
- Aggregates view counts by date and formats them for analysis.
- Retrieves metadata about the marts schema and checks existing tables.

## marts_device.sql
- Aggregates device views by date and type, creating summaries for analysis.
- Creates a summary table with essential metrics about device usage.
- Checks and retrieves data from the newly created tables.
