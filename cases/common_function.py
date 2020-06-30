import requests
import os
import allure


@allure.step("登陆")
def login(s, username='test', password='123456'):
    '''
    登陆个人信息
    :param s: s = requests.session()
    :param username: test
    :param password: 123456
    :return: s
    '''
    url = os.environ["host"]+'/api/v1/login/'
    body = {"username": username,
            "password": password}
    r = s.post(url=url, json=body)
    token = (r.json()['token'])
    print('\n' + token)
    h = {'Authorization': 'Token {}'.format(token)}
    s.headers.update(h)  # 后面请求不需要再传token
    return r.json()


@allure.step("注册")
def register(s, username='testadmin', password='testadmin', mail='123456@qq.com'):
    '''注册'''
    url = os.environ["host"]+'/api/v1/register'
    body = {'username': username,
            'password': password,
            'mail': mail}
    r = s.post(url, json=body)
    # print(r.text)
    # print(r.json())
    return r


class UserInfo(object):
    def __init__(self, s: requests.Session):
        self.s = s

    @allure.step("修改个人信息")
    def update_info(self, name='test', sex='M'):
        url = os.environ["host"]+'/api/v1/userinfo'
        # 修改个人信息
        body = {"name": name,
                "sex": sex,
                "age": 20,
                "mail": "123@qq.com"}
        r = self.s.post(url=url, json=body)
        print(r.json())
        return r.json()

    @allure.step("查询个人信息")
    def get_info(self):
        url = os.environ["host"]+'/api/v1/userinfo'
        # 查询
        r = self.s.get(url)
        return r.json()


if __name__ == '__main__':
    s = requests.session()
    login(s)                      # 登陆
    info = UserInfo(s)            # 实例化
    info.update_info()            # 修改个人信息
    info.get_info()               # 查询
