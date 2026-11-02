# Gregg Marshall
# SIE 557
# Lab 8
# 4/20/2026 - 5/5/2026

import customtkinter as ctk
import pywinstyles as pws
from Modules.db_config_file2 import INSERT_PASS
from Modules.db_build_SQL_query2 import build_query, run_query
from Modules.db_build_SQL_insert2 import build_insert
from PIL import Image

# -- Main Functions --
def run_app():
    try:

        # -- Create Main Window --

        root = ctk.CTk() 
        ctk.set_appearance_mode("dark") 
        pws.apply_style(root, "dark")
        root.title("Maine Power Stations")
        root.geometry("1400x600")

        return root

    except Exception as e:
        print(f"An error occurred while launching the app: {e}")
        
def build_tab_menu(root):
    try:

        # -- Create Tabs --

        tabview = ctk.CTkTabview(root)
        tabview.pack(fill="both", expand=True, padx=10, pady =10)

        tabview.add("Maine Energy Information")
        tabview.add("Power Station Search")
        tabview.add("Search Results")
        tabview.add("Add New Project")

        return tabview
    
    except Exception as e2:
        print(f"An error occurred while building the tab menu: {e2}")

def build_tab1(tabview):
    try:

        # -- First Tab: App Info --

        # -- Create Tab Header --

        info_label = ctk.CTkLabel(tabview.tab("Maine Energy Information"),
                                text="Let's learn about how Maine produces energy!",
                                font=("Arial", 36, "bold"))

        info_label.pack(pady=35,
                        padx=10)
        
        # -- App Information --

        body_text = ctk.CTkTextbox(
            tabview.tab("Maine Energy Information"),
            width=600,
            height=240,
            font=("Arial", 18),
            corner_radius=10,
            border_width=2
        )

        body_text.pack(pady=10,
                    padx=20,
                    fill="both",
                    expand=False)
        
        # -- Main Body of Text --

        content = (
    "Maine is a leader in clean energy production!\n\n"
    "Maine uses renewable resources like wind, solar, hydropower, and even biomass.\n\n"
    '"In 2024, renewable resources fueled 57% of Maine\'s total electricity net generation, with hydropower accounting for 32% of the state\'s total renewable generation."\n\n'
    '"The state\'s three largest power plants by generation are natural gas-fired. In 2024, natural gas fueled about 41% of the state\'s total generation."\n\n'
    '"In 2025, the passage of LD 1868 increased Maine\'s RPS from 80 percent by 2030 to 90 percent by 2040 and added a complementary 10 percent CES to reach 100 percent clean energy by 2040."'
    )

        # -- Index --
        body_text.insert("0.0",content)
        
        # -- Make Text Box Read Only --
        body_text.configure(state="disabled")

        # -- Create Bottom Label --

        info_label2 = ctk.CTkLabel(
            tabview.tab("Maine Energy Information"),
            text="Use this app to learn about your local energy resources!",
            font=("Arial", 36,"bold")
        )
        info_label2.pack(pady=(35,10))

        # -- Create Citation Label --

        footer_label = ctk.CTkLabel(
            tabview.tab("Maine Energy Information"),
            text="Source: Maine Governor's Energy Office & U.S. Energy Information Administration (EIA)",
            font=("Arial", 12, "italic"),
            text_color="gray",
        )

        footer_label.pack(pady=(5, 20), side="bottom")

    except Exception as e3:
        print(f"An error occurred while creating tab 1: {e3}")
    
