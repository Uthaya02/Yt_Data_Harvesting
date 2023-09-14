

pip install google-api-python-client

from googleapiclient.discovery import build
import pandas as pd
import seaborn as sns

api_key ='AIzaSyDYJ6XqNUiLLbSiBcmWCNw6dNFX4iVb-b0'

channel_ids = ['UC2J_VKrAzOEJuQvFFtj3KUw', #1.CSK
               'UCCBe9iIoN9Ar-Elluxca-Xw', #2.GT
               'UC-mi8xUqL43BMlhvJbAf-Ew', #3.LSG
               'UCl23mvQ3321L7zO6JyzhVmg', #4.MI
               'UCkpgyRmcNy-aZFLUkKkWK4w', #5.RR
               'UCCq1xDJMBRF61kiOgU90_kw', #6-RCB
               'UCp10aBPqcOeBbEg7d_K9SBw', #7-KKR
               'UCvRa1LWA_-aARq1AQMC4AyA', #8-PG
               'UCEzB47eM-HZu04f4mB2nycg', #9-DC
               'UCScgEv0U9Wcnk24KfAzGTXg' #10-SRH
              ]
youtube = build('youtube', 'v3', developerKey=api_key)

def channel_data(youtube, channel_ids):
    all_data = []
    request = youtube.channels().list(
                part='snippet,contentDetails,statistics',
                id=','.join(channel_ids))
    response = request.execute()

    for i in range(len(response['items'])):
        data = dict(Channel_name = response['items'][i]['snippet']['title'],
                    Subscribers = response['items'][i]['statistics']['subscriberCount'],
                    Total_videos = response['items'][i]['statistics']['videoCount'],
                    Views = response['items'][i]['statistics']['viewCount'],
                    playlist_id = response['items'][i]['contentDetails']['relatedPlaylists']['uploads'])
        all_data.append(data)

    return all_data

channel_statistics = channel_data(youtube, channel_ids)

channel_data = pd.DataFrame(channel_statistics)

channel_data

channel_data.dtypes

channel_data['Subscribers'] = pd.to_numeric(channel_data['Subscribers'])
channel_data['Views'] = pd.to_numeric(channel_data['Views'])
channel_data['Total_videos'] = pd.to_numeric(channel_data['Total_videos'])
channel_data.dtypes

sns.set(rc={'figure.figsize':(22,7)})
ax = sns.barplot(x = 'Channel_name', y = 'Subscribers', data=channel_data)

ax = sns.barplot(x = 'Channel_name', y = 'Views', data=channel_data)

ax = sns.barplot(x = 'Channel_name', y = 'Total_videos', data=channel_data)

channel_data

playlist_id = channel_data.loc[channel_data['Channel_name']=='Chennai Super Kings', 'playlist_id'].iloc[0]

playlist_id

#function to get video ids

def get_video_ids(youtube, playlist_id):

    request = youtube.playlistItems().list(
                part='contentDetails',
                playlistId = playlist_id,
                maxResults = 50)
    response = request.execute()

    video_ids = []

    for i in range(len(response['items'])):
        video_ids.append(response['items'][i]['contentDetails']['videoId'])

    next_page_token = response.get('nextPageToken')
    more_pages = True

    while more_pages:
        if next_page_token is None:
            more_pages = False
        else:
            request = youtube.playlistItems().list(
                         part='contentDetails',
                         playlistId = playlist_id,
                         maxResults = 50,
                         pageToken = next_page_token)
            response = request.execute()

            for i in range(len(response['items'])):
                video_ids.append(response['items'][i]['contentDetails']['videoId'])

            next_page_token = response.get('nextPageToken')

    return video_ids

video_ids = get_video_ids(youtube, playlist_id)
video_ids

#function to get video details

def get_video_details(youtube, video_ids):
    all_video_stats = []

    for i in range(0, len(video_ids), 50):
        request = youtube.videos().list(
                    part='snippet,statistics',
                    id=','.join(video_ids[i:i+50]))
        response = request.execute()

        for video in response['items']:
            video_stats = dict(Title = video['snippet']['title'],
                              Published_date = video['snippet']['publishedAt'],
                              Views = video['statistics']['viewCount'],
                              Likes = video['statistics']['likeCount'],
                              #Dislikes = video['statistics']['dislikeCount'],
                              Comments = video['statistics']['commentCount']
                              )
            all_video_stats.append(video_stats)

    return all_video_stats

video_details = get_video_details(youtube, video_ids)

video_data = pd.DataFrame(video_details)

video_data['Published_date'] = pd.to_datetime(video_data['Published_date']).dt.date
video_data['Views'] = pd.to_numeric(video_data['Views'])
video_data['Likes'] = pd.to_numeric(video_data['Likes'])
#video_data['Views'] = pd.to_numeric(video_data['Views'])
video_data['Comments'] = pd.to_numeric(video_data['Comments'])
video_data

top10_videos = video_data.sort_values(by='Views', ascending=False).head(10)
top10_videos

sns.set(rc={'figure.figsize':(7,7)})
ax = sns.barplot(x='Views', y='Title', data=top10_videos)

video_data

video_data['Month'] = pd.to_datetime(video_data['Published_date']).dt.strftime('%b')
video_data

video_data['Published_date'] = pd.to_datetime(video_data['Published_date']).dt.date

videos_per_month = video_data.groupby('Month', as_index=False).size()
videos_per_month

sort_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'
             'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

videos_per_month.index = pd.CategoricalIndex(videos_per_month['Month'], categories=sort_order, ordered=True)

videos_per_month = videos_per_month.sort_index()
sns.set(rc={'figure.figsize':(10,5)})
ax2 = sns.barplot(x='Month', y='size', data=videos_per_month)

video_data.to_csv('uthaya.csv')
video_data.to_json('uthaya.json')

pip install pymongo

import pymongo

client = pymongo.MongoClient('mongodb+srv://uthaya05:uthesh05@uthaya0.pawhyo8.mongodb.net/?retryWrites=true&w=majority')

db = client['yt']

client.list_database_names()

db = client['yt']

db.list_collection_names()

client.list_database_names()

db = client["Yt"]

my_collection = db['youtube_channel_details']

import json

file = open("uthaya.csv","r")

for i in file:
    print(i)

print(file)

c =0

for i in file:
    if c<=5:
        print(i)
    else:
        break
    c=c+1

new = db["database_yt"]

client.list_database_names()

db.list_collection_names()

for i in file:
    x = json.loads(i)
    new.insert_one(x)

file = open("uthaya.json","r")

for i in file:
    print(i)

my_collection



import pandas as pd

from sqlalchemy import create_engine

pip install mysql

!pip install psycopg2-binary

import psycopg2

uthaya = psycopg2.connect(host = 'localhost',user = 'postgres',password='Aqwerty@1',port = 5432,database = 'uthaya')

engine = create_engine(connection_string)

channel_df = pd.DataFrame(list(collection.find()))
channel_df.to_sql('channels', engine, if_exists='replace', index=False)

video_df = pd.DataFrame(list(collection.find()))
video_df.to_sql('videos', engine, if_exists='replace', index=False)
