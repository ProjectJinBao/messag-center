from database.db_content import Content

def svc_create_content(body):
    name = body.get("name")
    msgtype = body.get("msgtype")
    content = body.get("content")
    project = body.get("project")
    sprint = body.get("sprint")
    Content.db_create_content(msgtype=msgtype, name=name, content=content, project=project, sprint=sprint )

def svc_get_content():
    data = Content.db_get_content()
    return data

def svc_update_content(name, body):
    content = body.get("content")
    msgtype = body.get("msgtype")
    project = body.get("project")
    sprint = body.get("sprint")
    Content.db_update_content(name=name, content=content, msgtype=msgtype, project=project, sprint=sprint)

def svc_delete_content(name):
    Content.db_delete_content(name)