def build_tab2(tabview, results_container, col_widths):
    try:

        # -- Second Tab: Search (Tab 3 built first in Main Code) --

        # Search Variables
        counties = ["Androscoggin", "Aroostook", "Cumberland", "Franklin", "Hancock", 
                    "Kennebec", "Knox", "Lincoln", "Oxford", "Penobscot", 
                    "Piscataquis", "Sagadahoc", "Somerset", "Waldo", "Washington", "York"]

        battery_var = ctk.IntVar(value = 0)
        biomass_var = ctk.IntVar(value = 0)
        gas_var = ctk.IntVar(value = 0)
        hydro_var = ctk.IntVar(value = 0)
        landfill_gas_var = ctk.IntVar(value = 0)
        oil_var = ctk.IntVar(value = 0)
        other_var = ctk.IntVar(value = 0)
        solar_var = ctk.IntVar(value = 0)
        waste_var = ctk.IntVar(value = 0)
        wind_var = ctk.IntVar(value = 0)

        op_var = ctk.IntVar(value=0)
        planned_var = ctk.IntVar(value=0)

        # -- Master Frame --

        master_frame = ctk.CTkFrame(tabview.tab("Power Station Search"), fg_color="transparent")
        master_frame.pack(expand="True", fill="both", pady=10)

        # -- Inner Frame -- 

        inner_frame = ctk.CTkFrame(master_frame, fg_color="transparent")
        inner_frame.pack(expand=True, fill="both")

        # -- Container 1 --

        container_1 = ctk.CTkFrame(inner_frame, corner_radius=10)
        container_1.pack(side="left", fill="y", padx=0, pady=10, anchor="n")

        # County Dropdown
        # Selected county stored in county_dropdown to be passed to query_search().
        county_label = ctk.CTkLabel(container_1, text="Step 1: Select County", font=("Arial", 14, "bold"))
        county_label.pack(pady=(10, 5))

        county_dropdown = ctk.CTkOptionMenu( 
            container_1,
            values = counties, 
            width = 200,
            dynamic_resizing = False
        )

        # Dropdown placeholder text.
        county_dropdown.set("Select County")
        county_dropdown.pack(padx=20, pady = 5, anchor="n")

        # Map of Maine Counties
        try:
            counties_image = ctk.CTkImage(light_image = Image.open("colorcounties2.png"), # Image source.
                                        dark_image = Image.open("colorcounties2.png"), # Image styling.
                                        size = (300, 400))
            
            image_label = ctk.CTkLabel(container_1,
                                    image = counties_image,
                                    text = "",
                                    fg_color = "transparent")
            
            image_label.pack(padx=20, pady=5, anchor="n")

        except FileNotFoundError as e6:
            print(f"Image not found: {e6}")

        # -- Container 2 --

        container_2 = ctk.CTkFrame(inner_frame, corner_radius=10)
        container_2.pack(side="left", expand=True, fill="y", padx=0, pady=10, anchor="n")

        # Checkbox Label
        checkbox_label = ctk.CTkLabel(container_2, text="Step 2: Select Generation Type", font=("Arial", 14, "bold"))
        checkbox_label.pack(pady=(10, 5))

        # Generation Type Checkbox Frame
        generation_frame = ctk.CTkFrame(container_2, fg_color = "transparent")
        generation_frame.pack(pady = 5, fill="x")

        # Generation Type Checkboxes
        ctk.CTkCheckBox(generation_frame, text = "Battery", variable = battery_var).pack(side = "top", padx = 10, pady = 7, anchor="w")
        ctk.CTkCheckBox(generation_frame, text = "Biomass", variable = biomass_var).pack(side = "top", padx = 10, pady = 7, anchor="w")
        ctk.CTkCheckBox(generation_frame, text = "Gas", variable = gas_var).pack(side = "top", padx = 10, pady = 7, anchor="w")
        ctk.CTkCheckBox(generation_frame, text = "Hydro", variable = hydro_var).pack(side = "top", padx = 10, pady = 7, anchor="w")
        ctk.CTkCheckBox(generation_frame, text = "Landfill, Gas", variable = landfill_gas_var).pack(side = "top", padx = 10, pady = 7, anchor="w")
        ctk.CTkCheckBox(generation_frame, text = "Oil", variable = oil_var).pack(side = "top", padx = 10, pady = 7, anchor="w")
        ctk.CTkCheckBox(generation_frame, text = "Other", variable = other_var).pack(side = "top", padx = 10, pady = 7, anchor="w")
        ctk.CTkCheckBox(generation_frame, text = "Solar", variable = solar_var).pack(side = "top", padx = 10, pady = 7, anchor="w")
        ctk.CTkCheckBox(generation_frame, text = "Waste", variable = waste_var).pack(side = "top", padx = 10, pady = 7, anchor="w")
        ctk.CTkCheckBox(generation_frame, text = "Wind", variable = wind_var).pack(side = "top", padx = 10, pady = 7, anchor="w")

        # Generation Key
        # CheckBox assigns selected variables to 1 via IntVar().
        # Variables updated with name string in generation_key.
        # generation_key passed to query_search().
        generation_key = {
            "Battery": battery_var,
            "Biomass": biomass_var,
            "Gas": gas_var,
            "Hydro": hydro_var,
            "Landfill Gas": landfill_gas_var,
            "Oil": oil_var,
            "Other": other_var,
            "Solar": solar_var,
            "Waste": waste_var,
            "Wind": wind_var
        }

        # -- Container 3 --

        container_3 = ctk.CTkFrame(inner_frame, corner_radius=10)
        container_3.pack(side="right", fill="y", padx=(10, 50), pady=10, anchor="n")

        # Operation Status Checkbox Label
        checkbox2_label = ctk.CTkLabel(container_3, text="Step 3: Select Operational Status", font=("Arial", 14, "bold"))
        checkbox2_label.pack(pady=(10, 5))

        # Operation Status Checkbox Frame
        status_frame = ctk.CTkFrame(container_3, fg_color = "transparent")
        status_frame.pack(pady = 5, fill="x")

        # Operation Status Checkboxes
        ctk.CTkCheckBox(status_frame, text = "Operational", variable = op_var).pack(side = "top", padx = 10, pady = 7, anchor="w")
        ctk.CTkCheckBox(status_frame, text = "Planned", variable = planned_var).pack(side = "top", padx = 10, pady = 7, anchor="w")

        # Status Key
        # CheckBox assigns selected variables to 1 via IntVar().
        # Variables updated with name string in status_key.
        # status_key passed to query_search().
        status_key = {
            "Operational": op_var,
            "Planned": planned_var
        }

        # -- Search Function --
        def query_search():

            # Menu selections passed to build_query() and returned as query
            # and params to be assigned to results. Tab 3 is opened.
            query, params = build_query(county_dropdown, generation_key, status_key)
            if query:
                results = run_query(query, params)
                display_results(results_container, results, col_widths, header_frame)
                tabview.set("Search Results")

        # -- Search Button Container --

        search_button = ctk.CTkButton(container_3,
                                    text="Search",
                                    font=("Arial", 16, "bold"),
                                    width=200,
                                    height=50,
                                    command= query_search
                                    )
        
        search_button.pack(pady=(100, 10), 
                        padx=10,
                        )
    
    except Exception as e4:
        print(f"An error occurred while building tab 2: {e4}")

