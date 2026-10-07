def show_analyzer(url_one_dick, url_two_dick):
    analyzer_message = {
        "Status" : "Status Code Changed",
        "Headers" : "Headers Difference Detected",
        "Body" : "Response Body Changed",
        "Lenght" : "Response Lenght Changed"
    }

    summary_response = {}
    for access, message in analyzer_message.items():
        checker1 = url_one_dick.get(access)
        checker2 = url_two_dick.get(access)
        if checker1 != checker2:
            summary_response[access] = f"[+] {message}"
        else:
            summary_response[access] = f"[-] No differences found: {access}"    

    return summary_response        
