from utils.exception_handle import IsNotExist
class ContentHandle(object):
    def conten_handle_template(self,content):
        c = eval(content)  # dict格式的字符串，转字典，可以用eval方法
        num = len(c)
        i = 0
        list = []
        while(i<num):
            title = c[i].get("titile")
            words = c[i].get("words")
            color = c[i].get("color")
            info = c[i].get("info")
            print(list[i])
            if title != None:
                list[i] = title
            else:
                pass
            if words != None:
                list[i] = title + words
            if info != None:
                list[i] = title + words + list
            else:
                pass
            print(i)
            i=i+1


    # "content": f"DX DMP 2.3.0\n>* <font color=\"warning\">待修复：{new_num}</font>\n>* <font color=\"comment\">已修复：{fixed_num}</font>\n >* <font color=\"info\">已验证：{verified_num}</font>\n  "
    # ">* [JIRA链接](https://jira.daocloud.io/secure/RapidBoard.jspa?rapidView=305&projectKey=DX&view=detail&selectedIssue=DX-955&sprint=567)"


    def color_handle(self,color):
        if color == "green":
            mcolor = "info"
        elif color == "gray":
            mcolor = "comment"
        elif color == "Orange":
            mcolor = "warning"
        else:
            raise IsNotExist(title = '没有该种颜色', detail = f'没有【{color}】这种颜色')
        return mcolor



# a = ContentHandle().conten_handle_template('[{"words":"test"},{"words":'',"color":"green","info":"未修复"}]')

