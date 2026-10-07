import requests
import time

def show_response(url_one, url_two):

    try:
        url_one_dick = {}
        url_two_dick = {}
    
        all_requests = [ (url_one, url_one_dick), (url_two, url_two_dick) ]
        for url, dick in all_requests:
            s_time = time.time()
            response_validator = requests.get(url, timeout=5)
            e_time = time.time()
            response_time = e_time - s_time

            dick.update({
                    "Status" : response_validator.status_code,
                    "Headers" : response_validator.headers,
                    "Body" : response_validator.text,
                    "Lenght" : response_validator.headers.get("Content-Length", "Not Found"),
                    "Url" : url,
                    "Time" : f"{response_time:.3f}s"
                })
    except Exception as e:
        print("ERROR OCCURE!", e)    
         

    return url_one_dick, url_two_dick