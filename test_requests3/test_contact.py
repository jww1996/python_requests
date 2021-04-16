import requests


def get_token():
    r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=wwd0c073a797282b83&corpsecret=9AjwgUixNyV3nOcyqQX5qLKDPuHRFcpRzkEopDRgX9w")
    # 打印原生格式
    print(r.raw)
    # r.json()可以展示企业微信真实的结果
    # 打印access_token
    print(r.json()["access_token"])
    assert r.json()["errcode"] == 0
    token = r.json()["access_token"]
    return token
# 读取成员
def test_defect_member():
    get_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={get_token()}&userid=12'
    r = requests.get(url=get_member_url)
    print(r.json())
    assert r.json()["name"] == "1212123"

# 更新成员
def test_update_member():
    data = {
        "userid": "12",
        "name": "1212123"
    }
    update_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={get_token()}'
    r = requests.post(url=update_member_url, json=data)
    print(r.json())

# 创建成员
def test_add_member():
    data = {
        "userid": "zhangsan001",
        "name": "张三001",
        "alias": "jackzhang",
        "mobile": "+86 13812300000",
        "department": [1]
    }
    add_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={get_token()}'
    r = requests.post(url=add_member_url, json=data)
    print(r.json())

# 删除成员
def test_delete_member():
    delete_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={get_token()}&userid=zhangsan001'
    r = requests.get(url=delete_member_url)
    print(r.json())