def build_tab3(tabview):
    try:

        # -- Third Tab: Display Results --

        # Tab 3 is run before Tab 2 in the main code because Tab 2 needs
        # results_container and col_widths when calling display_results()
        # in query_search().

        # -- Results Container (ScrollableFrame) --
        results_container = ctk.CTkScrollableFrame(
            tabview.tab("Search Results"),
            label_text ="Power Station Search Results",
            label_font=("Arial", 16, "bold")
        )

        results_container.pack(fill="both", expand=True, padx=20, pady=20)

        # Header Frame
        header_frame = ctk.CTkFrame(results_container, fg_color='transparent')
        header_frame.pack(fill='x', pady=(0, 5), padx=5)

        # Results Table Headers
        headers = ["Name", "County", "Generation Type", "Operational Status", "Electrical Output (MW)", "Developer"]
        col_widths = [200, 120, 160, 170, 150, 200]

        # Header Formatting 
        for i, (header, width) in enumerate(zip(headers, col_widths)):
            label1 = ctk.CTkLabel(header_frame, text=header, font=("Arial", 12, "bold"), width=width, anchor="w")
            label1.grid(row=0, column=i, padx=5)

        return results_container, col_widths, header_frame

    except Exception as e5:
        print(f"An error occurred while building tab 3: {e5}")

