from datetime import datetime, timezone
import pytz
import pytz

def print_time(timestamp):

    # Convert timestamp to UTC time
    utc_time = datetime.fromtimestamp(timestamp, tz=timezone.utc)

    # Define Eastern Time (ET) timezone
    eastern = pytz.timezone('America/New_York')

    # Convert UTC time to Eastern Time
    eastern_time = utc_time.replace(tzinfo=pytz.utc).astimezone(eastern)

    print("Eastern Time:", eastern_time.strftime('%Y-%m-%d %H:%M:%S %Z%z'))