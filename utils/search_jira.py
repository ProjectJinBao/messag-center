
from jira import JIRA

#登录jira
def search_jira(project,sprint):

    jira = JIRA('https://jira.daocloud.io', basic_auth=('jing.yu', 'YUJINGguanguo99%'))
    try:
        issue_new = len(jira.search_issues(f'project = {project} AND Sprint = {sprint} AND status = "New"',maxResults=1000))
        issue_fixing = len (jira.search_issues(f'project = {project} AND Sprint = {sprint} AND status = "Fixing"',maxResults=1000))
        issue_fixed = len(jira.search_issues(f'project = {project} AND Sprint = {sprint} AND status = "Fixed"',maxResults=1000))
        issue_verified = len(jira.search_issues(f'project = {project} AND Sprint = {sprint} AND status = "verified"', maxResults=1000))
        return {"new_num":issue_new,
                "fixed_num":issue_fixed,
                "verified_num":issue_verified,
                "fixing_num":issue_fixing}

    except Exception as e:
        print(e.text)



