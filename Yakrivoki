from datetime import datetime
def current_time() -> dict:
    formatted_datetime = datetime.now().strftime("%d %m %Y %H %M %S ")

    l = []
    n = ""

    for i in formatted_datetime:
        if i.isdigit():
            n += i
        else:
            l.append(n)
            n = ""

    date_dict = {"Дата": l[0] ,"Месяц": l[1],"Год": l[2],"Час": l[3],"МинуткО": l[4],"СекундО": l[5]}
    return date_dict