def build_tab4(tabview):
    try:

        # -- Fourth Tab: Add New Project --

        # -- Entry Variables --
        counties = ["Androscoggin", "Aroostook", "Cumberland", "Franklin", "Hancock", 
                    "Kennebec", "Knox", "Lincoln", "Oxford", "Penobscot", 
                    "Piscataquis", "Sagadahoc", "Somerset", "Waldo", "Washington", "York"]
        
        generation_types = ["Battery", "Biomass", "Gas", "Hydro", "Landfill Gas", "Oil", "Other", "Solar", "Waste", "Wind"]

        status_types = ["Operational", "Planned"]

        # -- Create Tab Header --
        np_label = ctk.CTkLabel(tabview.tab("Add New Project"),
                                text="Submit New Project to Database",
                                font=("Arial", 36, "bold"))

        np_label.pack(pady=35,
                        padx=10)
        
        # -- Create Tab 4 Frame -- 
        np_frame = ctk.CTkFrame(tabview.tab("Add New Project"))
        np_frame.pack(pady=10, padx=10, fill="both", expand=True )
        
        # -- Project Name Entry Box --
        name_entry = ctk.CTkEntry(np_frame,
                                  placeholder_text="Enter Project Name",
                                  width=200)
        name_entry.pack(pady=10)

        # -- County Dropdown Entry --
        county_entry = ctk.CTkOptionMenu( 
            np_frame,
            values = counties, 
            width = 200)
        county_entry.set("Select County")
        county_entry.pack(pady=10)

        # -- Generation Type Dropdown Entry --
        generation_entry = ctk.CTkOptionMenu(np_frame,
                                             values = generation_types,
                                             width=200)
        generation_entry.set("Select Generation Type")
        generation_entry.pack(pady=10)

        # -- Status Type Dropdown Entry --
        status_entry = ctk.CTkOptionMenu(np_frame,
                                         values = status_types,
                                         width=200)
        status_entry.set("Select Operational Status")
        status_entry.pack(pady=10)

        # -- Capacity Entry --
        capacity_entry = ctk.CTkEntry(np_frame, placeholder_text="Enter MW (Num w/ 1 decimal)", width=200)
        capacity_entry.pack(pady=10)

        # -- Developer Name Entry --
        developer_entry = ctk.CTkEntry(np_frame, placeholder_text="Enter Developer Name", width=200)
        developer_entry.pack(pady=10)

        # -- Submit Data Function --
        def submit_data():
            
            # -- Check Admin Password--
            # Password check is required to prevent false entries from
            # flooding the database.
            def check_password():
                if password_entry.get() == INSERT_PASS:
                    popup.destroy()
                    validated_submission()
                else:
                    password_error_label.configure(text="⚠ Incorrect password.", text_color="red")
                
            popup = ctk.CTkToplevel()
            popup.title("Admin Password Required")
            popup.geometry("250x200")

            # -- Center the Password Entry Popup --
            run.update_idletasks()

            # -- Get Position of App --
            main_x = run.winfo_x()
            main_y = run.winfo_y()

            # -- Get Size of App --
            main_width = run.winfo_width()
            main_height = run.winfo_height()

            # -- Length of Popup Axes --
            popup_x = 250
            popup_y = 200

            # -- Calculate Center of Main App Window --
            center_app_x = main_x + (main_width // 2) - (popup_x // 2)
            center_app_y = main_y + (main_height // 2) - (popup_y // 2)

            popup.geometry(f"{popup_x}x{popup_y}+{center_app_x}+{center_app_y}")

            popup.grab_set() 

            # -- Password Popup and Button Formatting --
            ctk.CTkLabel(popup, text="Enter Password", font=("Arial", 14)).pack(pady=10)

            password_entry = ctk.CTkEntry(popup, show="*", width=200)
            password_entry.pack(pady=5)
            
            password_error_label = ctk.CTkLabel(popup, text="", font=("Arial", 12))
            password_error_label.pack(pady=5)

            ctk.CTkButton(popup, text="Confirm Password", command=check_password).pack(pady=5)

        # -- Submission Validation Function --
        def validated_submission():

            # This function runs tests to make sure data is appropriate for the database.

            # -- Validate Project Name Entry --
            if name_entry.get().strip() == "":
                validation_label.configure(text=f"⚠ Please Enter a project name.", text_color="red")
                return

            # -- Validate Developer Name Entry --
            if developer_entry.get().strip() == "":
                validation_label.configure(text=f"⚠ Please Enter a developer name.", text_color="red")
                return

            # -- Validate Capacity Entry --
            capacity_submission, error = validate_capacity(capacity_entry.get())
            if error:
                validation_label.configure(text=f"⚠ {error}", text_color="red")
                return
            
            # -- Clear Previous Error -- 
            validation_label.configure(text="")
            
            # -- Get Data and Organize --
            new_data = {
                "project_name": name_entry.get(),
                "county_name":county_entry.get(),
                "generation_type": generation_entry.get(),
                "operational_status": status_entry.get(),
                "capacity": capacity_submission,
                "developer_name": developer_entry.get()
            }

            # -- Total Submission Validation Message --
            if build_insert(new_data):
                validation_label.configure(text="✔ Project successfully added to database!", text_color="green")
            else:
                validation_label.configure(text="⚠ Submission failed. Please check your entries.", text_color="red")

        # -- Submit Button --
        submit_button = ctk.CTkButton(np_frame,
                                      text="Submit Project",
                                      fg_color="green",
                                      hover_color="#004225",
                                      command=submit_data)
        submit_button.pack(pady=30)

        # -- Validation Message --
        validation_label = ctk.CTkLabel(np_frame, text="", font=("Arial", 12))
        validation_label.pack(pady=(0, 10))

    except Exception as e6:
        print(f"An error occurred while building tab 3: {e6}")

# -- Display Results Function --
def display_results(results_container, results, col_widths, header_frame):
    try:

        # Erase Previous Results 
        # Any widget that is not header_frame is removed from results_container
        # when a new search is initiated. 
        for widget in results_container.winfo_children():
            if widget is not header_frame:
                widget.destroy()

        # No Results Message
        if not results:
            no_results_label = ctk.CTkLabel(results_container, text="No results found.", font=("Arial", 14))
            no_results_label.pack(pady=20)
            return
        
        # Results
        # A station_card is created for each row in results. 
        for row in results:
            station_card = ctk.CTkFrame(results_container)
            station_card.pack(fill="x", pady=5, padx=5)

            # Sets a minimum width for each column in the station_card.
            for i, width in enumerate(col_widths):
                station_card.grid_columnconfigure(i, minsize=width)

            # zip(row, col_widths) pairs each value in row with the width of
            # its column. The first value is given different styling than the
            # following values in its row. A label is created for each value in
            # each station_card and formatted to fit the results_container.
            for i, (value, width) in enumerate(zip(row, col_widths)):
                font = ("Arial", 14, "bold") if i == 0 else ("Arial", 12)
                label = ctk.CTkLabel(station_card, text=str(value), font=font, width=width, anchor="w", wraplength=width - 10, justify="left")
                label.grid(row=0, column=i, pady=10, padx=5, sticky="w")

    except Exception as e:
        print(f"An error occurred while displaying results: {e}")

# -- Validate Capacity Function --
def validate_capacity(cap_str):
    try:

        # This function checks to make sure capacity is a float that only extends
        # to the tenth's space. 
        valid_cap = float(cap_str.strip())

        if "." not in cap_str:
            return None, "Please include one decimal place (ex 8.1) in Capacity."
        
        dec_cap = cap_str.strip().split(".")[1]

        if len(dec_cap) != 1:
            return None, "Please include one decimal place (ex 8.1) in Capacity."
        
        return valid_cap, None
    except ValueError:
        return None, "Capacity must be a number with one decimal place (ex 8.1)"

# -- Main Code --
run = run_app()
tab_menu = build_tab_menu(run)
build_tab1(tab_menu)
results_container, col_widths, header_frame = build_tab3(tab_menu)
build_tab2(tab_menu, results_container, col_widths)
build_tab4(tab_menu)
run.mainloop()
