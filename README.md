# Maine Power Stations Database

---

## Project Overview
A Python application connecting to a MAMP-hosted SQL database to catalogue and query power generation infrastructure across Maine using official data from the U.S. Energy Information Administration (EIA).
Made for SIE 557 University of Maine, Spring 2026

## Repository Contents & Structure

* **Main Application & Modules:**
  * `Maine Power Stations Database.py` (Main program script)
  * **Modules Folder:** Contains the three required modules:
    * `db_config_file2.py`
    * `db_build_SQL_query2.py`
    * `db_build_SQL_insert2.py`

* **Visual Assets:**
  * `colorcounties2.png`: Used in the second tab of the application (located in the main folder).
  * `SIE557_FP_ERDiagram_Marshall.Gregg.png`: ER Diagram explaining the relationships between the database tables.

* **Data and Exports Folder:**
  * **Database Schema:** `SIE557_ForwardEngineeredDB_Marshall.Gregg.sql` *(Note: The "Capacity" column in the main table was altered to `decimal(10,1)` to hold the correct type of numeric data).*
  * **Source Data:** `SIE557_FP_OriginalData_Marshall.Gregg.csv` (Used to build the database on phpMyAdmin).
  * **Table Exports:** Complete data exports from every table in both SQL and Excel/CSV formats.

---

## How to Run
1. Ensure your MAMP server is running and your SQL database is initialized using the provided forward-engineered script.
2. Verify connection settings in `db_config_file2.py`.
3. Run the main script from your terminal or IDE:
   ```bash
   python "Maine Power Stations Database.py"
   ```

<small>*Google Gemini and Anthropic's Claude were used for spell checking, basic debugging, function lookup, and providing examples for me to learn during the process.*</small>

<small>*Google Gemini used in creation of README.*</small>
