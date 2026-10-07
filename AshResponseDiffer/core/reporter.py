def show_reports(url_one_dick, url_two_dick, comp_response_dick, terminal_data, summary_response):

   try:
    item_dick = {"Url" : "URL",
                 "Status" : "Status Code",
                 "Lenght" : "Content Lenght",
                 "Time" : "Response Time" 
                 }
    difference_list = ["Status", "Lenght", "Url", "Time"]
    difference_list_i = ["Status", "Headers", "Body", "Lenght"]
    print("")


    print("".ljust(30),"RESPONSE A")
    print("_"*130)
    print("")
    for list_i, message in item_dick.items():
      final_response = url_one_dick.get(list_i)
      print(message.ljust(5),":",final_response)
    print("")  


    print("".ljust(30),"RESPONSE B")
    print("_"*130)
    print("")
    for list_ii, message in item_dick.items():
      final_response_i = url_two_dick.get(list_ii)
      print(message.ljust(5),":",final_response_i)
    print("")


    print("_"*130)
    print("".ljust(30),"DIFFERENCES")        
    print("")
    for item_iii in difference_list:
     compara_checks = comp_response_dick.get(item_iii)
     print(compara_checks)
     print("") 
    print("")


    print("_"*130)
    print("".ljust(30),"BODY DIFFERENCES")        
    print("")   
    for data in terminal_data:
      print(data)
    print("")  

    print("_"*130)
    print("".ljust(30),"SUMMARY")        
    print("")     
    for summary_data in difference_list_i:
      final_summary = summary_response.get(summary_data)
      print(final_summary)
    print("")  

   except Exception as e:
     print("ERROR OCCURE!", e)   
