from bs4 import BeautifulSoup
import pandas as pd
import requests
from urllib.request import urlopen
import json
import streamlit as st
import plotly_express as px
import datetime 
import time
import numpy as np

l=[]
name=[]
totalcase=[]
activecase=[]
deathcase=[]
recoveredcase=[]



@st.cache 
def loaddata(url):
    site=urlopen(url)
    return(json.load(site))
#url="https://covid19-server.chrismichael.now.sh/api/v1/IndiaCasesByStates"
url1="https://api.quarantine.country/api/v1/summary/latest"

hunt=loaddata(url1)
#result=loaddata(url)
#a=result
state=[]
active=[]
confirm=[]
death=[]
lastupdated=[]
recovered=[]

def allvalue(u):
    for key,value in u.items():
        if type(value) is dict:
            allvalue(value)
        else:
            if(key=='name'):
                name.append(value)
            if key=='total_cases':
                totalcase.append(value)
            if key=='active_cases':
                activecase.append(value)
            if key=='deaths':
                deathcase.append(value)
            if key=='recovered':
                recoveredcase.append(value)

u=hunt.get('data').get('regions')

allvalue(u)

ar=[]
b=[]
c=[]
d=[]
er=0
for g in range(0,448):
    if g%2==0:
        ar.append(totalcase[g])
        b.append(activecase[g])
        c.append(deathcase[g])
        d.append(recoveredcase[g])

rf=pd.DataFrame(name,columns=['country'])
rf['totalcase']=ar
rf['activecase']=b
rf['death']=c
rf['recovered']=d


                
for i in range(len(a.get('data')[0].get('table'))):
    state.append(a.get('data')[0].get('table')[i].get('state'))
    active.append(a.get('data')[0].get('table')[i].get('active'))
    confirm.append(a.get('data')[0].get('table')[i].get('confirmed'))
    death.append(a.get('data')[0].get('table')[i].get('deaths'))
    lastupdated.append(a.get('data')[0].get('table')[i].get('lastupdatedtime'))
    recovered.append(a.get('data')[0].get('table')[i].get('recovered'))

h=state[0]
he=active[0]
her=confirm[0]
herf=death[0]
herfd=lastupdated[0]
yet=recovered[0]

df=pd.DataFrame(state[1:],columns=['state'])
df['confirmed']=confirm[1:]
df['active']=active[1:]
df['deaths']=death[1:]
df['lastupdated']=lastupdated[1:]
df['recovered']=recovered[1:]


st.sidebar.image('image/virus.png',width=200)
st.sidebar.header("C0VID-19")
selected=st.sidebar.selectbox('select',['Home','Precaution','About'])
if selected=='Home':
    st.sidebar.subheader(selected)
    st.image('image/search.png')
    st.title(" Covid-19 Tracker")
    st.markdown("Tracking the covid-19 cases in india🦠 😷🔬")
    st.write(rf)
    hl=px.bar(df,x='state',y='confirmed',color='active',height=500)
    st.plotly_chart(hl)
    fig = px.scatter(df, x ='state',y='confirmed',color='deaths')
    st.plotly_chart(fig)
    rest='Total confirmed cases in India  :  '+str(her)
    st.info(rest)
    stes='Total deaths in india :'+ herf
    st.warning(stes)
    st.write(datetime.datetime.now())

    

    
    st.table(df)
    st.map()
    st.image('image/map.jpg',width=1000)
    



if selected=='Precaution':
    st.sidebar.subheader(selected)
    st.subheader('symptoms')
    st.image('image/symptoms.png')
    st.write(' ')
    st.write(' ')
    st.subheader('Avoid')
    st.image('image/avoid.png')
    st.write(' ')
    st.write(' ')
    st.subheader('prevention')
    st.image('image/prevention.png')


if selected=='About':
    st.sidebar.subheader(selected)
    st.title('Coronavirus infection')
    st.markdown('coronavirus disease 2019(COVID-19)')
    st.image('image/corona.jpg',width=800)
    st.markdown('A cluster of pneumonia of unknown etiology was reported in Wuhan City, Hubei Province of China on 31 December 2019.  On 7 January Chinese authority identified a new type of coronavirus as a cause of pneumonia outbreak, which is different from any other human coronaviruses discovered so far')
    st.markdown('The new strain is named as severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2) and disease as COVID-19. While communicating with public, World Health Organization (WHO) has begun referring to the virus as “the virus responsible for COVID-19” or “the COVID-19 virus”')
    st.markdown('This outbreak was declared as a “Public Health Emergency of International Concern” (PHEIC) on 30th January 2020 by WHO under International Health Regulations (IHR) (2005) and subsequently WHO declared it pandemic on 11th March, 2020.')
    st.markdown('Preliminary investigations have identified environmental samples positive for nCoV in Huanan Seafood Wholesale Market in Wuhan City, however some laboratory-confirmed cases have not visited this market. According to WHO, additional investigations are needed to determine how the patients were infected, the extent of human-to-human transmission, the clinical spectrum of disease, and the geographic range of infection.')
    st.markdown('(SARS- CoV was first reported in 2002-2003 in Guangdong, China and MERS Coronavirus was first identified in Saudi Arabia in 2012.)  ')
    st.markdown('Coronaviruses (CoV) are a large family of viruses that can cause mild illness in the form of common cold to severe respiratory diseases such as MERS-CoV and SARS-CoV. A novel coronavirus is a new strain that has not been previously identified in humans.')
    st.markdown('Coronaviruses are zoonotic; it means they can be transmitted between animals and people. Previous investigations showed that SARS-CoV was transmitted from civet cats to humans and MERS-CoV from dromedary camels to humans.')
    st.markdown('Common symptoms of infection may be in the form of respiratory symptoms such as fever, cough, shortness of breath and breathing difficulties. In more severe cases, infection can cause pneumonia, severe acute respiratory syndrome, kidney failure and even death.')
    st.markdown('Most people infected with COVID-19 virus (approximately 80% of laboratory confirmed patients) have mild disease and recover, while 15% of cases require hospitalization and 5% of cases may be critical requiring ventilator management.')
    st.markdown('Risk communication is initiated for creating awareness among public to follow preventive public health measures such as personal hygiene, hand hygiene and respiratory etiquettes, promote use of face cover and physical distancing. ')
    



