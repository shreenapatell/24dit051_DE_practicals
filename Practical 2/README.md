# Automated Data Quality Validation

## Objective
This project demonstrates automated source data profiling, validation, and ingestion of structured, semi-structured, and unstructured data before loading into a target database.

## Tools Used
- Python 3.x
- Pandas
- Faker
- SQLite
- Logging

## Validation Strategies
- Automatic schema discovery
- Missing value detection
- Data type validation
- Primary key validation
- Quarantine of invalid records
- Execution logging

## Malformed Input Handling
- Missing emails are detected and quarantined.
- Missing age values are identified during validation.
- Invalid records are stored separately in quarantine.csv.
- Clean records are stored in SQLite.
- Validation events are written to quality_log.txt.

## Generated Files
- customers.csv
- api_transactions.json
- config.txt
- clean_customers.csv
- quarantine.csv
- quarantine_primarykey.csv
- validated.csv
- customer.db
- quality_log.txt

## Conclusion
The project successfully profiles incoming data, validates quality, quarantines invalid records, stores clean data in SQLite, and generates execution logs for auditing and monitoring.