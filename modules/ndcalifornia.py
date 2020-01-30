def instagram_handler(sender, message, bot_id, app_id):
    """Return NDCalifornia instagram story"""
    if '!ndcalifornia' in message or '!instagram' in message:
        return "https://www.instagram.com/stories/notredamecalifornia"
    return None