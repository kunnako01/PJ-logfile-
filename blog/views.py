from django.shortcuts import render
import json
from django.http import HttpResponse
import ast
import re
from .forms import ContactForm
from datetime import datetime, date, time
from datetime import datetime as dt


def home(request):

    data_log = []
    datamarker = []
    datadate = []
    dataco = []
    datanew = []
    Real=[]
    Real2=[]
    count2=[]
    na = 1
    qw = 0
    nu =0
    i=0
    x=[]
    ttt=[]
    ttt2=[]
    book4=[]
    newdata={}
    For_HTML=[]
    Kai={}
    MOMO=[]
    Date_Real1=[]
    Date_Real=[]
    POO=[]
    For_HTML2=[]
    For_HTML3 = []
    with open('C:/python3.7/Work_Sof2/Django/MyProject/blog/templates/blog/newdataGG.json',mode = 'r') as f:
        for line in f:
            r= ast.literal_eval(line)
            data_log.append(r)
    For_HTML3 = data_log
    if request.method == 'POST':
        form = ContactForm(request.POST)
        search_query = request.POST.get('search_box', None)
        print(type(search_query))
        if form.is_valid():
            with open('C:/python3.7/Work_Sof2/Django/MyProject/blog/templates/blog/newdataGG.json',mode = 'r') as f:
                for line in f:
                    r= ast.literal_eval(line)
                    datanew.append(r)
            data_log = datanew
            For_HTML3 = data_log
            type1 = form.cleaned_data['type1']
            number1 = form.cleaned_data['number1']
            date = form.cleaned_data['date']
            date2 = form.cleaned_data['date2']
            ti1 = str(date)
            ti2 = str(date2)
            print(ti1)
            ts1 = ti1[0:10].split("-")
            sad1 = ti1[0:10]
            txx1 = re.sub("\-", "/", sad1)
            ts2 = ti2[0:10].split("-")
            sad2 = ti2[0:10]
            txx2 = re.sub("\-", "/", sad2)
            ttt1 = dt.strptime(str(txx1), "%Y/%M/%d")
            ttt2 = dt.strptime(str(txx2), "%Y/%M/%d")
            # ttt1 = date(int(ts1[0]),int(ts1[1]),int(ts1[2]))
            # ttt2 = date(int(ts2[0]),int(ts2[1]),int(ts2[2]))
            print(ts1)
            # if search_query != 0:
            #     for s1 in range(len(data_log)):
            #         SS1 = data_log[s1]
            #         IP_1 = SS1["IP"]
            #         if IP_1 == search_query:
            #             Real.append(data_log[s1])
            #             print(search_query)
                    
            if type1 != 1:
                if type1 == "2":
                    na = 2
                if type1 == "3":
                    na = 3
                if type1 == "4":
                    na = 4        
            else:
                na = 1
                data_log == data_log
            if len(ts1) == 3   and len(ts2) == 3:
                print(len(data_log))
                tcou = 0
                tcou2 = 0
                RE=0
                for t1 in range(len(data_log)):
                    N1=data_log[t1]
                    N2=N1["Date"]
                    pa2 = dt.strptime(str(N2), "%d/%M/%Y")
                    IP_1 = N1["IP"]
                    CO_1 = N1["Country"]
                    La_1 = N1["Lat"]
                    Lo_1 = N1["Lon"]
                    ST_1 = N1["Status"]
                    if pa2 >= ttt1 :
                        if search_query != '':
                            if IP_1 == search_query:
                                Real2.append(data_log[t1])
                            if CO_1 == search_query:
                                Real2.append(data_log[t1])
                            if str(La_1) == search_query:
                                Real2.append(data_log[t1])
                            if str(Lo_1) == search_query:
                                Real.append(data_log[t1])
                            if ST_1 == search_query:
                                Real2.append(data_log[t1])
                        else:
                            Real2.append(data_log[t1])
                for t22 in range(len(Real2)):
                    N1=Real2[t22]
                    N2=N1["Date"]
                    # pa3 = date(int(N2[6:10]),int(N2[3:5]),int(N2[0:2]))
                    pa3 = dt.strptime(str(N2), "%d/%M/%Y")
                    IP_1 = N1["IP"]
                    CO_1 = N1["Country"]
                    La_1 = N1["Lat"]
                    Lo_1 = N1["Lon"]
                    ST_1 = N1["Status"]
                    if ttt2 >= pa3:
                        if search_query != '':
                            if IP_1 == search_query:
                                Real.append(Real2[t22])
                            if CO_1 == search_query:
                                Real.append(Real2[t22])
                            if str(La_1) == search_query:
                                Real.append(Real2[t22])
                            if str(Lo_1) == search_query:
                                Real.append(Real2[t22])
                            if ST_1 == search_query:
                                Real.append(Real2[t22])
                        else:
                            Real.append(Real2[t22])
                

                    tcou = tcou +1
                data_log = Real
                datamarker = Real
                print(len(Real))
                RealGG=sorted(Real, key = lambda i: (i['IP'], i['Status'],i["Country"],i["Date"],i["Lat"],i["Lon"])) 
                while RE < len(RealGG):
                    tor2=RealGG[RE]
                    book4.append(tor2)
                    S=RealGG.count(tor2)
                    count2.append(S)
                    RE+=S
                s=0
                for i in range(len(count2)):
                    s+=int(count2[i])
                print(s)
                for i in range(len(book4)):
                    fil=book4[i]
                    ty=count2[i]
                    newdata[i]={"IP":fil["IP"],"Status":fil["Status"],"Country":fil["Country"],"Date":fil["Date"],"Lat":fil["Lat"],"Lon":fil["Lon"],"Count":ty}
                    For_HTML.append(newdata[i])
                for i in range(len(For_HTML)):
                    For_HTML2.append(For_HTML[i])
                For_HTML3 = sorted(For_HTML2, key = lambda i: (i['Count'])) 
                For_HTML3.reverse()
                datamarker = For_HTML3
            else:
                print('error')
                data_log == data_log
            print(ts2)
            if number1 != "0":
                if number1 == "10":
                    nu = 10
                    For_HTML3 = For_HTML3[0:10]
                    datamarker = For_HTML3
                elif number1 == "20":
                    nu = 20
                    For_HTML3 = For_HTML3[0:20]
                    datamarker = For_HTML3
                elif number1 == "50":
                    nu = 50
                    For_HTML3 = For_HTML3[0:50]
                    datamarker = For_HTML3
                elif number1 == "100":
                    nu = 100
                    For_HTML3 = For_HTML3[0:100]
                    datamarker = For_HTML3
                else:
                 For_HTML3 == For_HTML3
                 datamarker = For_HTML3
    else:
        form = ContactForm()
    data_log1=data_log[0:10]       
    context ={
        'dataco': dataco,
        'na' : na,
        'datadate' : datadate,
         'data_log': For_HTML3,
            'form': form ,
            'data_log1':data_log1,
            'datamarker':datamarker,
            'qw':qw
        }


    return render(request, 'blog/home.html', context)


def about(request):
    data_log = []
    datalat=[]
    datalon=[]
    dataco = []
    dataeq=[]
    dataeq12=[]
 
    i = 0
    with open('C:/python3.7/Work_Sof2/Django/MyProject/blog/templates/blog/newdata.json',mode = 'r') as f:
        for line in f:
            r= ast.literal_eval(line)
            data_log.append(r)
            datalat.append(r['Lat'])
            datalon.append(r['Lon'])
            dataco.append(r['Country'])
            i = i+1
    for k1 in range(i):
        dataeq = [datalon[k1],datalat[k1],dataco[k1]]
        dataeq12.append(dataeq)
            

    data_log1=data_log[0:10]
    dataeq1 = dataeq12[0:30]
    context ={
         'data_log': data_log,
        'data_log1': data_log1,
        'datalat':datalat,
        'datalon':datalon,
        'dataco':dataco,
        'dataeq1':dataeq1
        }
#     print(dataco)
#     print(datalat)
    print(dataeq1)
    return render(request, 'blog/about.html', context)


# Create your views here.
