'''
در این برنامه کاریر اطلاعات شخص را دارد می کند
و با تاربخ در یک فایل ذخیره می شود
'''
import datetime

def write_dic_birthday(birthday):

    date_object = str(datetime.date.today())
    print(date_object)
    file_birthday = open("Test.txt","a")
    file_birthday.write(date_object+birthday+"\n")
    file_birthday.close()





if __name__ == "__main__":

    birthday={}
    while True:
     name = input("What is your name or for exit press enter? ")
     if name == "":
        break
     else:
      birthday_date = input("What is your birthday date? ")
      birthday[name] = birthday_date
      print(birthday)

    write_dic_birthday(str(birthday))

