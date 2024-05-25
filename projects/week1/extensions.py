f_name = input("Enter the file name with extension : ")

def main():
    if f_name.endswith(".gif"):
        return "image/gif"
    elif f_name.endswith(".jpg"):
        return "image/jpg"
    elif f_name.endswith(".jpeg"):
        return "image/jpg"
    elif f_name.endswith(".png"):
        return "image/png"
    elif f_name.endswith("pdf"):
        return "appliaction/pdf"
    elif f_name.endswith(".txt"):
        return "text/plain"
    elif f_name.endswith(".zip"):
        return "application/zip"
    else:
        return "application/octet-stream"

a = main()
print(a)
