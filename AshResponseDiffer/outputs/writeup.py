import os

def show_writeup(url_one_dick, url_two_dick, comp_response_dick, terminal_data, summary_response):
    path = "AshResponseDiffer/reports/report.txt"
    os.makedirs(os.path.dirname(path), exist_ok=True)

    item_dick = {
        "Url": "URL",
        "Status": "Status Code",
        "Lenght": "Content Lenght",
        "Time": "Response Time",
    }
    difference_list = ["Status", "Lenght", "Url", "Time"]
    difference_list_i = ["Status", "Headers", "Body", "Lenght"]

    with open(path, "w", encoding="utf-8") as file:
        try:
            file.write("\n")

            file.write("".ljust(30) + " RESPONSE A\n")
            file.write("_" * 130 + "\n")
            file.write("\n")
            for list_i, message in item_dick.items():
                final_response = url_one_dick.get(list_i)
                file.write(message + " : " + str(final_response) + "\n")
            file.write("\n")

            file.write("".ljust(30) + " RESPONSE B\n")
            file.write("_" * 130 + "\n")
            file.write("\n")
            for list_ii, message in item_dick.items():
                final_response_i = url_two_dick.get(list_ii)
                file.write(message + " : " + str(final_response_i) + "\n")
            file.write("\n")

            file.write("_" * 130 + "\n")
            file.write("".ljust(30) + " DIFFERENCES\n")
            file.write("\n")
            for item_iii in difference_list:
                compara_checks = comp_response_dick.get(item_iii)
                file.write(str(compara_checks) + "\n")
                file.write("\n")
            file.write("\n")

            file.write("_" * 130 + "\n")
            file.write("".ljust(30) + " BODY DIFFERENCES\n")
            file.write("\n")
            for data in terminal_data:
                file.write(str(data) + "\n")
            file.write("\n")

            file.write("_" * 130 + "\n")
            file.write("".ljust(30) + " SUMMARY\n")
            file.write("\n")
            for summary_data in difference_list_i:
                final_summary = summary_response.get(summary_data, "No difference")
                file.write(str(final_summary) + "\n")
            file.write("\n")

        except Exception as e:
            print("ERROR OCCURRED!", repr(e))