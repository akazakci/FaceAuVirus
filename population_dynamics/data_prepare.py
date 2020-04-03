import pandas as pd
import numpy as np
import string 
from utils import remove_punctuation



 
filename = 'sample.csv' #change path of files 

df = pd.read_csv(filename)

# drop unnecessary columns
df = df.drop(['ad_position', 'app_bundle', 'app_id', 'app_name', 'auction_id', 'category', 'content_coppa_flag',
              'content_language','content_rating', 'domain', 'environment_type', 'inventory_interstitial', 
              'inventory_source','inventory_source_relationship', 'placement', 'platform_bandwidth', 
              'platform_browser', 'platform_browser_version', 'platform_carrier', 'platform_device_didmd5', 
              'platform_device_didsha1', 'platform_device_dpidmd5', 'platform_device_dpidsha1',
              'platform_device_idfa', 'platform_device_ifa', 'platform_device_make', 'platform_device_model', 
              'platform_device_screen_size', 'platform_device_type', 'platform_js', 'platform_os',
              'platform_os_version', 'segment_id', 'segment_user_id', 'site_id', 'site_name','video_boxing_allowed', 
              'video_companion_required', 'video_playback_method', 'video_player_size', 'video_start_delay', 'test', 
              'placement_type','bid_time_epoch_in_usecs', 'page_url', 'exchange_predicted_view_rate', 
              'available_deal_ids', 'exchange_auction_id', 'rewarded', 'bid_floor_micros', 'bid_floor_currency', 
              'display_manager', 'display_manager_ver', 'exchange_device_make', 'exchange_device_model', 'user_id_type', 
              'auction_type', 'publisher_id', 'ads_txt', 'matched_user_groups','video_protocols', 'banner_top_frame',
              'inventory_source_user_id', 'mccmnc', 'us_privacy', 'video_placement', 'experiment_user_index', 
              'publisher_name'], axis = 1 )

# drop nan columns
df = df.dropna(axis = 1)

# let us drop further 'geo_type', 'is_gdpr', 'request_id', 'geo_country' since they are constant (at least in this sample)
# let us also drop bid_time_utc (same as 'bid_time') and ip_range (same as ip_address)
# no need fo time of week or usertime of week
df =  df.drop(['geo_type', 'is_gdpr', 'request_id', 'geo_country','bid_time_utc','ip_range', 
              'time_of_week','user_time_of_week'], axis=1)


 df = df[df['geo_lat'] != 0] # drop rows with zero latitude 
 df = df[df['geo_long'] != 0] # drop rows with zero latitude 




exclude = set(string.punctuation) 
df['ip_address'] = df['ip_address'].apply(lambda ch: remove_punctuation(ch))
df['bid_time'] = pd.to_datetime(df['bid_time'])

df.columns = ['time','id','lat','long']

df.to_csv(cleaned_file,  index=False)
