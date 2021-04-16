import requests


class Base:
    # 由于每次操作都需要获取token，所以在初始化中先获取token将其保存
    def __init__(self):
        # session 只发送一次握手和挥手，可以提高效率
        self.s = requests.Session()
        self.token = self.get_token()
        # 将token放到session中
        self.s.params = {"access_token": self.token}

    def get_token(self):
        corpid = "wwd0c073a797282b83"
        corpsecret = "9AjwgUixNyV3nOcyqQX5qLKDPuHRFcpRzkEopDRgX9w"
        r = requests.get(
            f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}")
        # 打印原生格式
        print(r.raw)
        # r.json()可以展示企业微信真实的结果
        # 打印access_token
        print(r.json()["access_token"])
        assert r.json()["errcode"] == 0
        token = r.json()["access_token"]
        return token
    # 封装send方法,get,post方法中返回值为self.request('GET', url, **kwargs)，后面调用只需要传入（“GET” or “POST”， url，**kwargs）即可
    def send(self, *args, **kwargs):
        return self.s.request(*args, **kwargs)