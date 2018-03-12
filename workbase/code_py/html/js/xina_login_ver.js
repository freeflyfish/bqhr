/**
 * Created by BQ0391 on 2017/12/19.
 */
(function () {
    if (!b) {
        var b = (function () {
            var h = {};
            var a = "theia";
            var k = [];
            var l = 200;
            var i;
            h[a] = {
                IE: /msie/i.test(navigator.userAgent), E: function (c) {
                    if (typeof c === "string") {
                        return document.getElementById(c)
                    } else {
                        return c
                    }
                }, C: function (d) {
                    var c;
                    d = d.toUpperCase();
                    if (d == "TEXT") {
                        c = document.createTextNode("")
                    } else {
                        if (d == "BUFFER") {
                            c = document.createDocumentFragment()
                        } else {
                            c = document.createElement(d)
                        }
                    }
                    return c
                }, log: function () {
                    var q, c = arguments, e = c.length, f = [].slice.apply(c, [0, e]), d = "error", g;
                    while (f[--e]) {
                        if (f[e] instanceof Error) {
                            q = f.splice(e, 1)[0];
                            break
                        }
                    }
                    if (!q) {
                        q = new Error();
                        d = "log"
                    }
                    g = [f, d, new Date().getTime(), q.message, q.stack];
                    if (i) {
                        try {
                            i.apply(null, g)
                        } catch (p) {
                        }
                    } else {
                        k.length >= l && k.shift();
                        k.push(g)
                    }
                }, _regLogFn: function (c) {
                    i = c
                }, _clearLogList: function () {
                    return k.splice(0, k.length)
                }
            };
            var j = h[a];
            j.register = function (c, g, d) {
                if (!d || typeof d != "string") {
                    d = a
                }
                if (!h[d]) {
                    h[d] = {}
                }
                var e = h[d];
                var r = c.split(".");
                var s = e;
                var f = null;
                while (f = r.shift()) {
                    if (r.length) {
                        if (s[f] === undefined) {
                            s[f] = {}
                        }
                        s = s[f]
                    } else {
                        if (s[f] === undefined) {
                            try {
                                if (d && d !== a) {
                                    if (c === "core.util.listener") {
                                        s[f] = h[a].core.util.listener;
                                        return true
                                    }
                                    if (c === "core.util.connect") {
                                        s[f] = h[a].core.util.connect;
                                        return true
                                    }
                                }
                                s[f] = g(e);
                                return true
                            } catch (q) {
                                setTimeout(function () {
                                    console.log(q)
                                }, 0)
                            }
                        }
                    }
                }
                return false
            };
            j.unRegister = function (d, e) {
                if (!e || typeof e != "string") {
                    e = a
                }
                var f = h[e];
                var o = d.split(".");
                var c = f;
                var g = null;
                while (g = o.shift()) {
                    if (o.length) {
                        if (c[g] === undefined) {
                            return false
                        }
                        c = c[g]
                    } else {
                        if (c[g] !== undefined) {
                            delete c[g];
                            return true
                        }
                    }
                }
                return false
            };
            j.regShort = function (d, c) {
                if (j[d] !== undefined) {
                    throw"[" + d + "] : short : has been register"
                }
                j[d] = c
            };
            j.shortRegister = function (c, g, d) {
                if (!d || typeof d != "string") {
                    d = a
                }
                var e = h[d];
                var p = c.split(".");
                if (!g) {
                    return false
                }
                if (e[g]) {
                    return false
                }
                var q = e;
                var f = null;
                while (f = p.shift()) {
                    if (p.length) {
                        if (q[f] === undefined) {
                            return false
                        }
                        q = q[f]
                    } else {
                        if (q[f] !== undefined) {
                            if (e[g]) {
                                return false
                            }
                            e[g] = q[f];
                            return true
                        }
                    }
                }
                return false
            };
            j.getPKG = function (c) {
                if (!c || typeof c != "string") {
                    c = a
                }
                return h[c]
            };
            return j
        })()
    }
    b.register("core.util.listener", function (a) {
        return (function () {
            var i = {};
            var h = [];
            var j;
            var g = function () {
                if (h.length == 0) {
                    return
                }
                clearTimeout(j);
                var d = h.splice(0, 1)[0];
                try {
                    d.func.apply(d.func, [].concat(d.data))
                } catch (c) {
                }
                j = setTimeout(g, 25)
            };
            return {
                register: function (e, c, d) {
                    i[e] = i[e] || {};
                    i[e][c] = i[e][c] || [];
                    i[e][c].push(d)
                }, fire: function (f, d, c) {
                    var e;
                    var n, o;
                    if (i[f] && i[f][d] && i[f][d].length > 0) {
                        e = i[f][d];
                        e.data_cache = c;
                        for (n = 0, o = e.length; n < o; n++) {
                            h.push({channel: f, evt: d, func: e[n], data: c})
                        }
                        g()
                    }
                }, remove: function (e, c, d) {
                    if (i[e]) {
                        if (i[e][c]) {
                            for (var f = 0, m = i[e][c].length; f < m; f++) {
                                if (i[e][c][f] === d) {
                                    i[e][c].splice(f, 1);
                                    break
                                }
                            }
                        }
                    }
                }, list: function () {
                    return i
                }, cache: function (d, c) {
                    if (i[d] && i[d][c]) {
                        return i[d][c].data_cache
                    }
                }
            }
        })()
    });
    b.register("core.obj.parseParam", function (a) {
        return function (j, k, l) {
            var i, h = {};
            k = k || {};
            for (i in j) {
                h[i] = j[i];
                if (k[i] != null) {
                    if (l) {
                        if (j.hasOwnProperty(i)) {
                            h[i] = k[i]
                        }
                    } else {
                        h[i] = k[i]
                    }
                }
            }
            return h
        }
    });
    b.register("core.dom.removeNode", function (a) {
        return function (f) {
            f = a.E(f) || f;
            try {
                f.parentNode.removeChild(f)
            } catch (e) {
            }
        }
    });
    b.register("core.util.getUniqueKey", function (e) {
        var a = (new Date()).getTime().toString(), f = 1;
        return function () {
            return a + (f++)
        }
    });
    b.register("core.func.empty", function () {
        return function () {
        }
    });
    b.register("core.str.parseURL", function (a) {
        return function (n) {
            var o = /^(?:([A-Za-z]+):(\/{0,3}))?([0-9.\-A-Za-z]+\.[0-9A-Za-z]+)?(?::(\d+))?(?:\/([^?#]*))?(?:\?([^#]*))?(?:#(.*))?$/;
            var i = ["url", "scheme", "slash", "host", "port", "path", "query", "hash"];
            var l = o.exec(n);
            var k = {};
            for (var m = 0, p = i.length; m < p; m += 1) {
                k[i[m]] = l[m] || ""
            }
            return k
        }
    });
    b.register("core.arr.isArray", function (a) {
        return function (d) {
            return Object.prototype.toString.call(d) === "[object Array]"
        }
    });
    b.register("core.str.trim", function (a) {
        return function (g) {
            if (typeof g !== "string") {
                throw"trim need a string as parameter"
            }
            var j = g.length;
            var h = 0;
            var i = /(\u3000|\s|\t|\u00A0)/;
            while (h < j) {
                if (!i.test(g.charAt(h))) {
                    break
                }
                h += 1
            }
            while (j > h) {
                if (!i.test(g.charAt(j - 1))) {
                    break
                }
                j -= 1
            }
            return g.slice(h, j)
        }
    });
    b.register("core.json.queryToJson", function (a) {
        return function (t, p) {
            var n = a.core.str.trim(t).split("&");
            var o = {};
            var u = function (c) {
                if (p) {
                    return decodeURIComponent(c)
                } else {
                    return c
                }
            };
            for (var r = 0, q = n.length; r < q; r++) {
                if (n[r]) {
                    var s = n[r].split("=");
                    var v = s[0];
                    var i = s[1];
                    if (s.length < 2) {
                        i = v;
                        v = "$nullName"
                    }
                    if (!o[v]) {
                        o[v] = u(i)
                    } else {
                        if (a.core.arr.isArray(o[v]) != true) {
                            o[v] = [o[v]]
                        }
                        o[v].push(u(i))
                    }
                }
            }
            return o
        }
    });
    b.register("core.json.jsonToQuery", function (a) {
        var d = function (c, f) {
            c = c == null ? "" : c;
            c = a.core.str.trim(c.toString());
            if (f) {
                return encodeURIComponent(c)
            }
            return c
        };
        return function (i, l) {
            var c = [];
            if (typeof i == "object") {
                for (var m in i) {
                    if (m === "$nullName") {
                        c = c.concat(i[m]);
                        continue
                    }
                    if (i[m] instanceof Array) {
                        for (var k = 0, n = i[m].length; k < n; k++) {
                            c.push(m + "=" + d(i[m][k], l))
                        }
                    } else {
                        if (typeof i[m] != "function") {
                            c.push(m + "=" + d(i[m], l))
                        }
                    }
                }
            }
            if (c.length) {
                return c.join("&")
            }
            return ""
        }
    });
    b.register("core.util.URL", function (a) {
        return function (l, o) {
            var m = a.core.obj.parseParam({isEncodeQuery: false, isEncodeHash: false}, o || {});
            var n = {};
            var j = a.core.str.parseURL(l);
            var p = a.core.json.queryToJson(j.query);
            var k = a.core.json.queryToJson(j.hash);
            n.setParam = function (d, c) {
                p[d] = c;
                return this
            };
            n.getParam = function (c) {
                return p[c]
            };
            n.setParams = function (c) {
                for (var d in c) {
                    n.setParam(d, c[d])
                }
                return this
            };
            n.setHash = function (d, c) {
                k[d] = c;
                return this
            };
            n.getHash = function (c) {
                return k[c]
            };
            n.valueOf = n.toString = function () {
                var e = [];
                var d = a.core.json.jsonToQuery(p, m.isEncodeQuery);
                var c = a.core.json.jsonToQuery(k, m.isEncodeQuery);
                if (j.scheme != "") {
                    e.push(j.scheme + ":");
                    e.push(j.slash)
                }
                if (j.host != "") {
                    e.push(j.host);
                    if (j.port != "") {
                        e.push(":");
                        e.push(j.port)
                    }
                }
                e.push("/");
                e.push(j.path);
                if (d != "") {
                    e.push("?" + d)
                }
                if (c != "") {
                    e.push("#" + c)
                }
                return e.join("")
            };
            return n
        }
    });
    b.register("core.io.scriptLoader", function (f) {
        var e = {};
        var a = {
            url: "",
            charset: "UTF-8",
            timeout: 30 * 1000,
            args: {},
            onComplete: f.core.func.empty,
            onTimeout: f.core.func.empty,
            isEncode: false,
            uniqueID: null
        };
        return function (c) {
            var j, l;
            var k = f.core.obj.parseParam(a, c);
            if (k.url == "") {
                throw"scriptLoader: url is null"
            }
            var d = k.uniqueID || f.core.util.getUniqueKey();
            j = e[d];
            if (j != null && f.IE != true) {
                f.core.dom.removeNode(j);
                j = null
            }
            if (j == null) {
                j = e[d] = f.C("script")
            }
            j.charset = k.charset;
            j.id = "scriptRequest_script_" + d;
            j.type = "text/javascript";
            if (k.onComplete != null) {
                if (f.IE) {
                    j.onreadystatechange = function () {
                        if (j.readyState.toLowerCase() == "loaded" || j.readyState.toLowerCase() == "complete") {
                            try {
                                clearTimeout(l);
                                document.getElementsByTagName("head")[0].removeChild(j);
                                j.onreadystatechange = null
                            } catch (g) {
                            }
                            k.onComplete()
                        }
                    }
                } else {
                    j.onload = function () {
                        try {
                            clearTimeout(l);
                            f.core.dom.removeNode(j)
                        } catch (g) {
                        }
                        k.onComplete()
                    }
                }
            }
            j.src = f.core.util.URL(k.url, {isEncodeQuery: k.isEncode}).setParams(k.args).toString();
            document.getElementsByTagName("head")[0].appendChild(j);
            if (k.timeout > 0) {
                l = setTimeout(function () {
                    try {
                        document.getElementsByTagName("head")[0].removeChild(j)
                    } catch (g) {
                    }
                    k.onTimeout()
                }, k.timeout)
            }
            return j
        }
    });
    b.register("core.io.jsonp", function (a) {
        return function (j) {
            var l = a.core.obj.parseParam({
                url: "",
                charset: "UTF-8",
                timeout: 30 * 1000,
                args: {},
                onComplete: null,
                onTimeout: null,
                responseName: null,
                isEncode: false,
                varkey: "callback"
            }, j);
            var i = -1;
            var k = l.responseName || ("STK_" + a.core.util.getUniqueKey());
            l.args[l.varkey] = k;
            var n = l.onComplete;
            var m = l.onTimeout;
            window[k] = function (c) {
                if (i != 2 && n != null) {
                    i = 1;
                    n(c)
                }
            };
            l.onComplete = null;
            l.onTimeout = function () {
                if (i != 1 && m != null) {
                    i = 2;
                    m()
                }
            };
            return a.core.io.scriptLoader(l)
        }
    });
    b.register("common.listener", function (f) {
        var e = {};
        var a = {};
        a.define = function (d, c) {
            if (e[d] != null) {
                throw"common.listener.define: 棰戦亾宸茶鍗犵敤"
            }
            e[d] = c;
            var h = {};
            h.register = function (g, j) {
                if (e[d] == null) {
                    throw"common.listener.define: 棰戦亾鏈畾涔�"
                }
                f.core.util.listener.register(d, g, j)
            };
            h.fire = function (j, g) {
                if (e[d] == null) {
                    throw"commonlistener.define: 棰戦亾鏈畾涔�"
                }
                f.core.util.listener.fire(d, j, g)
            };
            h.remove = function (g, j) {
                f.core.util.listener.remove(d, g, j)
            };
            return h
        };
        return a
    });
    b.register("common.channel.qrcode_login", function (a) {
        return a.common.listener.define("common.channel.qrcode_login", ["qrcode_scanned", "qrcode_used", "qrcode_timeout", "qrcode_exception", "login_failure", "login_success"])
    });
    b.register("jobs.qrcode_login", function (v) {
        var s = {}, A = v.common.channel.qrcode_login;
        var a = {
            entry: "sso",
            domain: "weibo.com",
            get_image_timeout: 10 * 1000,
            check_request_timeout: 10 * 1000,
            qrcode_size: 180,
            crossdomain_timeout: 3 * 1000,
            savestate: 30
        };
        var z = {
            qrcode_image: "https://login.sina.com.cn/sso/qrcode/image",
            qrcode_check: "https://login.sina.com.cn/sso/qrcode/check",
            qrcode_login: "https://login.sina.com.cn/sso/login.php"
        };
        var u, p = 0, x = 3000;
        var q;
        s.set = function (c) {
            for (var d in c) {
                a[d] = c[d]
            }
            return s
        };
        s.getQRcode = function (c) {
            return w(function (d) {
                c(d)
            })
        };
        s.getQRcodeId = function () {
            return u
        };
        s.start = function () {
            q = false;
            p++;
            t(p)
        };
        s.cancel = function () {
            q = true
        };
        s.register = function (c, d) {
            A.register(c, d);
            return s
        };
        s.remove = function (c, d) {
            A.remove(c, d);
            return s
        };
        var w = function (c) {
            v.core.io.jsonp({
                url: z.qrcode_image,
                timeout: a.get_image_timeout,
                args: {entry: a.entry, size: a.qrcode_size},
                onComplete: function (e) {
                    if (!e || e.retcode != 20000000) {
                        c(e);
                        return
                    }
                    var d = e.data;
                    if (d.interval) {
                        x = d.interval
                    }
                    u = d.qrid;
                    c(e)
                },
                onTimeout: function () {
                    A.fire("get_image_timeout")
                },
                isEncode: true,
                varkey: "callback"
            });
            return s
        };
        var t = function (c) {
            var d = function (e) {
                if (e.retcode == 20000000) {
                    r(e)
                } else {
                    if (e.retcode == 50114002) {
                        A.fire("qrcode_scanned", [e])
                    } else {
                        if (e.retcode == 50114003) {
                            A.fire("qrcode_timeout", [e])
                        } else {
                            if (e.retcode == 50114004) {
                                A.fire("qrcode_used", [e])
                            } else {
                                if (e.retcode == 50114015) {
                                    A.fire("qrcode_exception", [e])
                                } else {
                                }
                            }
                        }
                    }
                }
                if (e.retcode == 50114001 || e.retcode == 50114002) {
                    setTimeout(function () {
                        if (c < p) {
                            return
                        }
                        if (q) {
                            return
                        }
                        y(d)
                    }, x)
                }
            };
            y(d)
        };
        var y = function (c) {
            v.core.io.jsonp({
                url: z.qrcode_check,
                timeout: a.check_request_timeout,
                args: {entry: a.entry, qrid: u},
                onComplete: function (d) {
                    if (!d) {
                        c({retcode: -1});
                        return
                    }
                    c(d)
                },
                onTimeout: function () {
                    A.fire("check_timeout")
                },
                isEncode: true,
                varkey: "callback"
            })
        };
        var r = function (c) {
            v.core.io.jsonp({
                url: z.qrcode_login,
                timeout: a.login_request_timeout,
                args: {
                    entry: a.entry,
                    returntype: "TEXT",
                    crossdomain: 1,
                    cdult: 3,
                    domain: a.domain,
                    alt: c.data.alt,
                    savestate: a.savestate
                },
                onComplete: function (d) {
                    if (d.retcode != 0) {
                        A.fire("login_failure", {retcode: d.retcode, msg: d.reason})
                    } else {
                        B(d, function (e) {
                            if (e.result === false) {
                                A.fire("login_failure", {retcode: -2, msg: "鐧诲綍澶辫触"})
                            } else {
                                A.fire("login_success", d)
                            }
                        })
                    }
                },
                onTimeout: function () {
                    A.fire("login_failure", {retcode: -1, msg: "鐧诲綍瓒呮椂"})
                },
                isEncode: true,
                varkey: "callback"
            })
        };
        var B = function (e, c) {
            var h = e.crossDomainUrlList.length;
            if (h == 0) {
                c({result: true});
                return
            }
            var d = setTimeout(function () {
                h = -1;
                c({result: false})
            }, a.crossdomain_timeout);
            for (var g in e.crossDomainUrlList) {
                var f = v.core.str.parseURL(e.crossDomainUrlList[g]);
                if (f.host == "weibo.com") {
                    v.core.io.scriptLoader({
                        url: e.crossDomainUrlList[g],
                        charset: "UTF-8",
                        args: {action: "login"},
                        onComplete: function () {
                            h--;
                            if (h == 0) {
                                clearTimeout(d);
                                c({result: true})
                            }
                        }
                    })
                } else {
                    v.core.io.jsonp({
                        url: e.crossDomainUrlList[g],
                        charset: "UTF-8",
                        args: {action: "login"},
                        onComplete: function () {
                            h--;
                            if (h == 0) {
                                clearTimeout(d);
                                c({result: true})
                            }
                        }
                    })
                }
            }
        };
        return s
    });
    (function (d) {
        var a = d.jobs.qrcode_login;
        a.getVersion = function () {
            return "qrcode_login.js(v1.0.1) 2017-7-10"
        };
        a.STK = d;
        this.SINA_QRCODE_LOGIN = a
    }).call(this, b)
}).call(this);
function InputSuggest(a) {
    this.win = null;
    this.doc = null;
    this.container = null;
    this.input = a.input || null;
    this.containerCls = a.containerCls || "suggest-container";
    this.itemCls = a.itemCls || "suggest-item";
    this.activeCls = a.activeCls || "suggest-active";
    this.width = a.width;
    this.data = a.data || [];
    this.active = null;
    this.visible = false;
    this.init()
}
InputSuggest.prototype = {
    init: function () {
        this.win = window;
        this.doc = window.document;
        this.container = this.$C("div");
        this.attr(this.container, "class", this.containerCls);
        this.doc.body.appendChild(this.container);
        this.setPos();
        var b = this, a = this.input;
        a.onkeyup = function (d) {
            d = d || window.event;
            if (a.value == "") {
                b.hide()
            } else {
                if (/^\d{11}$/.test(a.value)) {
                    if (d.keyCode == 13) {
                        b.hide();
                        try {
                            var c = document.getElementsByTagName("input")[1];
                            c.focus()
                        } catch (d) {
                        }
                    } else {
                        b.onKeyup(d)
                    }
                } else {
                    b.onKeyup(d)
                }
            }
        };
        a.onblur = function (c) {
            b.hide()
        };
        this.onMouseover();
        this.onMousedown()
    }, $C: function (a) {
        return this.doc.createElement(a)
    }, getPos: function (a) {
        var c = [0, 0];
        if (a.getBoundingClientRect) {
            var b = a.getBoundingClientRect();
            c = [b.left, b.top]
        }
        return c
    }, setPos: function () {
        var c = this.input, e = this.getPos(c), b = this.brow, d = this.width, a = this.container;
        a.style.cssText = "position:absolute;overflow:hidden;left:" + e[0] + "px;top:" + (e[1] + c.offsetHeight) + "px;width:" + ($B.firefox ? c.clientWidth : c.offsetWidth - 2) + "px;";
        if (d) {
            a.style.width = d + "px"
        }
    }, show: function () {
        this.container.style.display = "block";
        this.visible = true
    }, hide: function () {
        this.container.style.display = "none";
        this.visible = false
    }, attr: function (b, a, c) {
        if (c === undefined) {
            return b.getAttribute(a)
        } else {
            b.setAttribute(a, c);
            a == "class" && (b.className = c)
        }
    }, onKeyup: function (j) {
        var c = [], a = this.container, m = this.input, d = m.value.trim(), k = this.itemCls, l = this.activeCls;
        if (d == "") {
            return
        }
        if (this.visible) {
            switch (j.keyCode) {
                case 13:
                    if (this.active) {
                        m.value = this.active.firstChild.data;
                        this.hide();
                        try {
                            var b = document.getElementsByTagName("input")[1];
                            b.focus()
                        } catch (j) {
                        }
                    }
                    return;
                case 38:
                    if (this.active == null) {
                        this.active = a.lastChild;
                        this.attr(this.active, "class", l);
                        m.value = this.active.firstChild.data
                    } else {
                        if (this.active.previousSibling != null) {
                            this.attr(this.active, "class", k);
                            this.active = this.active.previousSibling;
                            this.attr(this.active, "class", l);
                            m.value = this.active.firstChild.data
                        } else {
                            this.attr(this.active, "class", k);
                            this.active = null;
                            m.focus();
                            m.value = m.getAttribute("curr_val")
                        }
                    }
                    return;
                case 40:
                    if (this.active == null) {
                        this.active = a.firstChild;
                        this.attr(this.active, "class", l);
                        m.value = this.active.firstChild.data
                    } else {
                        if (this.active.nextSibling != null) {
                            this.attr(this.active, "class", k);
                            this.active = this.active.nextSibling;
                            this.attr(this.active, "class", l);
                            m.value = this.active.firstChild.data
                        } else {
                            this.attr(this.active, "class", k);
                            this.active = null;
                            m.focus();
                            m.value = m.getAttribute("curr_val")
                        }
                    }
                    return
            }
        }
        if (j.keyCode == 27) {
            this.hide();
            m.value = this.attr(m, "curr_val");
            return
        }
        if (this.attr(m, "curr_val") != m.value) {
            this.container.innerHTML = "";
            var h = [];
            if (d.indexOf("@") != -1) {
                h = m.value.split("@");
                for (var f = 0, g = this.data.length; f < g; f++) {
                    if (this.startsWith(this.data[f], h[1])) {
                        c.push(this.data[f])
                    }
                }
            }
            c = c.length >= 1 ? c : this.data;
            for (var f = 0; f < c.length; f++) {
                this.createItem(h[0] || d, c[f])
            }
            this.attr(m, "curr_val", d);
            this.active = this.container.firstChild;
            this.attr(this.active, "class", l)
        }
        this.show()
    }, startsWith: function (b, a) {
        return b.lastIndexOf(a, 0) == 0
    }, createItem: function (d, c) {
        c = c || "";
        var a = d.indexOf("@") != -1;
        var b = this.$C("div");
        this.attr(b, "class", this.itemCls);
        b.innerHTML = d.replace(/[&"'><]/g, function (e) {
                return {"&": "&amp;", ">": "&gt;", "<": "&lt;", '"': "&quot;", "'": "&#39;"}[e]
            }) + (a ? "" : "@") + c;
        this.container.appendChild(b)
    }, onMouseover: function () {
        var b = this, a = this.itemCls, c = this.activeCls;
        this.container.onmouseover = function (f) {
            f = f || window.event;
            var d = f.target || f.srcElement || document;
            if (d.className == a) {
                if (b.active) {
                    b.active.className = a
                }
                d.className = c;
                b.active = d
            }
        }
    }, onMousedown: function () {
        var a = this;
        this.container.onmousedown = function (b) {
            b = b || window.event;
            if (!b.target) {
                b.target = b.srcElement || document
            }
            a.input.value = a.active.firstChild.data;
            a.hide()
        }
    }
};
var $B = function (e) {
    var a = {
        msie: /msie/.test(e) && !/opera/.test(e),
        opera: /opera/.test(e),
        safari: /webkit/.test(e) && !/chrome/.test(e),
        firefox: /firefox/.test(e),
        chrome: /chrome/.test(e),
        maxthon: /maxthon/.test(e),
        sogou: /se/.test(e),
        tt: /TencentTraveler/.test(e)
    };
    var f = "", c;
    for (var d in a) {
        if (a[d]) {
            f = "safari" == d ? "version" : d;
            break
        }
    }
    a.version = f && RegExp("(?:" + f + ")[\\/: ]([\\d.]+)").test(e) ? RegExp.$1 : "0";
    a.ie = a.msie;
    c = parseInt(a.version, 10);
    a.ie6 = a.msie && c == 6;
    a.ie7 = a.msie && c == 7;
    a.ie8 = a.msie && c == 8;
    a.ie9 = a.msie && c == 9;
    return a
}(navigator.userAgent.toLowerCase());
using(["r/core"], function (X) {
    var av = X.global, L = av.document, ae = X.dom, af = X.event, am = ae.query, ap = ae.$, g, f, e;
    var u = am(".mailLogin"), i = am(".loginBox"), aj = am(".loginBox_code");
    var O = !am(".productName") ? 1 : 0;
    var U = X.util.cookie("pname") ? 1 : 0;
    var n = [];
    var S = "@sina.cn", ad = "@sina.com", T = "2008.sina.com";
    var W, j = false, z = false, al = (location.protocol == "https:") ? "" : "http://i0.sinaimg.cn/rny/webface/2012login/", q = (function () {
        var d = location.href, E = X.string.params(d.split("?")[1]);
        return location.protocol + "//" + location.host + "/cgi-bin/sla.php?" + (E && E.rt ? ("rt=" + encodeURIComponent(E.rt) + "&a=") : "a=")
    })();
    if (O) {
        var m = am(".freeMailbox");
        var F = am(".username", m), au = am(".password", m), aC = am(".checkcodeBox", m), ax = am("img", aC), r = am("a", aC), Q = am("input", aC), ag = am("img", aC), ao = am(".clearname", m)
    }
    var x = am(".vipMailbox");
    var J = am(".username", x), v = am(".password", x), aq = am(".checkcodeBox", x), aa = am("input", aq), Y = am("img", aq), p = am("a", aq), at = am(".mailvsn", x), ab = am("input", at), aA = am(".clearname", x);
    var C = am(".supportBtn"), k = am(".supportBox"), az = am(".favorites"), H = am(".viploginbg");
    if (H) {
        var N = am("img", am(".viploginbg")), an = new Image(), l, s, M
    }
    SINA_QRCODE_LOGIN.set({entry: "cnmail", domain: "sina.com"});
    function aw(R) {
        var d = "";
        for (var E = 0; E < R.length; E++) {
            if (R.charCodeAt(E) == 12288) {
                d += String.fromCharCode(R.charCodeAt(E) - 12256);
                continue
            }
            if (R.charCodeAt(E) > 65280 && R.charCodeAt(E) < 65375) {
                d += String.fromCharCode(R.charCodeAt(E) - 65248)
            } else {
                d += String.fromCharCode(R.charCodeAt(E))
            }
        }
        return d
    }

    function P(aD, E) {
        var d = am(".tip" + E);

        function R(aG) {
            for (var aF = 0, aE = aG.length; aF < aE; aF++) {
                if (aG.charCodeAt(aF) <= 255) {
                    continue
                } else {
                    return true
                }
            }
            return false
        }

        if (E == "32") {
            if (aD == "") {
                ae.show(d, 0);
                return false
            } else {
                ae.hide(d, 0);
                return true
            }
        }
        if (aD == "" || aD == "输入邮箱名/手机号" || aD == "@vip.sina.com") {
            d.innerHTML = "请输入邮箱名";
            ae.show(d, 0);
            return false
        }
        if (R(aD)) {
            d.innerHTML = "邮箱名不支持中文";
            ae.show(d, 0);
            return false
        }
        if (!/^\d{11}$/.test(aD) && !/^\w([.!#$%&\'*+\-\/=?^_`{|}~\w]{0,62})?@(\w([!#$%&\'*+\-\/=?^_`{|}~\w]{0,62}\w)?\.){1,7}\w([!#$%&\'*+\-\/=?^_`{|}~\w]){0,62}\w$/.test(aD) || aD.length > 70) {
            d.innerHTML = "您输入的邮箱名格式不正确";
            ae.show(d, 0);
            return false
        }
        ae.hide(d, 0);
        return true
    }

    function w(E, d) {
        if (E == "") {
            ae.show(am(".tip" + d), 0);
            return false
        }
        return true
    }

    function ac(aE, R) {
        var aD = aE.keyCode ? aE.keyCode : aE.which, d = aE.shiftKey ? aE.shiftKey : ((aD == 16) ? true : false), E = am(".tip" + R);
        if (((aD >= 65 && aD <= 90) && !d) || ((aD >= 97 && aD <= 122) && d)) {
            E.innerHTML = "大写键已开启";
            ae.show(E, 0)
        } else {
            ae.hide(E, 0)
        }
    }

    function D() {
        try {
            function aE(aG) {
                var aH = Math.round(Math.random() * (aG.length - 1));
                return aG[aH]
            }

            var aD = aE(X.confdata.bgdata), R = aD.infoHtml, aF = "";
            if (aD.img) {
                ae.css(am(".mainBox"), "background", "url(" + aD.img + ") repeat-x left top " + aD.bgcolor)
            }
            if (aD.borderbg) {
                ae.css(am(".main"), "background", aD.borderbg == "none" ? "none" : "url(" + aD.borderbg + ") no-repeat center center")
            }
            if (aD.link) {
                ae.addClass(am(".mainBox"), "activity");
                af.on(am(".main"), "click", function (aH) {
                    var aH = aH || av.event, aG = aH.target || aH.srcElement;
                    if (!ae.contains(am(".loginBox"), aG)) {
                        av.open(aD.link)
                    }
                })
            }
            if (R) {
                var d = L.createElement("div");
                d.innerHTML = R;
                am(".positionBox").insertBefore(d.firstChild, am(".loginBox"));
                d = null
            }
            ae.css(am(".bg1"), "backgroundColor", aD.bgcolor)
        } catch (E) {
        }
    }

    function b() {
        try {
            function aD(aG) {
                var aH = Math.round(Math.random() * (aG.length - 1));
                return aG[aH]
            }

            var R = aD(X.confdata.bgdata), E = R.infoHtml, aF = "";
            N.style.width = 0;
            var aE = al + "images/" + R.img;
            af.on(an, "load", function () {
                l = an.width;
                s = an.height;
                N.style.display = "none";
                N.src = aE
            });
            an.src = aE
        } catch (d) {
        }
    }

    function I(aD) {
        if (O) {
            ae.css(am(".main"), "background", "url(" + al + "images/2012_error.jpg) no-repeat scroll center center #FFF")
        }
        var E = am(".error");
        for (var R = 0, d = E.length; R < d; R++) {
            ae.hide(E[R], 0)
        }
        var aE = am("." + aD);
        if (aE) {
            ae.show(aE, 0);
            if (aD == "addfavorite") {
                setTimeout(function () {
                    am(".addfavorite").style.display = "none"
                }, 3000)
            }
        } else {
            ae.show(am(".timeout"), 0)
        }
    }

    function ah() {
        var d = am(".mid")[0];
        var E = ae.create("iframe", {
            scrolling: "no",
            frameborder: "0",
            marginheight: "0",
            marginwidth: "0",
            src: "http://mail.sina.com.cn/ad/logout_taobao.html"
        }, {
            position: "absolute",
            top: "40px",
            width: "601px",
            height: "373px",
            "border-width": "0px",
            overflow: "hidden"
        });
        d.appendChild(E);
        ae.css(am(".login_main", d), "left", "602px")
    }

    function V(d) {
        d.src = sinaSSOController.getPinCodeUrl()
    }

    function y(R) {
        var E = am(".bgHeight"), d = i.clientHeight;
        if (!R) {
            return (E.clientHeight - 54 - 65 - d) / 2
        } else {
            return (500 - 54 - 65 - d) / 2
        }
    }

    var B = function (E) {
        var d = E.target;
        if (d.value == "") {
            ae.show(am(".placeholder", d.parentNode))
        } else {
            ae.hide(am(".placeholder", d.parentNode))
        }
        if (d == F) {
            ae[d.value ? "show" : "hide"](ao)
        } else {
            if (d == J) {
                if (!d.getAttribute("data-prevent")) {
                    ae[d.value ? "show" : "hide"](aA);
                    if (ae.isVisible(at)) {
                        if ((E.type == "propertychange" && E.propertyName == "value") || E.type == "input") {
                            ae.hide(at)
                        }
                    }
                }
            }
        }
    };
    var G = function (aE) {
        var aD = aE.target;
        if (!ae.hasClass(aD.parentNode, "focus")) {
            var d = am(".focus", i, true), E = d.length;
            for (var R = E; R > 0; R--) {
                ae.removeClass(d[R - 1], "focus")
            }
            ae.removeClass(aD, "hover");
            ae.addClass(aD.parentNode, "focus");
            B(aE)
        }
    };
    var h = function () {
        var aE = am(".bgHeight");
        if (s == 0 || l == 0) {
            return
        }
        var aG = Math.min(L.body.clientWidth, L.documentElement.clientWidth), aD = Math.min(L.body.clientHeight, L.documentElement.clientHeight);
        var aF, aI, R = 0, aH = 0;
        var E = l / aG;
        var d = s / aD;
        if (aD <= 500 && aG <= 950) {
            aE.style.width = "950px";
            aE.style.height = "500px";
            E = l / 950;
            d = s / 500;
            if (E > d) {
                aF = "500px";
                aI = "auto";
                R = (950 - Math.round((l / s) * aF)) / 2;
                aH = 0
            } else {
                aI = "950px";
                aF = "auto";
                R = 0;
                aH = (500 - Math.round((s / l) * parseFloat(aI))) / 2
            }
        } else {
            if (aD <= 500) {
                aE.style.width = "100%";
                aE.style.height = "500px";
                E = l / aG;
                d = s / 500;
                if (E > d) {
                    aF = "500px";
                    aI = "auto";
                    R = (aG - Math.round((l / s) * parseFloat(aF))) / 2;
                    aH = 0
                } else {
                    aI = aG + "px";
                    aF = "auto";
                    aH = (500 - Math.round((s / l) * parseFloat(aI))) / 2;
                    R = 0
                }
            } else {
                if (aG <= 950) {
                    aE.style.width = "950px";
                    aE.style.height = "100%";
                    E = l / 950;
                    d = s / aD;
                    if (E > d) {
                        aF = aD + "px";
                        aI = "auto";
                        R = (950 - Math.round((l / s) * parseFloat(aF))) / 2;
                        aH = 0
                    } else {
                        aI = "950px";
                        aF = "auto";
                        aH = (aD - Math.round((s / l) * parseFloat(aI))) / 2;
                        R = 0
                    }
                } else {
                    if (E > d) {
                        aF = aD + "px";
                        aI = "auto";
                        R = (aG - Math.round((l / s) * parseFloat(aF))) / 2;
                        aH = 0
                    } else {
                        aI = aG + "px";
                        aF = "auto";
                        aH = (aD - Math.round((s / l) * parseFloat(aI))) / 2;
                        R = 0
                    }
                    aE.style.width = "100%";
                    aE.style.height = "100%"
                }
            }
        }
        ae.css(N, "width", aI);
        ae.css(N, "height", aF);
        if (R) {
            N.style.marginLeft = R + "px";
            N.style.marginTop = 0 + "px"
        } else {
            N.style.marginLeft = 0;
            N.style.marginTop = aH + "px"
        }
        N.style.display = ""
    };
    var aB = function () {
        var E;
        var d = Math.max(L.body.clientWidth, L.documentElement.clientWidth), R = Math.max(L.body.clientHeight, L.documentElement.clientHeight);
        if (R <= 500 && d <= 950) {
            E = y(1)
        } else {
            if (R <= 500) {
                E = y(1)
            } else {
                if (d <= 950) {
                    E = y()
                } else {
                    E = y()
                }
            }
        }
        if (E != parseFloat(i.style.marginTop)) {
            i.style.marginTop = i.style.marginBottom = E + "px"
        }
    };
    if (O) {
        var ai = am("li", am(".tit"));

        function ar() {
            conf.isVip = true;
            ai[0].className = "";
            ai[1].className = "current";
            ae.show(x, 0);
            ae.hide(m, 0);
            if (J.value != (X.util.cookie("vipName") || "")) {
                J.value = X.util.cookie("vipName") || ""
            }
            J.focus()
        }

        function A() {
            conf.isVip = false;
            ai[0].className = "current";
            ai[1].className = "";
            ae.show(m, 0);
            ae.hide(x, 0);
            F.focus()
        }

        if (U) {
            ar();
            if (J.value) {
                ae.hide(am(".placeholder", J.parentNode));
                v.focus()
            }
        } else {
            A()
        }
        af.on(am(".tit"), "click", function (R) {
            var E = R.target;
            var d = am("li", am(".tit"));
            if (d[0].className == "" && ae.contains(d[0], E)) {
                A();
                if (F.value) {
                    au.focus()
                }
                X.util.cookie("pname", "", 100)
            }
            if (d[1].className == "" && ae.contains(d[1], E)) {
                ar();
                if (J.value) {
                    v.focus()
                }
                X.util.cookie("pname", "1", 100)
            }
        });
        af.on(am(".tit_code"), "click", function (R) {
            var E = R.target;
            var d = am("li", am(".tit_code"));
            if (d[0].className == "" && ae.contains(d[0], E)) {
                ay();
                d[0].className = "current";
                d[1].className = "";
                ae.hide(am(".weixin_login"));
                ae.show(am(".weibo_login"))
            }
            if (d[1].className == "" && ae.contains(d[1], E)) {
                Z();
                d[0].className = "";
                d[1].className = "current";
                ae.hide(am(".weibo_login"));
                ae.show(am(".weixin_login"))
            }
        });
        af.on(F, "focus", G);
        af.on(au, "focus", G);
        af.on(Q, "focus", G);
        if ($B.ie6 || $B.ie7 || $B.ie8) {
            af.on(F, "propertychange", B);
            af.on(au, "propertychange", B);
            af.on(Q, "propertychange", B)
        } else {
            af.on(F, "input", B);
            af.on(au, "input", B);
            af.on(Q, "input", B)
        }
        var ak = function (d) {
            if (d.value) {
                ae.hide(am(".placeholder", d.parentNode))
            } else {
                ae.show(am(".placeholder", d.parentNode))
            }
        };
        var K = L.getElementById("vippassword");
        setInterval(function () {
            ak(F);
            ak(au);
            ak(J);
            ak(K)
        }, 50);
        af.on(ao, "click", function (d) {
            X.util.cookie("freeName", "");
            F.value = "";
            F.focus();
            ae.hide(ao);
            ae.show(am(".placeholder", F.parentNode))
        });
        af.on(F, "keypress", function (d) {
            if (/^\d{1, 11}$/.test(F.value) || W) {
                return
            }
            W = true;
            W = new InputSuggest({
                input: F,
                activeCls: "active",
                containerCls: "autocomplete",
                data: ["sina.com", "sina.cn", "2008.sina.com", "51uc.com"]
            })
        });
        af.on(au, "focus", function (d) {
            if (F.value && !X.util.cookie("freeName")) {
                sinaSSOController.getServerTime(F.value, function () {
                })
            }
        });
        af.on(au, "keyup", function (d) {
            if (aC.style.display != "none") {
                return
            }
            if (d.keyCode == 13) {
                af.trigger(am(".loginBtn", m), "click")
            }
        });
        af.on(au, "keypress", function (d) {
            ac(d, 13)
        });
        af.on(r, "click", function (d) {
            d.preventDefault();
            V(ag)
        });
        af.on(Q, "keyup", function (d) {
            if (d.keyCode == 13) {
                af.trigger(am(".loginBtn", m), "click")
            }
        });
        var t = am(".forgetPas", m);
        af.on(t, "click", function (E) {
            if (F.value) {
                var d = ae.attr(t, "href");
                if (d.indexOf("loginname=") < 0) {
                    ae.attr(t, "href", d + "&loginname=" + F.value)
                } else {
                    ae.attr(t, "href", d.replace(/loginname=.*$/g, "loginname=" + F.value))
                }
            }
            return true
        });
        af.on(am(".loginBtn", m), "click", function (aF) {
            var aH = this;
            aF.stopPropagation();
            if (ae.hasClass(this, "loginBtnload")) {
                return
            }
            var R = aw(F.value).split("@");
            if (R.length > 2) {
                R = R[0] + "@" + R[1];
                F.value = R
            } else {
                F.value = aw(F.value)
            }
            var d = F, aG = d.value.trim(), aE = au, E = aE.value.trim(), aD;
            e = E == aE.value ? 0 : 1;
            if (!P(aG, "11")) {
                ae.hide(am(".tip13"), 0);
                ae.hide(am(".tip16"), 0);
                d.focus();
                return
            }
            if (!w(E, "13")) {
                ae.hide(am(".tip11"), 0);
                ae.hide(am(".tip16"), 0);
                aE.focus();
                return
            }
            if (aC.style.display != "none") {
                if (Q.value == "") {
                    am(".tip16").innerHTML = "请输入验证码";
                    ae.show(am(".tip16"), 0);
                    return
                }
                if (sinaSSOController.loginExtraQuery) {
                    sinaSSOController.loginExtraQuery.door = Q.value
                }
            } else {
                if (sinaSSOController.loginExtraQuery && sinaSSOController.loginExtraQuery.door) {
                    delete sinaSSOController.loginExtraQuery.door
                }
            }
            if (sinaSSOController.loginExtraQuery && sinaSSOController.loginExtraQuery.vsnf) {
                delete sinaSSOController.loginExtraQuery.vsnf
            }
            ae.hide(am(".tip13"), 0);
            ae.hide(am(".tip16"), 0);
            if (aG.indexOf("sina.cn") != -1) {
                sinaSSOController.entry = "cnmail"
            }
            if (aG.indexOf("sina.com") != -1) {
                sinaSSOController.entry = "freemail"
            }
            X.util.cookie("freeName", aG, 100);
            ap("store1").checked && (aD = 30);
            sinaSSOController.setLoginType(ap("ssl1").checked ? 3 : 2);
            setTimeout(function () {
                ae.addClass(aH, "loginBtnload");
                g = X.now();
                n = [1, aG, X.util.cookie("store1"), ap("ssl1").checked ? 1 : 0];
                sinaSSOController.login(aG.replace(/(^1\d{10})(@sina\.cn$)/, "$1").replace("sina.com.cn", "sina.com"), E, aD)
            }, 0)
        });
        af.on(ap("store1"), "click", function () {
            if (this.checked) {
                ae.show(am(".tip14"), 0);
                X.util.cookie("store1", 1, 100)
            } else {
                ae.hide(am(".tip14"), 0);
                X.util.cookie("store1", 0, 100)
            }
        });
        af.on(ap("ssl1"), "click", function () {
            if (this.checked) {
                X.util.cookie("https1", 1, 100)
            } else {
                try {
                    SUDA.uaTrack("mail_logout", "2")
                } catch (d) {
                }
                X.util.cookie("https1", 0, 100)
            }
        });
        af.on(ap("member"), "click", function () {
            var E = [];
            E.push('<div class="login_fail" style="margin-left:14px"><table cellpadding="0" cellspacing="0" border="0">');
            E.push('<tr><th></th><td><div class="visbleheight" style="visibility:visble;"><div class="input_tip tip31" style="display:none">登录名或密码输入不正确</div><div class="input_tip tip32" style="display:none">请输入登录名</div><div class="input_tip tip33" style="display:none">请输入密码</div><div class="input_tip tip34" style="display:none">请输入验证码</div></div></td></tr>');
            E.push('<tr><th>微博帐号/会员名：</th><td><input id="memname" class="input_w1" type="text" /></td></tr>');
            E.push('<tr><th></th><td><div class="visbleheight" style="visibility:visble;"></div></td></tr>');
            E.push('<tr><th class="vtop">密&nbsp;&nbsp;码：</th><td><input id="mempwd" class="input_w1" type="password" /></td></tr>');
            E.push('<tr class="trpasserr"><th></th><td><div class="visbleheight" style="visibility:visble;"></div></td></tr>');
            E.push('<tr class="trcode" style="display:none"><th>验证码：</th><td><input id="memcode" class="input_w2" type="text" /><a href="#" class="chgcode"><img class="checkcode" alt="" src=""></a></td></tr>');
            E.push('<tr><th></th><td><div class="check_name"><input checked type="checkbox" id="remember3" /><label for="remember3">记住登录名</label>');
            E.push('<input type="checkbox" id="store3" checked="cheched"/><label for="store3">保持登录状态</label></div>');
            E.push('<div class="safeTipflt">为了您的安全信息，请不要在网吧或公共电脑上使用此功能。</div></td></tr>');
            E.push('<tr><th></th> <td><div class="freeM_btn"><a href="javascript://;" id="nextStep"><span>下一步</span></a></div></td></tr>');
            E.push("</table></div>");
            var d = E.join("");
            var R = function () {
                var aD = new MiniDialog();
                aD.create(d).setCaption("微博帐号/会员名登录").moveToCenter();
                conf.dialog = aD;
                ap("memname").value = decodeURI(X.util.cookie("memberName") || "");
                ap("memname").focus();
                af.on(ap("remember3"), "click", function () {
                    if (!this.checked) {
                        X.util.cookie("memberName", "", 100)
                    }
                });
                af.on(ap("store3"), "click", function () {
                    if (this.checked) {
                        ae.show(am(".safeTipflt"), 0)
                    } else {
                        ae.hide(am(".safeTipflt"), 0)
                    }
                });
                af.on(ap("nextStep"), "click", function () {
                    ap("memname").value = aw(ap("memname").value);
                    var aG = ap("memname").value || "", aJ = ap("mempwd").value || "", aI;
                    var aH = ap("memcode").value || "";
                    if (!P(aG, "32")) {
                        ae.hide(am(".tip31"), 0);
                        ae.hide(am(".tip33"), 0);
                        ae.hide(am(".tip34"), 0);
                        ap("memname").focus();
                        return
                    }
                    if (!w(aJ, "33")) {
                        ae.hide(am(".tip31"), 0);
                        ae.hide(am(".tip32"), 0);
                        ae.hide(am(".tip34"), 0);
                        ap("mempwd").focus();
                        return
                    }
                    if (ae.isVisible(ap("memcode"))) {
                        if (aH == "") {
                            am(".tip34").innerHTML = "请输入验证码";
                            ae.show(am(".tip34"), 0);
                            ae.hide(am(".tip31"), 0);
                            ae.hide(am(".tip32"), 0);
                            ae.hide(am(".tip33"), 0);
                            ap("memcode").focus();
                            return
                        } else {
                            if (sinaSSOController.loginExtraQuery) {
                                sinaSSOController.loginExtraQuery.door = aH
                            }
                        }
                    } else {
                        if (sinaSSOController.loginExtraQuery && sinaSSOController.loginExtraQuery.door) {
                            delete sinaSSOController.loginExtraQuery.door
                        }
                    }
                    ae.hide(am(".tip32"), 0);
                    ae.hide(am(".tip33"), 0);
                    ae.hide(am(".tip34"), 0);
                    sinaSSOController.entry = "freemail";
                    ap("remember3").checked && X.util.cookie("memberName", encodeURI(aG), 100);
                    ap("store3").checked && (aI = 30);
                    X.util.cookie("store3", aI == 30 ? 1 : 0);
                    conf.isMem = true;
                    g = X.now();
                    n = [3, aG, X.util.cookie("store3"), 1];
                    sinaSSOController.login(aG.replace(/(^1\d{10})(@sina\.cn$)/, "$1").replace("sina.com.cn", "sina.com"), aJ, aI)
                });
                af.on(ap("memname"), "keyup", function (aG) {
                    if (aG.keyCode == 13) {
                        ap("mempwd").focus()
                    }
                });
                af.on(ap("mempwd"), "keyup", function (aG) {
                    if (aG.keyCode == 13) {
                        af.trigger(ap("nextStep"), "click")
                    }
                });
                af.on(ap("mempwd"), "keypress", function (aG) {
                    ac(aG, 33)
                });
                af.on(ap("memcode"), "keyup", function (aG) {
                    if (aG.keyCode == 13) {
                        af.trigger(ap("nextStep"), "click")
                    }
                });
                var aF = am(".chgcode", aD._body), aE = am("img", aD._body);
                af.on(aF, "click", function (aG) {
                    aG.preventDefault();
                    V(aE)
                });
                j = true
            };
            if (j && MiniDialog) {
                R()
            } else {
                X.io.script(al + "js/dialog.js", R)
            }
        })
    }
    af.on(J, "focus", G);
    af.on(v, "focus", G);
    af.on(aa, "focus", G);
    af.on(ab, "focus", G);
    if ($B.ie6 || $B.ie7 || $B.ie8) {
        af.on(J, "propertychange", B);
        af.on(v, "propertychange", B);
        af.on(aa, "propertychange", B);
        af.on(ab, "propertychange", B)
    } else {
        af.on(J, "input", B);
        af.on(v, "input", B);
        af.on(aa, "input", B);
        af.on(ab, "input", B)
    }
    af.on(aA, "click", function (d) {
        X.util.cookie("vipName", "");
        J.value = "";
        J.focus();
        ae.hide(aA);
        ae.show(am(".placeholder", J.parentNode));
        if (ae.isVisible(at)) {
            ae.hide(at)
        }
    });
    af.on(J, "keyup", function (d) {
        if (d.keyCode == 13) {
            v.focus()
        }
    });
    af.on(v, "keypress", function (d) {
        ac(d, 23)
    });
    af.on(v, "keyup", function (d) {
        if (d.keyCode == 13) {
            af.trigger(am(".loginBtn", x), "click")
        }
    });
    af.on(aa, "keyup", function (d) {
        if (d.keyCode == 13) {
            af.trigger(am(".loginBtn", x), "click")
        }
    });
    af.on(ab, "keyup", function (d) {
        if (d.keyCode == 13) {
            af.trigger(am(".loginBtn", x), "click")
        }
    });
    af.on(p, "click", function (d) {
        d.preventDefault();
        V(Y)
    });
    af.on(am(".loginBtn", x), "click", function (aD) {
        var aF = this;
        aD.stopPropagation();
        if (ae.hasClass(this, "loginBtnload")) {
            return
        }
        if ($B.ie8) {
            J.setAttribute("data-prevent", true);
            setTimeout(function () {
                J.removeAttribute("data-prevent")
            }, 100)
        }
        J.value = aw(J.value);
        var d = J, R = v, aE = d.value + "@vip.sina.com", E;
        if (!P(aE, "21")) {
            ae.hide(am(".tip23"), 0);
            ae.hide(am(".tip25"), 0);
            ae.hide(am(".tip26"), 0);
            d.focus();
            return
        }
        if (!w(R.value, "23")) {
            ae.hide(am(".tip21"), 0);
            ae.hide(am(".tip25"), 0);
            ae.hide(am(".tip26"), 0);
            R.focus();
            return
        }
        if (at.style.display != "none") {
            if (ab.value == "") {
                am(".tip25").innerHTML = "请输入动态码";
                ae.show(am(".tip25"), 0);
                ae.hide(am(".tip21"), 0);
                ae.hide(am(".tip23"), 0);
                ae.hide(am(".tip26"), 0);
                return
            } else {
                sinaSSOController.loginExtraQuery.vsnval = ab.value
            }
        } else {
            if (sinaSSOController.loginExtraQuery && sinaSSOController.loginExtraQuery.vsnval) {
                delete sinaSSOController.loginExtraQuery.vsnval
            }
        }
        if (aq.style.display != "none") {
            if (aa.value == "") {
                am(".tip26").innerHTML = "请输入验证码";
                ae.show(am(".tip26"), 0);
                return
            }
            if (sinaSSOController.loginExtraQuery) {
                sinaSSOController.loginExtraQuery.door = aa.value
            }
        } else {
            if (sinaSSOController.loginExtraQuery && sinaSSOController.loginExtraQuery.door) {
                delete sinaSSOController.loginExtraQuery.door
            }
        }
        ae.hide(am(".tip23"), 0);
        ae.hide(am(".tip21"), 0);
        ae.hide(am(".tip25"), 0);
        ae.hide(am(".tip26"), 0);
        sinaSSOController.entry = "vipmail";
        sinaSSOController.loginExtraQuery.vsnf = 1;
        X.util.cookie("vipName", d.value || "", 100);
        ap("store2").checked && (E = 30);
        sinaSSOController.setLoginType(ap("ssl2").checked ? 3 : 2);
        setTimeout(function () {
            ae.addClass(aF, "loginBtnload");
            g = X.now();
            n = [2, aE, X.util.cookie("store2"), ap("ssl2").checked ? 1 : 0];
            sinaSSOController.login(aE, R.value, E)
        }, 0)
    });
    af.on(ap("store2"), "click", function () {
        if (this.checked) {
            ae.show(am(".tip24"), 0);
            X.util.cookie("store2", 1, 100)
        } else {
            ae.hide(am(".tip24"), 0);
            X.util.cookie("store2", 0, 100)
        }
    });
    af.on(ap("ssl2"), "click", function () {
        if (this.checked) {
            X.util.cookie("https2", 1, 100)
        } else {
            try {
                SUDA.uaTrack("mail_logout", "2")
            } catch (d) {
            }
            X.util.cookie("https2", 0, 100)
        }
    });
    var c = am(".forgetPas", x);
    af.on(c, "click", function (E) {
        if (J.value) {
            var d = ae.attr(c, "href");
            if (d.indexOf("loginname=") < 0) {
                ae.attr(c, "href", d + "&loginname=" + J.value + "@vip.sina.com")
            } else {
                ae.attr(c, "href", d.replace(/loginname=.*$/g, "loginname=" + J.value + "@vip.sina.com"))
            }
        }
        return true
    });
    af.on(i, "mouseover", function (d) {
        if (d.target.type == "text" || d.target.type == "password" && !ae.hasClass(d.target.parentNode, "focus")) {
            ae.addClass(d.target, "hover")
        }
    });
    af.on(i, "mouseout", function (d) {
        if (d.target.type == "text" || d.target.type == "password") {
            ae.removeClass(d.target, "hover")
        }
    });
    function ay() {
        SINA_QRCODE_LOGIN.getQRcode(function (d) {
            ae.hide(ap("code_refresh"));
            var E = am("img", am(".weibo_code"));
            if (d.retcode == 20000000) {
                E.src = d.data.image;
                SINA_QRCODE_LOGIN.start()
            } else {
                alert(d.errmsg)
            }
        })
    }

    function Z() {
        var d = "https://open.weixin.qq.com/connect/qrconnect?appid=wx3141f8947f1713e8&scope=snsapi_login&redirect_uri=https://mail.sina.com.cn/register/weixin.php&state=&login_type=jssdk&href=https://mail2008.sina.com.cn/css/weixin_code.css?v=20161222";
        var E = am("iframe", am(".weixin_login"));
        if (!ae.attr(E, "src")) {
            ae.attr(E, "src", d);
            if ($B.firefox) {
                af.on(av, "beforeunload", function (R) {
                    E.parentNode.replaceChild(E.cloneNode(true), E)
                }, this)
            }
        }
    }

    SINA_QRCODE_LOGIN.register("login_success", function () {
        av.location.href = q + "&from=weibocode"
    });
    SINA_QRCODE_LOGIN.register("qrcode_timeout", function () {
        ae.show(ap("code_refresh"))
    });
    SINA_QRCODE_LOGIN.register("login_failure", function () {
        ae.show(ap("code_refresh"))
    });
    af.on(am(".switch", i), "click", function (d) {
        ay();
        Z();
        ae.hide(i);
        ae.show(aj)
    });
    af.on(am(".switch", aj), "click", function (d) {
        ae.hide(aj);
        ae.show(i)
    });
    af.on(ap("code_refresh"), "click", function (d) {
        ay()
    });
    J.value = X.util.cookie("vipName") || "";
    if (C) {
        af.on(C, "mouseover", function (d) {
            k.style.display = "";
            ae.removeClass(k, "aniOut");
            setTimeout(function () {
                ae.addClass(k, "aniIn")
            }, 100)
        });
        af.on(C, "mouseout", function (d) {
            M = setTimeout(function () {
                if ($B.ie) {
                    k.style.display = "none"
                }
                ae.removeClass(k, "aniIn");
                ae.addClass(k, "aniOut");
                av.clearTimeout(M)
            }, 200)
        });
        af.on(k, "mouseover", function (d) {
            av.clearTimeout(M);
            this.style.display = ""
        });
        af.on(k, "mouseout", function (R) {
            var E = R.srcElement || R.target, d;
            var aD = R.toElement || R.relatedTarget;
            if (!ae.contains(this, aD)) {
                if ($B.ie) {
                    k.style.display = "none"
                }
                ae.removeClass(k, "aniIn");
                ae.addClass(k, "aniOut")
            }
        });
        af.on(k, "mouseout", function (R) {
            var E = R.srcElement || R.target, d;
            var aD = R.toElement || R.relatedTarget;
            if (!ae.contains(this, aD)) {
                if ($B.ie) {
                    k.style.display = "none"
                }
                ae.removeClass(k, "aniIn");
                ae.addClass(k, "aniOut")
            }
        })
    }
    (function () {
        var aD, E, aJ;
        if (O) {
            aD = X.util.cookie("freeName") || "";
            E = F;
            aJ = au
        } else {
            aD = X.util.cookie("vipName") || "";
            E = J;
            aJ = v;
            conf.isVip = true
        }
        if (aD) {
            sinaSSOController.getServerTime(aD, function () {
            })
        }
        E.value = aD;
        if (aD) {
            ae.hide(am(".placeholder", E.parentNode))
        }
        if (X.util.cookie("store1") == 0) {
            ap("store1").checked = false;
            ae.hide(am(".tip14"), 0)
        }
        if (X.util.cookie("store2") == 0) {
            ap("store2").checked = false;
            ae.hide(am(".tip24"), 0)
        }
        var d = ae.node(L.body, "img", {
            src: "https://www.sinaimg.cn/rny/sinamail57/images/140711/loading1.gif",
            style: "position: absolute;top:-15px"
        });
        if (ap("ssl1")) {
            ap("ssl1").checked = false
        }
        af.on(d, "load", function () {
            if (ap("ssl1")) {
                ap("ssl1").checked = true
            }
            ap("ssl2").checked = true
        });
        setTimeout(function () {
            try {
                E.focus();
                if (E.value) {
                    aJ.focus()
                }
            } catch (aK) {
            }
        }, 50);
        if (aD.indexOf(S) != -1 || aD.indexOf(ad) != -1 || aD.indexOf(T) != -1) {
            setTimeout(function () {
                try {
                    aJ.focus()
                } catch (aK) {
                }
            }, 50)
        }
        var aH = location.href, aE = aH.split("?")[1];
        if (aE && aE.indexOf("err") != -1) {
            var aG = aE.indexOf("err="), R = aE.substr(aG + 4).trim(), aF = {
                "50101": "<h3>正在使用的人太多，请您耐心等待一下。</h3>",
                "50102": "<h3>已检测到您的会员名没有开通邮箱，请重新登录。</h3>",
                "50103": "<h3>用户系统繁忙，稍后再试。</h3>",
                "50105": "<h3>服务请正在维护中，请耐心等待一下。</h3>",
                "50107": "<h3>帐号切换失败，请重新登录。</h3>",
                "50108": "<h3>您的帐号存在安全风险，请登录关联的vip邮箱进行验证。</h3>",
                "50109": "<h3>您的帐号已经登出，请重新登录。</h3>",
                "50110": "<h3>您的VIP邮箱已过期，请您重新登录并续费。</h3>",
                "50111": "<h3>无权访问该账号，请重新登录。</h3>",
                "2089": "<h3>您已开启登录保护，请查收手机短信并继续完成登录</h3>"
            };
            if (aG != -1 && R && aF[R]) {
                am(".keyerr").innerHTML = aF[R];
                I("keyerr")
            } else {
                I("timeout")
            }
            if (!O) {
                b()
            }
        } else {
            if (aE && aE.indexOf("jumpto") != -1) {
                q = q.replace("?", "?" + aE.replace(/(^[\w|\W]*)(jumpto=[^\#\&]*)([\#|\&]*[\w|\W]*$)/, "$2&"))
            }
            if (O) {
                D()
            } else {
                b()
            }
        }
        try {
        } catch (aI) {
        }
    })();
    (function o() {
        ae.addHTML(L.body, '<ins class="sinaads" data-ad-pdps="PDPS000000058126" data-ad-type="float"></ins>');
        (function (aD, R, aF) {
            var R, aE = aD.getElementsByTagName(R)[0];
            if (aD.getElementById(aF)) {
                return
            }
            R = aD.createElement(R);
            R.id = aF;
            R.setAttribute("charset", "utf-8");
            R.src = "//d" + Math.floor(0 + Math.random() * (9 - 0 + 1)) + ".sina.com.cn/litong/zhitou/sinaads/release/sinaads.js";
            aE.parentNode.insertBefore(R, aE)
        })(L, "script", "sinaads-script");
        (sinaads = av.sinaads || []).push({params: {sinaads_float_show_pos: 0, sinaads_float_top: 1}});
        var d = false, E = function () {
            if (!ap("sinaadToolkitBox0") || !ap("sinaadToolkitBox1")) {
                if (d) {
                    return
                }
                return setTimeout(E, 100)
            }
            if (!d) {
                am(".mainBox").style.position = "relative";
                am(".mainBox").appendChild(ap("sinaadToolkitBox0"));
                am(".mainBox").appendChild(ap("sinaadToolkitBox1"))
            }
            d = true;
            if (L.body.clientWidth < 1280) {
                ae.hide(ap("sinaadToolkitBox0"));
                ae.hide(ap("sinaadToolkitBox1"));
                return
            }
            ae.show(ap("sinaadToolkitBox0"));
            ae.show(ap("sinaadToolkitBox1"))
        };
        af.on(av, "resize", E);
        E()
    })();
    var a = function (d) {
        var d = d.replace(".cn", "");
        var E = function () {
            var R = '<div class="loginMail" style="font-size:12px;color:#000;"><div style="float:left;width:40px;height:40px;background:url(' + al + 'images/warning.gif) no-repeat 0 0"></div>&nbsp;&nbsp;您的登录账号为' + d + '，请使用此账号进行登录。<div style="color:#aaa;padding:9px 0">&nbsp;&nbsp;投递到' + d + '.cn的信仍然可以收到。</div><div class="freeM_btn" style="margin-left:220px;margin-top:10px"><a title="" href="' + q + g + "&b=" + f + "&c=" + 2 + '"><span>确认</span></a></div></div>';
            var aD = new MiniDialog();
            aD.create(R).setCaption("提示").moveToCenter();
            aD.close = function () {
                if (this.doAction) {
                    this.doAction("cancel", this._btnClose);
                    q = q + g + "&b=" + f + "&c=" + 2;
                    av.location.href = q
                }
            };
            ae.css(aD._self, "width", "520px");
            am("a", aD._body).focus()
        };
        if (j && MiniDialog) {
            E()
        } else {
            X.io.script(al + "js/dialog.js", E)
        }
    };
    conf.loginCallBack = function (R) {
        f = X.now();
        function aJ(aP) {
            conf.dialog.close();
            var aO = '<div class="loginMail">您已登录成功，系统将默认使用您的邮箱名登录 <div class="userM">' + aP + '</div><div class="freeM_btn"><a title="" href="' + q + g + "&b=" + f + "&c=" + e + '"><span>确认</span></a></div></div>';
            var aQ = new MiniDialog();
            aQ.create(aO).setCaption("微博帐号/会员名登录").moveToCenter();
            aQ.close = function () {
                if (this.doAction) {
                    this.doAction("cancel", this._btnClose);
                    q = q + g + "&b=" + f + "&c=" + e;
                    av.location.href = q
                }
            };
            am("a", aQ._body).focus()
        }

        function aL() {
            conf.dialog.close();
            var aO = '<div class="regist"><div class="text">您还没有新浪邮箱</div><div class="freeM_btn"><a href="https://mail.sina.com.cn/register/bind_mail.php"><span>立即开通</span></a></div></div>';
            var aP = new MiniDialog();
            aP.create(aO).setCaption("微博帐号/会员名登录").moveToCenter()
        }

        if (conf.isMem) {
            if (R.result) {
                var aM = sinaSSOController.getSinaCookie();
                if (aM.email) {
                    aJ(aM.email)
                } else {
                    try {
                        X.io.text("cgi-bin/queryMail.php", {
                            data: "login=" + encodeURIComponent(aM.name),
                            success: function (aP) {
                                var aO = aP;
                                aO.indexOf("mail") == -1 ? aL() : aJ(aO.replace(/mail=/g, ""))
                            },
                            failure: function (aO) {
                                alert(aO)
                            }
                        })
                    } catch (aF) {
                    }
                }
            } else {
                var aI = "31", E = R.errno, aD = R.reason || "";
                var aE = am(".trcode"), aG = am("input", aE), aN = am("img", aE);
                X.io.json("/cgi-bin/lc.php?a=1", {method: "post", params: {b: E + ":" + n.join(":")}});
                switch (E) {
                    case"4047":
                        I("locked");
                        break;
                    case"4049":
                        V(aN);
                        am(".tip" + aI).innerHTML = "&nbsp;";
                        ae.show(am(".tip" + aI), 0);
                        aE.style.display = "";
                        aG.value = "";
                        break;
                    case"2070":
                        V(aN);
                        am(".tip" + aI).innerHTML = aD;
                        ae.show(am(".tip" + aI), 0);
                        break;
                    case"4057":
                        am(".tip" + aI).innerHTML = aD;
                        ae.show(am(".tip" + aI), 0);
                        break;
                    case"101":
                        am(".tip" + aI).innerHTML = aD;
                        ae.show(am(".tip" + aI), 0);
                        if (aC.style.display != "none") {
                            V(aN)
                        }
                        break;
                    default:
                        am(".tip" + aI).innerHTML = aD;
                        ae.show(am(".tip" + aI), 0)
                }
            }
            conf.isMem = false
        } else {
            if (R.result) {
                if (!conf.isVip && F && F.value.indexOf("sina.com.cn") > -1) {
                    a(F.value);
                    return
                }
                q = q + g + "&b=" + f + "&c=" + e + "&ssl=" + n[3];
                av.location.href = q
            } else {
                var d = conf.isVip;
                var aI = d ? "21" : "11", E = R.errno, aD = R.reason || "";
                var aK = d ? am("img", aq) : am("img", aC);
                var aH = am(".loginBtnload", d ? x : m);
                aH && ae.removeClass(aH, "loginBtnload");
                X.io.json("/cgi-bin/lc.php?a=1", {method: "post", params: {b: E + ":" + n.join(":")}});
                switch (E) {
                    case"4047":
                        I("locked");
                        break;
                    case"4049":
                        V(aK);
                        if (d) {
                            aq.style.display = "";
                            aa.value = ""
                        } else {
                            aC.style.display = "";
                            aG.value = ""
                        }
                        break;
                    case"2070":
                        V(aK);
                        am(".tip" + (d ? "26" : "16")).innerHTML = aD;
                        ae.show(am(".tip" + aI), 0);
                        break;
                    case"4057":
                        am(".tip" + aI).innerHTML = aD;
                        ae.show(am(".tip" + aI), 0);
                        break;
                    case"101":
                        am(".tip" + aI).innerHTML = aD;
                        ae.show(am(".tip" + aI), 0);
                        if (d) {
                            if (aq.style.display != "none") {
                                V(aK)
                            }
                        } else {
                            if (aC.style.display != "none") {
                                V(aK)
                            }
                        }
                        break;
                    case"5024":
                        aq.style.display = "none";
                        aa.value = "";
                        z = true;
                        if (d) {
                            am(".mailvsn", x).style.display = ""
                        } else {
                            am(".mailvsn", m).style.display = ""
                        }
                        ab.value = "";
                        ab.focus();
                        break;
                    case"5025":
                        am(".tip" + aI).innerHTML = aD;
                        ae.show(am(".tip" + aI), 0);
                        break;
                    case -1:
                        am(".tip" + aI).innerHTML = "登录超时，请重试";
                        ae.show(am(".tip" + aI), 0);
                        !d ? ap("ssl1").checked = false : ap("ssl2").checked = false;
                        break;
                    case -100:
                        am(".tip" + aI).innerHTML = "网络环境异常";
                        ae.show(am(".tip" + aI), 0);
                        !d ? ap("ssl1").checked = false : ap("ssl2").checked = false;
                        break;
                    default:
                        am(".tip" + aI).innerHTML = aD;
                        ae.show(am(".tip" + aI), 0)
                }
            }
        }
    }
});