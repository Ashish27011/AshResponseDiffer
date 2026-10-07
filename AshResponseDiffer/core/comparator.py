def show_comparator(url_one_dick, url_two_dick):
 
   try:

      comp_response_dick = {}
      message = {
         "Status" : "Status Code",
         "Lenght" : "Response Lenght",
         "Url" : "Final URL",
         "Time" : "Response Time"
      }
      for compare, messages in message.items():
         checker1 = url_one_dick.get(compare)
         checker2 = url_two_dick.get(compare)
         if checker1 != checker2:
            comp_response_dick[compare] = f"{messages} CHANGED: {checker1} --> {checker2}"
         else:
            comp_response_dick[compare] = f"{messages} SAME: {checker1} == {checker2}"

   except Exception as e:
      print("ERROR OCCURE!", e)   

   return comp_response_dick           

