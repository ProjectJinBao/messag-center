
from database.db_content import Content
from database.db_info import Info


def db_sendmsg(content_name, rel_key):

    content = Content.db_content(name=content_name)
    url = Info.db_info(key=rel_key)
    return {
        "url": url,
        "content": content.get("content"),
        "project": content.get("project"),
        "sprint": content.get("sprint"),
        "msgtype": content.get("msgtype"),
        "type": content.get("type")
    }
