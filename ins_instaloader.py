import instaloader
from datetime import datetime, timedelta, timezone
import pytz

def download_ins_vedio(ins_id):

    now_datetime = datetime.now()
    one_week_ago = pytz.utc.localize(now_datetime - timedelta(weeks=1))

    ins_username = 'fanliyang2021'
    ins_password = '!et3.Emx2VQWnAW'
    # ins_id = 'kanye__west__only'

    ins_player = instaloader.Instaloader()
    ins_player.login(ins_username, ins_password)

    # ins_player.interactive_login(ins_username)
    # ins_player.load_session_from_file(ins_username)

    posts = instaloader.Profile.from_username(
        ins_player.context, ins_id).get_posts()

    for post in posts:
        if post.is_video:
            post_datetime_local = pytz.utc.localize(post.date)
            if post_datetime_local > one_week_ago:
                ins_player.download_post(post, 'videos')

    # clear vedio , delete *.xz files
