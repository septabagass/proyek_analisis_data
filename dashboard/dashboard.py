import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load data
day_df = pd.read_csv("dashboard/day.csv")
hour_df = pd.read_csv("dashboard/hour.csv")

day_df['dteday'] = pd.to_datetime(day_df['dteday'])

# Mapping
season_mapping = {
    1: 'spring',
    2: 'summer',
    3: 'fall',
    4: 'winter'
}
day_df['season_label'] = day_df['season'].map(season_mapping)

weathersit_mapping = {
    1: 'Clear',
    2: 'Mist',
    3: 'Light Rain',
    4: 'Heavy Rain'
}
day_df['weathersit_label'] = day_df['weathersit'].map(weathersit_mapping)


day_df['yr_label'] = day_df['yr'].map({0: 2011, 1: 2012})
hour_df['yr_label'] = hour_df['yr'].map({0: 2011, 1: 2012})


# Sidebar Filter 
st.sidebar.title("filter")

year = st.sidebar.selectbox('Pilih Tahun', ['Semua', 2011, 2012])

season = st.sidebar.selectbox("Pilih Musim", day_df['season_label'].unique())

# filtered_df = day_df[(day_df['season_label'] == season) & (day_df['yr_label'] == year)]
if year == "Semua":
    filtered_df = day_df[day_df['season_label'] == season]
else:
    filtered_df = day_df[(day_df['season_label'] == season) &(day_df['yr_label'] == year)]


# Header
st.title("Bike Sharing Dashboard")

st.markdown(f"### Data Tahun {year} - Musim {season.title()}")

# Matrics
col1, col2, col3 = st.columns(3)

col1.metric("Total Rental", int(filtered_df['cnt'].sum()))
col2.metric("Rata rata Rental", int(filtered_df['cnt'].mean()))
col3.metric("Max Rental", int(filtered_df['cnt'].max()))

# 1. Tren Harian
st.subheader("Insight 1: Rush Hour vs Non Rush Hour (2012)")

data_2012 = hour_df[(hour_df['yr_label'] == 2012) & (hour_df['workingday'] == 1)].copy()

def kategori_jam(jam):
    if (7 <= jam <= 9) or (17 <= jam <= 19):
        return 'rush_hour'
    else:
        return 'non_rush_hour'

data_2012['kategori_jam'] = data_2012['hr'].apply(kategori_jam)

rata2 = data_2012.groupby('kategori_jam')['registered'].mean()

if 'rush_hour' in rata2 and 'non_rush_hour' in rata2:
    rush = rata2['rush_hour']
    non_rush = rata2['non_rush_hour']
    persentase = ((rush - non_rush)/non_rush)*100
    st.metric("Perbedaan (%)", f"{persentase:.2f}%")

# 2. Casual vs Registered
st.subheader("Casual vs Registered")

user = filtered_df[['casual','registered']].sum()

fig, ax = plt.subplots()
user.plot(kind='bar',ax=ax)
st.pyplot(fig)


# Cuaca 
st.subheader("Pengaruh Cuaca")

weather = filtered_df.groupby('weathersit_label')['cnt'].mean()

fig, ax = plt.subplots()
weather.plot(kind='bar', ax=ax)
st.pyplot(fig)

# Pola Jam
st.subheader("Pola Penyewa Per Jam")

hour_filtered = hour_df[hour_df['yr_label'] == year].groupby('hr')['cnt'].mean()

fig, ax = plt.subplots()
hour_filtered.plot(ax=ax)
st.pyplot(fig)

# Workingday
st.subheader("Workingday vs Weekend")

work = filtered_df.groupby('workingday')['cnt'].mean()

fig, ax = plt.subplots()
work.plot(kind='bar', ax=ax)
st.pyplot(fig)

# Heatmap (Advanced)
st.subheader("Heatmap Jam vs Workingday")

pivot = hour_df.pivot_table(
    values='cnt',
    index='hr',
    columns='workingday',
    aggfunc='mean'
)

fig, ax = plt.subplots()
sns.heatmap(pivot, annot=False)
st.pyplot(fig)
