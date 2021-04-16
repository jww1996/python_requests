import pytest
import yaml

from test_requests3.wework.address import Address


class TestAddress:
    def setup(self):
        self.address = Address()
        self.user_id = "zhangsan001"
        self.name = "张三001"
        self.mobile = "+86 13812300000"
        self.department = [1]

    # 并行插件pytest-xdist
    @pytest.mark.parametrize(("user_id", "name", "mobile", "department"), yaml.safe_load(open("../wework/member.yaml","r", encoding="utf-8")))
    def test_create_member(self, user_id, name, mobile, department):
        # 利用删除接口进行数据清理
        self.address.delete_member(user_id)
        r = self.address.add_member(user_id, name, mobile, department)

        assert r.get('errmsg', "network error") == "created"
        s = self.address.get_member_information(user_id)
        # 删除刚刚创建的测试数据
        self.address.delete_member(user_id)
        # 断言获取到通讯录信息中name == 前面输入的name
        assert s.get("name") == name

    # 获取成员信息
    @pytest.mark.parametrize(("user_id", "name", "mobile", "department"),
                             yaml.safe_load(open("../wework/member.yaml", "r", encoding="utf-8")))
    def test_get_member_information(self, user_id, name, mobile, department):
        self.address.add_member(user_id, name, mobile, department)
        r = self.address.get_member_information(user_id)
        assert r.get("errmsg") == "ok"
        # 断言获取到通讯录信息中name == 前面输入的name
        assert r.get("name") == name

    # 删除成员
    @pytest.mark.parametrize(("user_id", "name", "mobile", "department"),
                             yaml.safe_load(open("../wework/member.yaml", "r", encoding="utf-8")))
    def test_delete_member(self, user_id, name, mobile, department):
        # 为避免删除成员时该成员不存在，首先先创建一个新成员
        self.address.add_member(user_id, name, mobile, department)
        r = self.address.delete_member(user_id)
        assert r.get("errmsg") == "deleted"
        s = self.address.get_member_information(user_id)
        # 删除成功后再查询，查询不到结果会返回errcode == 60111,删除成功
        assert s.get("errcode") == 60111

    # 更新
    @pytest.mark.parametrize(("user_id", "name", "mobile", "department"),
                             yaml.safe_load(open("../wework/member.yaml", "r", encoding="utf-8")))
    def test_update_member(self, user_id, name, mobile, department):
        # 为了保证成员一定是新添加的
        self.address.delete_member(self.user_id)
        self.address.add_member(user_id, name, mobile, department)

        new_name = name + "QAQ"
        r = self.address.update_member(user_id, new_name)
        assert r.get("errmsg") == "updated"
        s = self.address.get_member_information(user_id)
        # 断言获取到通讯录信息中name == 前面输入的name
        assert s.get("name") == new_name
