# Gregg Marshall
# SIE 557
# Lab 8
# 4/20/2026 - 5/5/2026

import pymysql
from . import db_config_file2

# -- Construct SQL Query Function --
def build_query(county_dropdown, generation_key, status_key):

    # County selection retrieved with get().
    selected_county = county_dropdown.get()

    # Generation Type and Status retrieved if IntVar(1) from for loop in keys.
    selected_types = [label for label, var in generation_key.items() if var.get() == 1]
    selected_statuses = [label for label, var in status_key.items() if var.get() == 1]

    # -- SQL Code --

    # The query selects "Project_Name," "Operational_Status," "Capacity_MW,"
    # from the "project" table in the database. "County_Name," "Generation_Type,"
    # and "Developer_Name" are joined from their respective tables on their
    # Foreign Key in "project" to comply with Normalization Standards.
    query = """
        SELECT 
            p.`Project_Name`, 
            c.`County_Name`, 
            g.`Generation_Type`,
            p.`Operational_Status`,
            p.`Capacity_MW`,
            d.`Developer_Name`
        FROM `project` p
        JOIN `county` c ON p.`County_ID` = c.`County_ID`
        JOIN `generation` g ON p.`Generation_ID` = g.`Generation_ID`
        JOIN `developer` d ON p.`Developer_ID` = d.`Developer_ID`
        WHERE c.`County_Name` = %s
    """
    params = [selected_county]

    # Placeholders are created for the number of selections made in Tab 2.
    # A string of SQL is formatted to be added to the query. The selections
    # are added to params[selected_county].
    if selected_types:
        placeholders = ", ".join(["%s"] * len(selected_types))
        query += f" AND g.`Generation_Type` IN ({placeholders})"
        params.extend(selected_types)

    if selected_statuses:
        placeholders = ", ".join(["%s"] * len(selected_statuses))
        query += f" AND p.`Operational_Status` IN ({placeholders})"
        params.extend(selected_statuses)

    # The query and list of parameters is passed to run_query().
    return query, params

# -- Establish Connection to Database, Execute Query, Close Connection -- 
def run_query(query, params):

    # The connection to the Database is established with the info from
    # db_config_file.
    try:
        con = pymysql.connect(
            host=db_config_file2.DB_SERVER,
            user=db_config_file2.DB_USER,
            password=db_config_file2.DB_PASS,
            database=db_config_file2.DB
        )

        # Create the cursor to communicate with database.
        cursor = con.cursor()
        
        # Execute the query and replace the placeholders "%s" with second argument. 
        cursor.execute(query, params)

        # fetchall() returns a list of tuples. Each tuple is a row of data from
        # the database corresponding to the search parameters. 
        results = cursor.fetchall()

        return results

    except pymysql.Error as e:
        print(f"Database error: Search Function Error {e}.")
        return None

    finally:

        # The cursor is dismissed and the connection is closed. 
        cursor.close()
        con.close()
