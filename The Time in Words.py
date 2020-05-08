def fun(n):
    # n=int(input())


    d={
    1:'one',
    2:'two',
    3:'three',
    4:'four',
    5:'five',
    6:'six',
    7:'seven',
    8:'eight',
    9:'nine',
    10:'ten',
    11:'eleven',
    12:'twelve',
    13:'thirteen',
    14:'fourteen',
    15:'fifteen',
    16:'sixteen',
    17:'seventeen',
    18:'eighteen',
    19:'nineteen',
    20:'twenty',
    21:'twenty one',
    22:'twenty two',
    23:'twenty three',
    24:'twenty four',
    25:'twenty five',
    26:'twenty six',
    27:'twenty seven',
    28:'twenty eight',
    29:'twenty nine',
    30:'thirty',
    31:'thirty one',
    32:'thirty-two',
    33:'thirty-three',
    34:'thirty-four',
    35:'thirty-five',
    36:'thirty-six',
    37:'thirty-seven',
    38:'thirty-eight',
    39:'thirty-nine',
    40:'forty',
    41:'forty one',
    42:'forty two',
    43:'forty three',
    44:'forty four',
    45:'forty five',
    46:'forty six',
    47:'forty seven',
    48:'forty eight',
    49:'forty nine',
    50:'fifty',
    51:'fifty one',
    52:'fifty two',
    53:'fifty three',
    54:'fifty four',
    55:'fifty five',
    56:'fifty six',
    57:'fifty seven',
    58:'fifty eight',
    59:'fifty nine',
    60:'sixty'}


    return d[n]



hr=int(input())
min=int(input())

if min==0:print(str(fun(hr))+" o' clock")

elif min<15:
    if min<10:
        print(str(fun(min))+' minute past '+str(fun(hr)))
    else:print(str(fun(min))+' minutes past '+str(fun(hr)))


elif min==15:print('quarter past '+fun(hr))
elif min>15 and min<30:print(fun(min)+' minutes past '+str(fun(hr)))
elif min==30:print('half past '+str(fun(hr)))
elif min>30 and min!=45:print(fun(60-min)+' minutes to '+str(fun(hr+1)))
else:print('quarter to '+str(fun(hr+1)))


