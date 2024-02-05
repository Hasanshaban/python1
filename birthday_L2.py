def input_name():
    print(birthdy[name])

def cha_birthday():
        change_name = input("کدام اسم?:")
        birthdy[change_name] = input("تاریخ تولد جدید را وارد کنید؟:")
        print(birthdy)

birthdy={"علی": "فروردین 12","رضا":"مهر 12"}
print(birthdy)
while True:
    name = input("یک اسم از دیکشنری بالا انتخاب کن "
                 "و اگر می خواهید خارج شوید اینتر را بزنید:")
    if name in birthdy:
        input_name()
    else:
        print("اسم انتخابی در دیکشنری نیست")
        break
    change_birthday = input("آیا می خواهید تاریخ تولد را تغییر دهید؟: بله/خیر?")
    if change_birthday == "بله":
       cha_birthday()
    else:
        break








