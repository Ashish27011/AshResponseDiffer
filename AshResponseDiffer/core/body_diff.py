import difflib
def show_diff(url_one_dick, url_two_dick):

    try:
        print("")
        file = open("AshResponseDiffer/outputs/change_content.txt", "w") 
        terminal_data = []
        file_data = []
        
        a = (url_one_dick.get("Body") or "").splitlines()
        b = (url_two_dick.get("Body") or "").splitlines()
        if a == b:
            terminal_data.append("Response are Equal!")
        else:
            terminal_data.append("Unmatched Data Stored In : change_content.txt")
            for line in difflib.unified_diff(a, b, fromfile="a", tofile="b", n=0, lineterm="",):

                if line.startswith("+++") or line.startswith("---") or line.startswith("@@"):
                    terminal_data.append(line)
                else:
                    file_data.append(line)    

        for text_list in file_data:
            file.write("Changed Response : "+ text_list+"\n")
           

    except Exception as e:
        print("ERROR OCCURE!", e)    

    return terminal_data, file_data            
