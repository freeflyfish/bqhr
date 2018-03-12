# coding:utf-8

from gzip import decompress
from io import BytesIO
from re import compile as re_compile
from socket import AF_INET, SOCK_STREAM, setdefaulttimeout, socket, timeout
from ssl import wrap_socket
from threading import local
from urllib.parse import quote, unquote
import zlib

SOCKET_TIMEOUT = 10
HTTP_METHOD_GET = "GET"
HTTP_METHOD_POST = "POST"
HTTP_PROCTOCOL = "http"
HTTPS_PROCTOCOL = "https"
HTTP_VERSION = "HTTP/1.1"
BUFF_MAX_SIZE = 1024
DEFAULT_HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    # "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "Connection": "close",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.04",
    'Referer':'https://mail.sohu.com/fe/'
}


class SocketUtil(local):
    """
    利用socket模拟http请求
    """

    def __init__(self, timeout=SOCKET_TIMEOUT, buff_max_size=BUFF_MAX_SIZE, http_version=HTTP_VERSION):
        self._timeout = timeout
        self._buff_max_size = buff_max_size
        self._http_version = http_version
        self.request = None
        self.response = None
        self.__max_redirect_times = 5
        self._count = 0

    def http_get(self, url, headers=None, cookies=None, allow_redirect=True):
        self.request = RequestObject(url, method=HTTP_METHOD_GET, headers=headers, cookies=cookies, data=None, allow_redirect=True)
        return self._do_request()

    def http_post(self, url, headers=None, cookies=None, data=None, allow_redirect=True):
        self.request = RequestObject(url, method=HTTP_METHOD_POST, headers=headers, cookies=cookies, data=data, allow_redirect=True)
        return self._do_request()

    def _do_request(self):
        try:
            # setdefaulttimeout(self._timeout)
            method = self.request.method
            host = self.request.host
            proctocol = self.request.proctocol
            port = self.request.port
            m_url = self.request.m_url
            data = self.request.data
            headers_str = self.__convert_headers(self.request.headers)
            cookies_str = self.__convert_cookies(self.request.cookies)
            if cookies_str:
                headers_str += "Cookie: " + cookies_str

            data_str = ""
            if proctocol == HTTP_PROCTOCOL:
                my_socket = socket(AF_INET, SOCK_STREAM)
            else:
                my_socket = wrap_socket(socket(AF_INET, SOCK_STREAM))
            if method == HTTP_METHOD_POST:
                data_str = self.__convert_data(data=data)
            my_socket.settimeout(self._timeout)
            my_socket.connect((host, port))
            my_socket.settimeout(None)

            status_line = "{method} {m_url} {version}".format(method=method, m_url=m_url, version=self._http_version)
            send_msg = "{status}\n{headers}\r\n".format(status=status_line, headers=headers_str)
            if data_str:
                send_msg += data_str + "\r\n"
            # print(send_msg)
            my_socket.send(send_msg.encode("utf-8"))

            raw_content = b""
            buf = my_socket.recv(self._buff_max_size)
            while len(buf):
                raw_content += buf
                buf = my_socket.recv(self._buff_max_size)
            my_socket.close()
            # print(raw_content)

            # 判断是否跳转
            allow_redirect = self.request.allow_redirect
            tmp_request = self.request
            response = ResponseObject(content=raw_content, request=tmp_request)
            while self._count < self.__max_redirect_times:
                location = response.location
                cookies = tmp_request.cookies
                cookies.update(response.cookies)
                cookies = None
                if location:
                    response = self.http_get(url=location, headers=tmp_request.headers, cookies=cookies, allow_redirect=allow_redirect)
                    self._count += 1
                else:
                    break
            self.response = response
            return response
        except timeout as e:
            print("请求超时:url:%s --> error:%s" % (self.request.url, str(e)))
            return None
        except Exception as e:
            print("请求出错:url:%s --> error:%s" % (self.request.url, str(e)))
            return None

    def __convert_headers(self, headers):
        headers_str = ""
        if not headers:
            headers = DEFAULT_HEADERS
        headers.update({"Host": self.request.host})
        self.request.headers = headers
        for key, val in headers.items():
            headers_str += "{key}: {val}\n".format(key=key, val=val)
        return headers_str

    def __convert_cookies(self, cookies):
        cookies_str = ""
        for key, val in cookies.items():
            cookies_str += "{key}={val}; ".format(key=key, val=val)
        return cookies_str.rstrip(";").rstrip(" ")

    def __convert_data(self, data):
        data_str = ""
        for key, val in data.items():
            data_str += '{key}={val}&'.format(key=self._url_encode(key), val=self._url_encode(val))
        return data_str.rstrip("&")

    def _url_encode(self, text, charset="utf-8"):
        if text is None:
            return ""
        if isinstance(text, str):
            text = text.encode(charset)
        return quote(text)


