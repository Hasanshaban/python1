birthdy={"علی": "فروردین 12","رضا":"مهر 12"}
print(birthdy)
while True:

 name=input("یک اسم از دیکشنری بالا انتخاب کن "
            "و اگر می خواهید خارج شوید اینتر را بزنید:")

 if name in birthdy:
    print(birthdy[name])
    change_birthday = input("آیا می خواهید تاریخ تولد را تغییر دهید؟: بله/خیر?")
    if change_birthday == "بله":
        change_name=input("کدام اسم?:")
        birthdy[change_name] = input("تاریخ تولد جدید را وارد کنید؟:")
        print(birthdy)
    else:
        break

 else:
     if name=="":
      break
     else:
         print("اسم انتخابی در دیکشنری نیست")


