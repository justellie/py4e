def timeConversion(s):
    #
    # Write your code here.
    #
    itsPm=False
    last=s[6:8]
    if s[8:]=='PM':
        itsPm=True
    arr=s.split(':')
    if itsPm and int(arr[0])<12:
        arr[0]=str(12+int(arr[0]))
        arr[2]=last
    elif itsPm and int(arr[0])==12:
        arr[2]=last
    if not itsPm and int(arr[0])==12:
        arr[2]=last
        arr[0]='00'
    elif not itsPm:
        arr[2]=last     
        
    return(':'.join(arr))