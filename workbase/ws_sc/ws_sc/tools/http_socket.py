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
    # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    # "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "Connection": "close",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.04",
    "Content-Type": "application/x-www-form-urlencoded",
    'accept-charset':'big5, big5-hkscs, cesu-8, euc-jp, euc-kr, gb18030, gb2312, gbk, ibm-thai, ibm00858, ibm01140, ibm01141, ibm01142, ibm01143, ibm01144, ibm01145, ibm01146, ibm01147, ibm01148, ibm01149, ibm037, ibm1026, ibm1047, ibm273, ibm277, ibm278, ibm280, ibm284, ibm285, ibm290, ibm297, ibm420, ibm424, ibm437, ibm500, ibm775, ibm850, ibm852, ibm855, ibm857, ibm860, ibm861, ibm862, ibm863, ibm864, ibm865, ibm866, ibm868, ibm869, ibm870, ibm871, ibm918, iso-2022-cn, iso-2022-jp, iso-2022-jp-2, iso-2022-kr, iso-8859-1, iso-8859-13, iso-8859-15, iso-8859-2, iso-8859-3, iso-8859-4, iso-8859-5, iso-8859-6, iso-8859-7, iso-8859-8, iso-8859-9, jis_x0201, jis_x0212-1990, koi8-r, koi8-u, shift_jis, tis-620, us-ascii, utf-16, utf-16be, utf-16le, utf-32, utf-32be, utf-32le, utf-8, windows-1250, windows-1251, windows-1252, windows-1253, windows-1254, windows-1255, windows-1256, windows-1257, windows-1258, windows-31j, x-big5-hkscs-2001, x-big5-solaris, x-compound_text, x-euc-jp-linux, x-euc-tw, x-eucjp-open, x-ibm1006, x-ibm1025, x-ibm1046, x-ibm1097, x-ibm1098, x-ibm1112, x-ibm1122, x-ibm1123, x-ibm1124, x-ibm1166, x-ibm1364, x-ibm1381, x-ibm1383, x-ibm300, x-ibm33722, x-ibm737, x-ibm833, x-ibm834, x-ibm856, x-ibm874, x-ibm875, x-ibm921, x-ibm922, x-ibm930, x-ibm933, x-ibm935, x-ibm937, x-ibm939, x-ibm942, x-ibm942c, x-ibm943, x-ibm943c, x-ibm948, x-ibm949, x-ibm949c, x-ibm950, x-ibm964, x-ibm970, x-iscii91, x-iso-2022-cn-cns, x-iso-2022-cn-gb, x-iso-8859-11, x-jis0208, x-jisautodetect, x-johab, x-macarabic, x-maccentraleurope, x-maccroatian, x-maccyrillic, x-macdingbat, x-macgreek, x-machebrew, x-maciceland, x-macroman, x-macromania, x-macsymbol, x-macthai, x-macturkish, x-macukraine, x-ms932_0213, x-ms950-hkscs, x-ms950-hkscs-xp, x-mswin-936, x-pck, x-sjis_0213, x-utf-16le-bom, x-utf-32be-bom, x-utf-32le-bom, x-windows-50220, x-windows-50221, x-windows-874, x-windows-949, x-windows-950, x-windows-iso2022jp',
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
                headers_str += "Cookie: %s\n" % cookies_str

            data_str = ""
            if proctocol == HTTP_PROCTOCOL:
                my_socket = socket(AF_INET, SOCK_STREAM)
            else:
                my_socket = wrap_socket(socket(AF_INET, SOCK_STREAM))
            content_length = 0
            if method == HTTP_METHOD_POST:
                data_str = self.__convert_data(data=data)
                content_length = len(data_str) if data_str else 0
            if content_length:
                self.request.headers.update({"Content-Length": content_length})
                headers_str += "Content-Length: %d\n" % content_length
            my_socket.settimeout(self._timeout)
            my_socket.connect((host, port))
            my_socket.settimeout(None)

            status_line = "{method} {m_url} {version}".format(method=method, m_url=m_url, version=self._http_version)
            send_msg = "{status}\n{headers}\r\n".format(status=status_line, headers=headers_str)
            if data_str:
                send_msg += data_str + "\r\n"
            print(send_msg)
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
                pass
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
    import time
    s = SocketUtil()
    # url = "http://www.freebuf.com/sectool/157443.html"
    # url = "http://www.json.cn/"
    # url = "https://tool.lu/js/"
    # url = "https://consumeprod.alipay.com/record/checkSecurity.htm?securityId=web%7Cconsumeprod_record_list%7C00cbc619-4cef-46e2-8df6-41ab6c04a352GZ00&consumeVersion=advanced"
    # res = s.http_get(url)
    url_conn = "https://v4.passport.sohu.com/i/jf/code?callback=passport403_cb%s&type=0&_=%s" % (int(time.time() * 1E3), int(time.time() * 1E3 + 1000))
    print(url_conn)
    res = s.http_get(url_conn, headers=DEFAULT_HEADERS)
    # # res = s.http_post(url, headers=DEFAULT_HEADERS, data={"name": "1212", "ss": "你好"})
    print(res.cookies)
    print(res.text)

