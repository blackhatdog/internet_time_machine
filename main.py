import webbrowser as wb

print('Welcome to the internet time machine CLI')
Link=input('Enter the address of the site you would like to visit(Please include protocol like http://,https://)')
yyyy=input('year')
mm=input('month')
dd=input('day')
ITMLINK=('https://web.archive.org/web/'+yyyy+mm+dd+"/"+ Link)
print(ITMLINK)
wb.open(ITMLINK)