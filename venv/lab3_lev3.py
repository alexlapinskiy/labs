print("--- with IF ---")
day=int(input("Enter day of month: "))
if (day>31):
    print("Wrong number of day, max value is 31. Try again.")
elif(day==6):
    print("Petrenko A.O. Golos I.A.")
elif (day==15):
    print("Aleksievich A.O. Ivanov N.I.")
elif (day==18):
    print("Kurgan A.V. Males T.M. ")
elif(day==29):
    print("Maksimov M.M. Zarubin A.D.")
elif(day==3):
    print("Leonov A.P. Klinkov D.A.")
else:print("There are no birthdays on this day")
print("")

print("--- without IF ---")
day1=int(input("Enter day of month: "))
choices = {6:("Petrenko A.O. Golos I.A."),
           15:("Aleksievich A.O. Ivanov N.I."),
           18:("Kurgan A.V. Males T.M. "),
           29:("Maksimov M.M. Zarubin A.D."),
           3:("Leonov A.P. Klinkov D.A."),}
result = choices.get(day1, 'There are no birthdays on this day')
print(result)

