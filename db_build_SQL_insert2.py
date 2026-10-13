# Gregg Marshall
# SIE 557
# Lab 8
# 4/20/2026 - 5/5/2026

import pymysql
from . import db_config_file2

# -- Construct SQL Query Function --
def build_insert(new_data):

    # The connection to the Database is established with the info from
    # db_config_file.
    try:
        con = pymysql.connect(
            host=db_config_file2.DB_SERVER,
            user=db_config_file2.DB_USER,
            password=db_config_file2.DB_PASS,
            database=db_config_file2.DB
        )

        with con:
            with con.cursor() as cursor:
                # Selects the County_ID by swapping "county_name" with the placeholder.
                cursor.execute("SELECT County_ID FROM county WHERE County_Name = %s",
                               (new_data["county_name"],))
                
                county_row = cursor.fetchone()

                # Selects the Generation_ID by swapping "generation_type" with the placeholder.
                cursor.execute("SELECT Generation_ID FROM generation WHERE Generation_Type = %s",
                               (new_data["generation_type"],))
                
                generation_row = cursor.fetchone()

                # Developer is checked to see if it is already in the database.
                cursor.execute("INSERT IGNORE INTO developer (Developer_Name) VALUES (%s)",
                               (new_data["developer_name"],))
                
                cursor.execute("SELECT Developer_ID FROM developer WHERE Developer_Name = %s",
                               (new_data["developer_name"],))
                
                developer_row = cursor.fetchone()

                # -- Check that all data was entered --
                # Developer doesn't need to be checked because the user might
                # have to add a new developer to the database.
                if not all([county_row, generation_row]):
                    print("Submission Error: One or more lookup values not found.")
                    return False

                # -- Find ID from database --
                county_id = county_row[0]
                generation_id = generation_row[0]
                developer_id = developer_row[0]

                # -- Create Query and Substitute Values --
                insert_query = """
                    INSERT INTO project
                        (project_name, operational_status, capacity_mw, county_id, generation_id, developer_id)
                    VALUES
                        (%s, %s, %s, %s, %s, %s)
                """
                cursor.execute(insert_query, (
                    new_data["project_name"],
                    new_data["operational_status"],
                    new_data["capacity"],
                    county_id,
                    generation_id,
                    developer_id
                ))
        
            con.commit()
            print("Successfully added project to database.")
            return True
    
    except pymysql.Error as e:
        print(f"An error occurred adding project to database : {e}")
        return False