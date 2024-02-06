#  اضافه کردن یک شخص با تاربخ تولد به متغیر دیکشنری
#پاک کردن اطلاعات شخص از متغیر دیکشنری
#setdefault() & update()
#del() & pop()

def insert_info_person(info_person_name, info_person_birthday):
    global birthday
    birthday[info_person_name] = info_person_birthday
    print(birthday)
    new_dict={info_person_name: info_person_birthday}
    birthday.update(new_dict)
    print(birthday)
    birthday.setdefault(info_person_name,info_person_birthday)
    print(birthday)

def delete_info_person(info_person_name):
        #del birthday[info_person_name]
        #print(birthday)
        birthday.pop(info_person_name)
        print(birthday)

birthday={"علی": "فروردین 12","رضا":"مهر 12"}
print(birthday)
while True:
    select=input("برای اضافه کردن شخص add را تایپ کنید و برای حذف کردن شخص del را تایپ کنید")
    if select=="add":
     info_person_name = input("اسم شخص را وارد کنید ")
     info_person_birthday=input("تاریخ تولد را وارد نمایید")
     insert_info_person(info_person_name,info_person_birthday)
    else:
        info_person_name = input("اسم شخص را وارد کنید ")
        delete_info_person(info_person_name)