class RequestObject(object):
    """
    request对象
    """
    def __init__(self, url, method, headers, cookies, data, allow_redirect):
        self.url = url
        self.method = method if method else HTTP_METHOD_GET
        self.headers = headers if headers is not None else {}
        self.cookies = cookies if cookies is not None else {}
        self.data = data if data is not None else {}
        self.allow_redirect = allow_redirect

        self.__reg_url = re_compile('(https?)://([^/]+):?(\d{2,5})?(/.*)')

        self.proctocol, self.host, self.port, self.m_url = self.__parse_url()

    def __parse_url(self):
        self.url = self.url + "/" if not self.url.endswith("/") else self.url
        matchs = self.__reg_url.search(self.url)
        if matchs is not None:
            proctocol, host, port, m_url = matchs.groups()
            if port is None:
                if proctocol == "http":
                    port = 80
                else:
                    port = 443
            if m_url != "/":
                m_url = m_url.rstrip("/")
            return (proctocol, host, port, m_url)
        self.url = self.url.rstrip("/")


class ResponseObject(object):
    """
    response对象
    """
    def __init__(self, content, request):
        self.headers = {}
        self.cookies = {}
        self.encoding = "utf-8"
        self._raw_content = content
        self.text = None
        self.content = None
        self.status_code = 200
        self.location = None
        self.requset = request
        self.url = self.requset.url if self.requset else ""
        self.__split_char = b"\r\n\r\n"
        self.__split_sep = "\r\n"
        self.__reg_charset = re_compile('charset=(.+)')

        self.__parse_response()

    def __parse_response(self):
        index = self._raw_content.find(self.__split_char)
        if index:
            headers_str = self._raw_content[:index].decode()
            body_bytes = self._raw_content[index+4:]
            self.__parse_headers(headers_str)
            try:
                self.content = self._load_data(body_bytes)
                content_type = self.headers.get("Content-Type", "").lower()
                if content_type and self.__reg_charset.search(content_type) is not None:
                    self.encoding = self.__reg_charset.search(content_type).group(1)
                else:
                    self.encoding = "utf-8"
                try:
                    self.text = self.content.decode(self.encoding)
                except:
                    self.encoding = "gb18030"
                    self.text = self.content.decode(self.encoding)
            except Exception as e:
                print("解压缩失败:--> %s" % str(e))

    def __parse_headers(self, headers_str):
        tmp_headers = {}
        s_headers = headers_str.split(self.__split_sep)
        if len(s_headers) >= 1:
            status_line = s_headers[0]
            self.status_code = int(status_line.split(" ")[1])
            headers_lst = s_headers[1:]
            for item in headers_lst:
                if item.find("Set-Cookie") >= 0:
                    self.__parse_cookies(item)
                else:
                    header = {item.split(":", maxsplit=1)[0].strip(): item.split(":", maxsplit=1)[1].strip()}
                tmp_headers.update(header)
            self.headers = tmp_headers
        if self.status_code in [301, 302]:
            self.location = self.headers.get("Location")

    def __parse_cookies(self, cookies_str):
        cookies = cookies_str.split("Set-Cookie:")[1].strip()
        extr_field = ["path", "httponly", "domain", "expires"]
        temp_cookies = dict(kv.strip().split("=", 1) for kv in cookies.split(";") if "=" in kv
                      and kv.strip().split("=", 1)[0].lower() not in extr_field)
        self.cookies.update(temp_cookies)

    def _load_data(self, content):
        encoding = self.headers.get('Content-Encoding')
        if encoding == 'gzip':
            # 压缩后的数据长度，占三个字节，然后是 \r\n ，占两个字节
            content = content[content.find(b"\r\n") + 2:-7]
            content = self._gzip(content)
        elif encoding == 'deflate':
            content = content[5:]
            content = self._deflate(content)
        return content

    def _gzip(self, data):
        return decompress(data)

    def _deflate(self, data):
        try:
            return zlib.decompress(data, -zlib.MAX_WBITS)
        except zlib.error:
            return zlib.decompress(data)


if __name__ == '__main__':
    # url = "http://www.freebuf.com/sectool/157443.html"
    # url = "http://www.json.cn/"
    # url = "https://tool.lu/js/"
    # url = "https://consumeprod.alipay.com/record/checkSecurity.htm?securityId=web%7Cconsumeprod_record_list%7C00cbc619-4cef-46e2-8df6-41ab6c04a352GZ00&consumeVersion=advanced"
    # url = 'https://mail.sohu.com/fe/#/login'
    s = SocketUtil()
    url_login = 'https://v4.passport.sohu.com/i/login/101305'
    # res = s.http_get(url)
    data = {
        'userid': 'xiongtaozt@sohu.com',
        'password': '48f47223167479066fa329b6912fb2bd',
        'appid': '101305',
        'callback': 'passport403_cb1514538658106'
    }
    res = s.http_post(url_login, headers=DEFAULT_HEADERS, data=data)
    print(res.cookies)
    print(res.text is not None)
    print("xxxx")
