import requests

from test_requests3.wework.base import Base


class Address(Base):

    # 读取成员
    def get_member_information(self, user_id):
        get_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/get'
        params = {
            "userid" : user_id
        }
        # 由于继承了Base类，s代表的session中包含了获取到的token，所以直接使用self.s.get就可以
        r = self.send("GET", url=get_member_url,params=params)
        return r.json()


    # 更新成员
    def update_member(self, user_id, name):
        data = {
            "userid": user_id,
            "name": name
        }
        update_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/update'
        r = self.send("POST", url=update_member_url, json=data)
        return r.json()

    # 创建成员
    def add_member(self, user_id, name, mobile, department):
        data = {
            "userid": user_id,
            "name": name,
            "mobile": mobile,
            "department": department
        }
        add_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create'
        r = self.send("POST", url=add_member_url, json=data)
        return r.json()

    # 删除成员
    def delete_member(self, userid):
        delete_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/delete'

        # url过长，使用params将参数单独列出放在requests请求中（参数是指url问号后面的内容）
        params = {
            "userid" : userid
        }
        r = self.send("GET",url=delete_member_url, params=params)

        # 返回删除的结果
        return r.json()