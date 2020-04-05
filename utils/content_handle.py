from utils.exception_handle import IsNotExist,FormatTypeError
from utils.exception_handle import IsExist, DefalutError,IsNotExist,NotMatch
class ContentHandle(object):
    @classmethod
    def conten_handle_template(self,content):
        """
        :param content: 将数据库中的markdown list的模式的格式转为markdown
        :return:
        """
        c = eval(content)  # dict格式的字符串，转字典，可以用eval方法
        num = len(c)
        i = 0
        a=[]
        while(i<num):
            title = c[i].get("titile")
            words = c[i].get("words")
            color = c[i].get("color")
            info = c[i].get("info")
            link = c[i].get("link")
            link_text = c[i].get("link_text")
            try:
                m_color = self.color_handle(color)
            except IsNotExist as e:
                raise FormatTypeError(title=f'{e.title}', detail=f'{e.detail}')
            if title != None and m_color == "":
                list = "**"+ title + "**" + '\n'
            elif title != None and m_color != None:
                list = f'<font color=\"{m_color}\">' + title + '</font>'+ '\n'
            elif words != None and info != None and m_color!= None:
               list = '>* ' + words + f'<font color=\"{m_color}\">' + info +'</font>'+ '\n'
            elif words != None and info != None and m_color == None:
                list = '>* ' + words +  info + '\n'
            elif info != None and m_color!= None:
                list = '>* ' + f'<font color=\"{m_color}\">' + info + '</font>'+ '\n'
            elif link != None and link_text!=None:
                list = '>* ' + f'[{link_text}]({link})'
            else:
                print("pass")
            a.append(list)
            i=i+1
        content_l = "".join(a)#把列表中的元素放在空串中，元素间用空格隔开
        return content_l


    # "content": f"DX DMP 2.3.0\n>* <font color=\"warning\">待修复：{new_num}</font>\n>* <font color=\"comment\">已修复：{fixed_num}</font>\n >* <font color=\"info\">已验证：{verified_num}</font>\n  "
    # ">* [JIRA链接](https://jira.daocloud.io/secure/RapidBoard.jspa?rapidView=305&projectKey=DX&view=detail&selectedIssue=DX-955&sprint=567)"

    @classmethod
    def color_handle(self,color):
        '''

        :param color: <font color="info">绿色</font>
                     <font color="comment">灰色</font>
                     <font color="warning">橙红色</font>
        :return:
        '''
        if color == "green":
            mcolor = "info"
            return mcolor
        elif color == "gray":
            mcolor = "comment"
            return mcolor
        elif color == "orange":
            mcolor = "warning"
            return mcolor
        elif color == "black":
            mcolor = ""
            return mcolor
        else:
            raise IsNotExist(title = '没有该种颜色', detail = f'没有【{color}】这种颜色')





# # a = ContentHandle().conten_handle_template('[{"words":"test"},{"words":'',"color":"green","info":"未修复"}]')
# #
# content = '[{"titile":"test","info":"未修复","words":"1" ,"color":"balck"}]'
# a = ContentHandle.conten_handle_template(content)

# a=ContentHandle.color_handle("balce")