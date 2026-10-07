from urllib.parse import urlparse

def show_validator():
  while True:
   try:

    url_one = input("Enter Request A : ")
    url_two = input("Enter Request B : ")
    url_list = [url_one, url_two]
    all_valid = True
    for valid in url_list:
     url_validator = urlparse(valid)
     schemas_checker = url_validator.scheme
     hostname_checker = url_validator.netloc
     if schemas_checker not in ["http", "https"]:
      print("Invalid Schema!", valid)
      all_valid = False
     elif not hostname_checker:
      print("Invalid HostName!", valid)
      all_valid = False
    if all_valid:
      break

   except Exception as e:
    print("ERROR OCCURE!", e) 

  return url_one, url_two 