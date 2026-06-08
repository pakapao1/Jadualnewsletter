import streamlit as st
import calendar
from datetime import datetime, timedelta
import pytz
import re

# Set zon masa Kuala Lumpur
kl_tz = pytz.timezone('Asia/Kuala_Lumpur')
hari_ini_kl = datetime.now(kl_tz)

st.set_page_config(page_title="Kalendar Jadual Newsletter KL", layout="centered")
st.title("📆 Kalendar Kuda Newsletter (Waktu KL)")

# Data jadual dari teks kau [cite: 1]
data_jadual = """
week 24 (8-12 june )
Newsletter 
HTML: Syazwan
PDF: Irteira
JE Task: Suzie
Pic : Yusri

week 25 (15-19 june )
Newsletter 
HTML: Femi
PDF: Terry
JE Task: Naza
Pic : Yusri

week 26 (22-26 june )
Newsletter 
HTML: Nukman
PDF: Mizan
JE Task: Yusri
Pic : Yusri

week 27 (29 june-3 july )
Newsletter 
HTML: Aurellia
PDF: Atul
JE Task: Wardina
Pic : Amira

week 28 (6-10 july )
Newsletter 
HTML: Aziah
PDF: Eric
JE Task: Suzie
Pic : Amira
"""

# Parsing data [cite: 1]
jadual_khamis = {}
def month_to_num(m_name):
    months = {'june': 6, 'july': 7, 'august': 8, 'sept': 9, 'oct': 10}
    return months.get(m_name.lower().strip(), 6)

blocks = data_jadual.strip().split("\n\n")
for block in blocks:
    lines = block.split("\n")
    match = re.search(r'\((\d+)-.*?(\w+)\s*\)', lines[0])
    if match:
        hari_isnin = int(match.group(1))
        no_bulan = month_to_num(match.group(2))
        dt_isnin = datetime(2026, no_bulan, hari_isnin)
        dt_khamis = dt_isnin + timedelta(days=3)
        
        html_pic, main_pic = "", ""
        for line in lines:
            if "HTML:" in line: html_pic = line.split(":")[1].strip() [cite: 1]
            if "Pic :" in line: main_pic = line.split(":")[1].strip() [cite: 1]
        
        jadual_khamis[dt_khamis.strftime('%Y-%m-%d')] = {"html": html_pic, "pic": main_pic} [cite: 1]

# Setup Kalendar Bulanan (Mula hari Ahad)
calendar.setfirstweekday(calendar.SUNDAY)
tahun, bulan = 2026, 6  # Boleh tukar bulan kat sini (6 = June)

st.subheader(f"📅 {calendar.month_name[bulan]} {tahun}")

# Header Hari
cols_header = st.columns(7)
hari_nama = ["Ahd", "Isn", "Sel", "Rab", "Kha", "Jum", "Sab"]
for i, h in enumerate(hari_nama):
    cols_header[i].markdown(f"**{h}**")

# Matrix Kalendar
matrix_bulan = calendar.monthcalendar(tahun, bulan)
for minggu in matrix_bulan:
    cols = st.columns(7)
    for idx, hari in enumerate(minggu):
        if hari == 0:
            cols[idx].write(" ")
        else:
            dt_semasa = datetime(tahun, bulan, hari)
            key_tarikh = dt_semasa.strftime('%Y-%m-%d')
            
            # Highlight Hari Ini
            if hari == hari_ini_kl.day and bulan == hari_ini_kl.month:
                box_text = f"**{hari}** 🌟"
            else:
                box_text = f"{hari}"
                
            # Check kalau hari Khamis ada Task [cite: 1]
            if idx == 4 and key_tarikh in jadual_khamis:
                task = jadual_khamis[key_tarikh] [cite: 1]
                box_text += f"\n\n📌 **HTML:** {task['html']}\n\n**PIC:** {task['pic']}" [cite: 1]
                cols[idx].info(box_text)
            else:
                cols[idx].write(box_text)