def passwordValidator(s):
    message = []

    if not any(x.isupper() for x in s):
        print("no upper letter please add one.")
    
    if not any(x.islower() for x in s):
        print("no lower letter please add one.")
    
    if not any(x.isnum() for x in s):
        print("no number  please add one.")
    if not any(x.isupper() for x in s):
        print("no upper letter please add one.")

    


    


