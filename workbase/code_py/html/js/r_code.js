/**
 * Created by BQ0391 on 2017/12/19.
 */
(function () {
    function z(a) {
        for (var g = 1, q, e; q = arguments[g]; g++)for (e in q)a[e] = q[e];
        return a
    }

    function y(a) {
        return Array[E].slice.call(a)
    }

    function r(a, g) {
        for (var q = a.length >> 0; q--;)if (g === a[q])return q;
        return -1
    }

    function u(a) {
        var g, q, e;
        if (g = k.build) q = g[0], g = g[1] || "1.0", e = N || (N = C("[?|&]" + q + "=([^&]*)", "i")), a = e.test(a) ? a.replace(C.$1, g) : a + ((-1 !== a.indexOf("?") ? "&" : "?") + q + "=" + g);
        return a
    }

    function j() {
        for (var a = y(arguments), g = [], q = 0, e = a.length; q < e; q++)0 < a[q].length && g.push(a[q].replace(/\/$/, ""));
        return u(g.join("/"))
    }

    function m(a) {
        for (var g = -1, q, e = O, d = e.length; ++g < d;)for (q in e[g])if (q !== a && -1 !== r(e[g][q], a))return u(q);
        return a
    }

    function n(a, g, q) {
        for (var g = g.split("/"), e = a; 1 < g.length;)a = g.shift(), e = e[a] || (e[a] = {});
        e[g[0]] = q
    }

    function x(a, q, d) {
        var b = H.cloneNode(!1), p = a.sid = b.id = "LR" + ++F, i = function () {
            e.removeChild(b);
            b.onload = b[P] = b.onerror = null;
            b = void 0
        };
        b.type = "text/javascript";
        b.onload = b[P] = function () {
            if (!b.readyState || W[b.readyState]) delete J[p], i(), q(a)
        };
        b.onerror = function () {
            var g = Error("Syntax error or http error: " + a.path);
            if (d) d(g); else throw g;
            i()
        };
        b.charset = "utf-8";
        b.async = !0;
        b.src = a.path;
        g = J[p] = a;
        e.insertBefore(b, e.firstChild);
        g = null
    }

    function t() {
    }

    function f(a) {
        a && (this.id = this.path = m(a))
    }

    function c(a, g) {
        var e = q[a];
        if (e && e.body)return e;
        this.id = a;
        this.body = g;
        g || (e = m(a), this.path = e !== a ? e : j(k.baseUrl, a + ".js"))
    }

    function h(a) {
        for (var g = [], q = -1, e; e = a[++q];)e instanceof l ? g = g.concat(h(e.deps)) : e instanceof c && g.push(e);
        return g
    }

    function w(a) {
        this.deps = a;
        0 == this.deps.length && this.complete()
    }

    function l(a) {
        this.deps = a
    }

    function s(e, d) {
        var b;
        if (!e && D && !(b = g))a:{
            for (b = a.length; b--;)if ("interactive" === a[b].readyState) {
                b = J[a[b].id];
                break a
            }
            b = void 0
        }
        b ? (delete J[b.sid], b.body = d, b.exec()) : (G = b = new c(e, d), q[b.id] = b);
        return b
    }

    function d(a, g) {
        if ("." !== a.charAt(0))return a;
        var q = (g.id || "").split("/");
        q.pop();
        q = q.join("/");
        return a.replace(/^\./, q)
    }

    function v(a) {
        return function (g) {
            var q = c.exports[d(g, a)];
            q || (k(g).then(function (a) {
                q = a
            }), q || R('module (id="' + g + '") not load yet.'));
            return q
        }
    }

    function B(a) {
        for (var g = [], q = -1, e; e = a[++q];) {
            if ("string" === typeof e)a:{
                var b = S, d = b.length, p = null;
                if (0 < d) {
                    do if (p = b[--d], e.match(p[0])) {
                        e = p[1](e);
                        break a
                    } while (d)
                }
                R(e + " was not recognised by loader");
                e = null
            } else L(e) && (e = new l(B(e)));
            e && g.push(e)
        }
        return g
    }

    function b() {
        var a = y(arguments), g;
        "string" === typeof a[0] && (g = a.shift());
        a = a.shift();
        return s(g, a)
    }

    function k() {
        var a = y(arguments), g;
        "function" === typeof a[a.length - 1] && (g = a.pop());
        a = new w(B(a));
        g && a.then(g);
        return a
    }

    function A(a, g) {
        S.push([a, g])
    }

    var p = this || Function("return this")();
    if (!p.runner) {
        var i = p.document, C = p.RegExp, a = i.getElementsByTagName("script"), e = i.head || i.getElementsByTagName("head")[0], H = i.createElement("script"), F = 0, I = {}, q = {}, G, g, D = p.attachEvent && !p.opera, J = {}, K = {}, W = {
            loaded: 1,
            interactive: 1,
            complete: 1
        }, P = "onreadystatechange", E = "prototype", L = Array.isArray || function (a) {
                return a.constructor === Array
            }, M = null, T = null, S = [], O = [], N = null, R = function () {
            var a = p.console;
            return a ? function () {
                a.error.apply(a, arguments)
            } : function () {
            }
        }(), i = t.prototype;
        i.then = function (a) {
            this.started || (this.started = !0, this.start(!0));
            this.completed ? a.apply(p, this.results) : (this.callbacks = this.callbacks || [], this.callbacks.push(a));
            return this
        };
        i.start = function () {
        };
        i.complete = function () {
            if (!this.completed && (this.results = y(arguments), this.completed = !0, this.callbacks))for (var a = 0, g; g = this.callbacks[a]; a++)g.apply(p, this.results)
        };
        f.loaded = [];
        f.times = {};
        i = f[E] = new t;
        i.start = function (a) {
            var g = this, e = g.id, b, d;
            if (d = q[e])return d.then(function () {
                g.complete()
            }), g;
            (b = I[e]) ? b.then(function () {
                g.loaded()
            }) : -1 !== r(f.loaded, e) ? g.loaded() : g.load(a);
            return g
        };
        i.load = function (a) {
            var g = this, q = g.path, e;
            a ? (I[g.id] = g, (e = K[q]) && g.then(function () {
                for (var a = 0, g; g = e[a]; a++)g.complete.apply(g, arguments)
            }), g.times = {start: new Date}, x(g, function () {
                g.loaded()
            })) : (K[q] = K[q] || [], K[q].push(g));
            return this
        };
        i.loaded = function () {
            this.complete()
        };
        i.complete = function () {
            -1 === r(f.loaded, this.id) && f.loaded.push(this.id);
            this.times && (f.times[this.id] = z(this.times, {end: new Date}));
            delete I[this.id];
            t[E].complete.apply(this, arguments)
        };
        c.exports = {};
        i = c[E] = new f;
        i.start = function (a) {
            var g = this, e = g.id, b;
            g.body ? g.exec() : (b = c.exports[e]) ? this.exp(b) : (b = q[e]) ? b.then(function (a) {
                g.exp(a)
            }) : (q[e] = g, g.load(a))
        };
        i.load = function (a) {
            a && (G = null);
            return f[E].load.apply(this, arguments)
        };
        i.loaded = function () {
            var a, g, e = this, b = e.id;
            D ? (g = c.exports[b]) ? e.exp(g) : (a = q[b]) && a.then(function (a) {
                e.exp(a)
            }) : (a = G, G = null, a.id = a.id || b, a.then(function (a) {
                e.exp(a)
            }))
        };
        i.complete = function () {
            delete q[this.id];
            f[E].complete.apply(this, arguments)
        };
        i.exec = function () {
            var a = this, g = a.body, e, q;
            "object" === typeof g ? a.exp(g) : "function" === typeof g && (e = v(a), q = function Q(g, e) {
                if (!Q.done) {
                    Q.done = !0;
                    g = a.exp(g);
                    if (e) {
                        var q = a.id, b = q.split("/");
                        b.length && b[0] === T && (b.shift(), q = b.join("/"));
                        n(M, q, g)
                    }
                    return g
                }
            }, g(e, q), !q.done && (!a.deps || !a.deps.length) && q())
        };
        i.exp = function (a) {
            this.times && z(this.times, {eval: new Date});
            var g = this.id;
            this.exports = c.exports[g] = a = a || {id: g};
            this.complete(a);
            return a
        };
        i = w[E] = new t;
        i.start = function () {
            function a() {
                for (var e = [], q = 0, b; b = g.deps[q]; q++) {
                    if (!b.completed)return;
                    0 < b.results.length && (e = e.concat(b.results))
                }
                g.complete.apply(g, e)
            }

            for (var g = this, e = 0, q; q = this.deps[e]; e++)q.then(a);
            return this
        };
        i.load = function () {
            for (var a = 0, g; g = this.deps[a]; a++)g.load && g.load(!0);
            return this
        };
        i.as = function (a) {
            var g = this;
            return g.then(function () {
                for (var e = h(g.deps), q = {}, b = -1, d; d = e[++b];)n(q, d.id, arguments[b]);
                a.apply(p, [q].concat(y(arguments)))
            })
        };
        i = l[E] = new t;
        i.start = function () {
            var a = this, g = 0, e = [];
            (function V() {
                var q = a.deps[g++];
                q ? q.then(function () {
                    0 < q.results.length && (e = e.concat(q.results));
                    V()
                }) : a.complete.apply(a, e)
            })();
            return this
        };
        i.load = function () {
            var a = this, g = 0;
            (function U() {
                var e = a.deps[g++];
                e && e.load && e.load(!0).then(U)
            })();
            return this
        };
        b.sandbox = function (a, g) {
            if (!M) {
                if ("object" !== typeof g)throw TypeError("sandbox reference should a object type");
                T = a;
                M = g || {};
                delete b.sandbox
            }
        };
        A(/(^script!|\.js$)/, function (a) {
            var g = new f(a.replace(/^\$/, k.baseUrl.replace(/\/$/, "") + "/").replace(/^script!/, ""), !1);
            g.id = a;
            return g
        });
        A(/^[a-zA-Z0-9_\-\/.]+$/, function (a) {
            return new c(a)
        });
        k.baseUrl = ".";
        k.regBundle = function (a) {
            L(a) || (a = [a]);
            [].push.apply(O, a)
        };
        k.addPattern = A;
        p.provide = b;
        p.using = k;
        p.define = function () {
            var a = y(arguments), g = [], e, q;
            "string" === typeof a[0] && (e = a.shift());
            L(a[0]) && (g = a.shift());
            q = a.shift();
            var b = s(e, function (a, e) {
                function p() {
                    for (var a = y(g), d = b, i = [], D = 0, f = a.length, c, k = v(d); D < f; D++)c = a[D], c = "require" === c ? k : "exports" === c ? d.exports || (d.exports = {}) : k(c), i.push(c);
                    a = "function" === typeof q ? q.apply(b, i) : q;
                    "undefined" === typeof a && (a = b.exports);
                    e(a)
                }

                for (var i = [], D = 0, c = g.length, f; D < c; D++)f = g[D], -1 === r(["require", "exports"], f) && i.push(d(f, b));
                i.length ? k.apply(this, i.concat(p)) : p()
            });
            b.deps = g || [];
            return b
        };
        (function () {
            for (var g, e, q = a.length; q--;)if (e = a[q], e.src.match(/^(.*?)r\.core\.js(\?|#|$)/)) {
                k.baseUrl = e.getAttribute("data-path") || C.$1 || "";
                if (q = e.getAttribute("data-ver")) k.build = ["v", q];
                (g = e.getAttribute("data-main")) && k.apply(p, g.split(/\s*,\s*/)).then(function () {
                });
                break
            }
        })()
    }
})();
provide("r/base", function (z, y) {
    function r(a, e) {
        for (var g = a.length, b = e.length; b--;)a[g + b] = e[b];
        return a
    }

    var u = Function, j = this || u("return this")(), m = y({VERSION: "1.3.0", global: j}), n = function (a) {
        return a
    }, x = function (a) {
        return function () {
            return a
        }
    }, t = x(), f = Object.prototype, c = f.toString, h = f.hasOwnProperty, w = Array.prototype.slice, l = u.prototype.bind, s = {}, d = !{toString: 1}.propertyIsEnumerable("toString"), v = !d ? [] : "propertyIsEnumerable,hasOwnProperty,valueOf,isPrototypeOf,toLocaleString,toString,constructor".split(","), B = v.length;
    provide.sandbox("r", m);
    (function (a) {
        if ("function" === typeof a.loadFirebugConsole) a.loadFirebugConsole(); else if (!a.console)for (var e = "assert,count,debug,dir,dirxml,error,group,groupEnd,info,profile,profileEnd,time,timeEnd,trace,warn,clear,log".split(","), g = e.length, a = a.console = {}; g--;)a[e[g]] = t
    })(j);
    var b = function (a, e, g, b) {
        var p, i, c;
        if (a && e) {
            if (b)for (i = b.length; i--;) {
                if (c = b[i], h.call(e, c) && (p = g ? !1 : key in a, g || !p)) a[c] = e[c]
            } else {
                for (c in e)if (b = e[c], !(c in a) || g && a[c] !== b && (!(c in s) || s[c] !== b)) a[c] = b;
                if (d && (i = B))for (; i;)if (c = v[--i], b = e[c], !(c in a) || a[c] !== b && (!(c in s) || s[c] !== b)) a[c] = b
            }
            return a
        }
    }, k = function (a, e, g) {
        for (var g = g || j, b = 0, d; g && (d = a[b]); b++)g = d in g ? g[d] : e ? g[d] = {} : void 0;
        return g
    }, A = function (a, e, g, b) {
        var d = a.split("."), a = d.pop();
        if ((g = k(d, !0, g)) && a) {
            if (!b && e && "object" === typeof e && void 0 !== g[a])for (a in g = g[a] || (g[a] = {}), e)h.call(e, a) && (g[a] = e[a]); else g[a] = e;
            return e
        }
    };
    b(m, {
        mixin: function (a, e) {
            var g = w.call(arguments, 1), d = -1, c = g.length, i = "boolean" === typeof g[c - 1] && !!g[--c];
            void 0 === e && (g[0] = e = a, a = this);
            for (; d < c;)b(a, g[++d], i);
            return a
        }, apply: b, merge: function () {
            var a = arguments, e = {}, g, d = a.length, c = "boolean" === typeof a[d - 1] && !!a[--d];
            for (g = 0; g < d; g += 1)b(e, a[g], c);
            return e
        }, bind: l ? function (a, e) {
            a = "string" === typeof a ? e[a] : a;
            return l.apply(a, w.call(arguments, 1))
        } : function (a, e) {
            var g = 2 < arguments.length ? w.call(arguments, 2) : 0, b, a = "function" !== typeof a ? e[a] : a;
            return g ? (b = g.length, function () {
                g.length = b;
                return a.apply(e, r(g, arguments))
            }) : function () {
                return a.apply(e, arguments)
            }
        }, setObject: A, getObject: function (a, e, g) {
            return k(a.split("."), e, g || this)
        }, declare: function (a, e, g) {
            if ("string" === typeof a)return A(a, e, this, g);
            "object" !== typeof e && (e = a, a = this);
            return e ? (b(a, e, g), e) : null
        }, I: n, K: x, noop: t, once: function (a) {
            var e = !1, g;
            return function () {
                if (e)return g;
                e = !0;
                return g = a.apply(this, arguments)
            }
        }, memoize: function (a, e) {
            var g = {};
            e || (e = n);
            return function () {
                var b = e.apply(this, arguments);
                return h.call(g, b) ? g[b] : g[b] = a.apply(this, arguments)
            }
        }, error: function (a) {
            console.error(a)
        }, log: function (a) {
            console.log(a)
        }
    });
    var p = {
        string: "string",
        number: "number",
        "boolean": "boolean",
        undefined: "undefined"
    }, i = Array.prototype.push, C = j.setTimeout, a = function (a) {
        var e;
        return p[typeof a] || p[e = c.call(a)] || (a ? e.slice(8, -1).toLowerCase() : "null")
    }, u = function (a, e, g) {
        var b = 0, d = a.length;
        if (void 0 === d || "function" === typeof a)for (b in a) {
            if (F(a, b) && !1 === e.call(g || a[b], a[b], b, a))break
        } else for (; b < d && !(!1 === e.call(g || a[b], a[b], b++, a)););
    }, e = function (a, e, g) {
        a = w.call(a, ~~e);
        return g ? (i.apply(g, a), g) : a
    }, H = Array.isArray || function (e) {
            return "array" === a(e)
        }, F = function (a, e) {
        return !!a && h.call(a, e)
    };
    u("Boolean,Number,String,Function,Array,Date,RegExp".split(","), function (e, b) {
        p["[object " + e + "]"] = b = e.toLowerCase();
        m["is" + e] = function (e) {
            return a(e) === b
        }
    });
    b(m, {
        isArray: H, type: a, each: u, filter: function (a, e) {
            if (a.filter)return a.filter(e);
            for (var g = [], b = 0, d = -1, c = a.length; b < c; b++)e(a[b], b) && (g[++d] = a[b]);
            return g
        }, owns: F, makeArray: function (a, b, g) {
            return null === a || void 0 === a ? [] : "string" === typeof a || "number" !== typeof a.length || m.isFunction(a) ? [a] : e(a, b, g)
        }, now: Date.now || function () {
            return (new Date).getTime()
        }, isNumber: function (a) {
            return "number" === typeof a && isFinite(a)
        }, isObject: function (e, b) {
            var g = typeof e;
            return !!e && ("object" === g || !b && ("function" === g || "function" === a(e)))
        }, isDate: function (e) {
            return "date" === a(e) && "Invalid Date" !== e.toString() && !isNaN(e)
        }, isDefined: function (a) {
            return "undefined" !== typeof a && null !== a
        }, isNode: function (a) {
            return !!a && 1 === a.nodeType && "string" === typeof a.nodeName
        }, isEmpty: function (a, e) {
            if (null === a || void 0 === a)return !1;
            if (H(a))return 0 === a.length;
            if ("object" === typeof a) {
                for (var g in a)if (F(a, g))return !1;
                return !0
            }
            return !e ? "" === a : !1
        }, isValue: function (e, b) {
            var g = a(e);
            switch (g) {
                case "number":
                    return isFinite(e);
                case "null":
                case "undefined":
                    return !1;
                default:
                    return g && (b ? "" !== e : !0)
            }
        }, later: function (a, e, g) {
            var e = void 0 === e ? 10 : e, b = arguments;
            if (4 > b.length && !g)return C(a, e);
            b = 3 < b.length ? w.call(b, 3) : [];
            return C(function () {
                a.apply(g, b)
            }, e)
        }, setter: function (a, e, g) {
            return function (b, d, c) {
                if (null == d)return b;
                var i = e || b;
                if (g || "string" !== typeof d)for (d in c = d, c)F(c, d) && a.call(i, b, d, c[d]); else return a.call(i, b, d, c);
                return i
            }
        }
    }, !0);
    m.toArray = m.makeArray;
    try {
        document && w.call(document.documentElement.childNodes, 0)
    } catch (I) {
        e = function (a, e, g) {
            var b = g || [], d = e || 0;
            if ("[object Array]" === c.call(a)) {
                e && (a = w.call(a, e));
                return g ? (i.apply(b, a), b) : a
            }
            if ("number" === typeof a.length)for (e = a.length; d < e; d++)b[b.length] = a[d]; else for (; a[d]; d++)b[b.length] = a[d];
            return b
        }
    }
});
provide("r/lang", function (z) {
    function y(a) {
        return k[a] || "\\u" + ("0000" + a.charCodeAt().toString(16)).slice(-4)
    }

    function r(a, e) {
        return -1 !== a.indexOf(e)
    }

    function u(a) {
        return ("" + a).replace(C, "\\$1")
    }

    function j(a, e, b) {
        if (!e)return a.trim();
        b = q[e] || (!b && (e = u(e)), q[e] = c("^(?:" + e + ")+|(?:" + e + ")+$", "g"));
        return ("" + a).trim().replace(b, "")
    }

    function m(a) {
        return a
    }

    function n(a, e) {
        return e
    }

    function x(a, e, b) {
        var d = [], c = -1, i;
        if (!a)throw new TypeError;
        for (i in a)G(a, i) && (d[++c] = e.apply(b, [a[i], i]));
        return d
    }

    var t = z("r/base"), f = t.global, c = f.RegExp, h = f.Object;
    if (!String.prototype.trim) {
        var w = new c("^[\t\n-\r \u00a0\u1680\u180e\u2000-\u200a\u202f\u205f\u3000\u2028\u2029\ufeff][\t\n-\r \u00a0\u1680\u180e\u2000-\u200a\u202f\u205f\u3000\u2028\u2029\ufeff]*"), l = new c("[\t\n-\r \u00a0\u1680\u180e\u2000-\u200a\u202f\u205f\u3000\u2028\u2029\ufeff][\t\n-\r \u00a0\u1680\u180e\u2000-\u200a\u202f\u205f\u3000\u2028\u2029\ufeff]*$");
        String.prototype.trim = function () {
            return ("" + this).replace(w, "").replace(l, "")
        }
    }
    t.mixin(Array.prototype, {
        indexOf: function (a) {
            var e = h(this), b = e.length >>> 0;
            if (!b)return -1;
            var d = 0;
            1 < arguments.length && (d = arguments[1] >>> 0);
            for (d = 0 <= d ? d : b - Math.abs(d); d < b; d++)if (d in e && e[d] === a)return d;
            return -1
        }, lastIndexOf: function (a) {
            var e = h(this), b = e.length >>> 0;
            if (!b)return -1;
            var d = b - 1;
            1 < arguments.length && (d = arguments[1] >>> 0);
            for (d = 0 <= d ? d : b - Math.abs(d); 0 <= d; d--)if (d in e && a === e[d])return d;
            return -1
        }, map: function (a, e) {
            if ("function" !== typeof a)throw new TypeError;
            for (var b = h(this), d = b.length >>> 0, c = Array(d), i = 0; i < d; i++)i in b && (c[i] = a.call(e, b[i], i, b));
            return c
        }, forEach: function (a, e) {
            if (!a || !a.call)throw new TypeError;
            for (var b = h(this), d = 0, c = b.length >>> 0; d < c;)d in b && a.call(e, b[d], d, b), d++
        }, every: function (a, e) {
            for (var b = this.length, d = 0; d < b; d++)if (!a.call(e, this[d], d, this))return !1;
            return !0
        }, some: function (a, e) {
            for (var b = this.length, d = 0; d < b; d++)if (a.call(e, this[d], d, this))return !0;
            return !1
        }, filter: function (a, e) {
            for (var b = [], d = 0, c = this.length, i = 0, p; d < c; d++)p = this[d], a.call(e, p, d, this) && (b[i++] = p);
            return b
        }
    });
    var s = t.getObject, d = t.isArray, v = /{(\d+)}/g, B = /{\$?([\w.]+?)}/g, b = /[\\\"\x00-\x1f\x7f-\x9f\u00ad\u0600-\u0604\u070f\u17b4\u17b5\u200c-\u200f\u2028-\u202f\u2060-\u206f\ufeff\ufff0-\uffff]/g, k = {
        "\u0008": "\\b",
        "\t": "\\t",
        "\n": "\\n",
        "\u000c": "\\f",
        "\r": "\\r",
        '"': '\\"',
        "/": "\\/",
        "\\": "\\\\"
    }, A = {"&": "&amp;", ">": "&gt;", "<": "&lt;", '"': "&quot;", "'": "&#39;"}, p = {
        "&lt;": "<",
        "&gt;": ">",
        "&quot;": '"',
        "&nbsp;": " ",
        "&amp;": "&"
    }, i = /<!(?:--[\s\S]*?--)?>\s*/g, C = /([-.*+?^${}()|[\]\/\\])/g, a = /%20/g, e = /[-_]\D/g, H = /[A-Z]/g, F = function (a) {
        return a.charAt(1).toUpperCase()
    }, I = function (a) {
        return "-" + a.toLowerCase()
    }, q = {};
    t.declare("string", {
        trim: j, inspect: function (a) {
            b.lastIndex = 0;
            return b.test(a) ? '"' + a.replace(b, y) + '"' : '"' + a + '"'
        }, format: function (a) {
            var e = Array.prototype.slice.call(arguments, 1);
            return a.replace(v, function (a, b) {
                return void 0 !== e[b] ? e[b] : a
            })
        }, supplant: function (a, e) {
            return a.replace(B, function (a, b) {
                if (-1 !== b.indexOf("."))return s(b, !1, e);
                b = e[b];
                return "object" !== typeof b ? b : a
            })
        }, tmplString: function (a) {
            return new Function("obj", "var p=[],print=function(){p.push.apply(p,arguments);};with(obj){p.push('" + a.replace(/[\r\t\n]/g, " ").split("<%").join("\t").replace(/((^|%>)[^\t]*)'/g, "$1\r").replace(/\t=(.*?)%>/g, "',$1,'").split("\t").join("');").split("%>").join("p.push('").split("\r").join("\\'") + "');}return p.join('');")
        }, encodeHTML: function (a) {
            return a && a.replace(/[&"'><]/g, function (a) {
                    return A[a]
                })
        }, decodeHTML: function (a) {
            return a && a.replace(/&[a-z]+;/gi, function (a) {
                    return p[a] || a
                }).replace(/&#(\d{2}|\d{4});/ig, function (a, e) {
                    return String.fromCharCode(e)
                })
        }, getAscLength: function (a) {
            for (var e = 0, b = a.length; b--;)e += 128 > a.charCodeAt(b) ? 1 : 2;
            return e
        }, cut: function (a, e, b) {
            for (var b = void 0 === b ? "..." : b, d = [], c = 0, i = a.length, p = 0, v; c <= e && !(c >= i); c++) {
                v = 128 > a.charCodeAt(c) ? 1 : 2;
                if (p + v > e) {
                    d.push(b);
                    break
                }
                p += v;
                d.push(a.charAt(c))
            }
            return d.join("")
        }, truncate: function (a, e, b) {
            b = void 0 === b ? "..." : b;
            return a.length > e ? a.slice(0, e - b.length) + b : a
        }, camelize: function (a) {
            return a.replace(e, F)
        }, hyphenate: function (a) {
            return a.replace(H, I)
        }, capitalize: function (a) {
            return a.replace(/\b[a-z]/g, function (a) {
                return a.toUpperCase()
            })
        }, escapeRegExp: u, has: r, params: function (a) {
            var e = a || f.location.search;
            if (!e)return null;
            "?" === e.charAt(0) && (e = e.slice(1));
            for (var a = {}, b = e.split("&"), c = -1, i, p, v; i = b[++c];) {
                e = i.split("=");
                p = e[0];
                v = e[1];
                try {
                    v = v ? decodeURIComponent(e[1].replace(/\+/g, "%20")) : -1 != i.indexOf("=") ? "" : !0
                } catch (k) {
                    v = "", t.error("Invalid decodeURIComponent: " + e[1])
                }
                a[p] ? (d(a[p]) || (a[p] = [a[p]]), a[p].push(v)) : a[p] = v
            }
            return a
        }, toQuery: function (e) {
            var b = [], d, c, i;
            for (d in e)if ((c = e[d]) && "object" === typeof c) {
                if ("number" === typeof c.length)for (i = c.length; i--;)b.push(null == c[i] ? d : d + "=" + encodeURIComponent("" + c[i]))
            } else b.push(null == c ? d : d + "=" + encodeURIComponent("" + c));
            return b.join("&").replace(a, "+")
        }, stripTags: function (a) {
            return a.replace(/<\/?[^>]+>/g, "")
        }, cleanHtml: function (a, e) {
            if ((a = a && a.replace(i, "") || "") && e) a = j(a, "&nbsp;"), a = j(a, "<br\\s*/?>", 1);
            return a
        }
    });
    var G = t.owns;
    t.declare("object", {
        map: x, owns: G, filter: function (a, e, b) {
            var d = [], c = -1, i;
            for (i in a)G(a, i) && e.apply(b, [a[i], i]) && (d[++c] = a[i]);
            return d
        }, keys: function (a) {
            return x(a, m)
        }, values: function (a) {
            return x(a, n)
        }
    });
    t.declare("array", {
        remove: function (a, e) {
            var b = a.indexOf(e);
            -1 !== b && a.splice(b, 1);
            return a
        }, find: function (a, e, b) {
            for (var d = a.length >>> 0; d--;)if (e.apply(b, [a[d], d]))return a[d];
            return null
        }, unique: function (a) {
            for (var e, b = -1, d = b, c = a.length >>> 0, i = []; ++b < c;)if (b in a && -1 === i.indexOf(e = a[b])) i[++d] = e;
            return i
        }
    });
    t.declare("date", {
        parse: function (a, e) {
            e || (e = "yyyy-MM-dd");
            var e = e.replace(/\W/g, ",").split(","), a = a.replace(/\D/g, ",").split(","), b = 2E3, d = 0, c = 1, i = 0, p = 0, v = 0, f = Number;
            t.each(e, function (e, k) {
                "" !== a[k] && !isNaN(a[k]) && (r(e, "y") && (b = f(a[k])), r(e, "M") && (d = f(a[k]) - 1), r(e, "d") && (c = f(a[k])), r(e, "h") && (i = f(a[k])), r(e, "m") && (p = f(a[k])), r(e, "s") && (v = f(a[k])), r(e, "w") && (v = f(a[k])))
            });
            return new Date(b, d, c, i, p, v)
        }, format: function (a, e) {
            var b = a.getFullYear(), d = a.getMonth() + 1, c = a.getDate(), i = a.getHours(), p = a.getMinutes(), v = a.getSeconds();
            switch (e) {
                case 10:
                    return "common_month_2" != i18n("common_month_2") ? i18n("common_date_format", b, i18n("common_month_" + d), c, i18n("common_week_" + a.getDay()), i18n("common_data_format_" + (12 > a.getHours() ? "am" : "pm")), 10 > i ? "0" + i : i, 10 > p ? "0" + p : p) : b + "\u5e74" + d + "\u6708" + c + "\u65e5(\u661f\u671f" + "\u65e5\u4e00\u4e8c\u4e09\u56db\u4e94\u516d".charAt(a.getDay()) + ") " + ["\u4e0a\u5348", "\u4e0b\u5348"][12 > a.getHours() ? 0 : 1] + (10 > i ? "0" + i : i) + ":" + (10 > p ? "0" + p : p);
                default:
                    return b + "-" + d + "-" + c + " " + i + ":" + p + ":" + v
            }
        }
    })
});
provide("r/oop", function (z) {
    function y(d, c, f) {
        return function () {
            var b = this[u], k;
            this[u] = f[d];
            k = c.apply(this, arguments);
            void 0 === b ? this[u] = b : delete this[u];
            return k
        }
    }

    var r = z("r/base"), u = "$super", j = r.global.Object, m = /xyz/.test(function () {
        return "xyz"
    }) ? RegExp(r.string.escapeRegExp(u) + "\\b") : /.*/, n = r.mixin, x = function (d) {
        return "function" === typeof d
    }, t = function (d) {
        return n(this, d, !0)
    }, f = function (d) {
        var c = this.prototype, f = this.superclass, b;
        for (b in d)d.hasOwnProperty(b) && (c[b] = x(d[b]) && x(f[b]) && m.test(d[b]) ? y(b, d[b], f) : d[b]);
        return this
    }, c = j.prototype.constructor, h = j.create || function () {
            function d() {
            }

            return function (c) {
                d.prototype = c;
                return new d
            }
        }(), w = function (d, f, l, b) {
        (!f || !d) && r.error("extend failed, verify dependencies");
        var k = f.prototype, s = h(k);
        d.prototype = s;
        s.constructor = d;
        d.superclass = k;
        f !== j && k.constructor === c && (k.constructor = f);
        l && n(s, l, !0);
        b && n(d, b, !0);
        return d
    }, l = function (d) {
        var c, f, b;
        if (d && "object" === typeof d) {
            b = d.length;
            if ("number" === typeof b)for (c = Array(b); b--;)c[b] = l(d[b]); else for (f in c = {}, d)d.hasOwnProperty(f) && (c[f] = l(d[f]));
            return c
        }
        return d
    }, s = function () {
    };
    s.prototype = {
        _disposed: !1, dispose: function () {
            this._disposed = !0
        }, toString: function () {
            return "[object " + (this.$name || "Object") + "]"
        }, instanceOf: function (d) {
            o = this;
            do if (o.constructor === d)return !0; while (o.constructor && (o = o.constructor.superclass));
            return !1
        }, call: function (d, c) {
            var f = this.constructor.superclass, b;
            if (f && x(b = f[d]))return b.apply(this, c)
        }
    };
    r.declare({
        klass: function (d, c, l) {
            var b, k;
            "string" !== typeof d && (l = c, c = d, d = null);
            if (!l) {
                if (!c)throw Error("class create failed, verify definitions");
                l = c;
                c = null
            }
            k = function () {
                var d = b._init || b.constructor;
                d && d !== k && d.apply(this, arguments)
            };
            c = c || s;
            b = w(k, c).prototype;
            b.$parent = c.prototype;
            d && (b.$name = d.split(".").pop(), b.$namespace = d, r.declare(d, k));
            k.methods = f;
            k.statics = t;
            k.toString = r.K("[class " + d + "]");
            d = typeof l;
            "object" === d ? k.methods(l) : "function" === d && l.apply(b, [k.superclass, k]);
            return k
        }, extend: w, create: h, clone: l
    })
});
provide("r/env", function (z, y) {
    var r = z("r/base").global || {}, u = r.document, j = r.navigator, m = j.userAgent, n = j.platform, j = r.RegExp, x = /\./g, t = function (c) {
        if (!c)return 0;
        var f = 0;
        return parseFloat(c.replace(x, function () {
            return 1 === f++ ? "" : "."
        }))
    }, f = {}, c, h = "unknow";
    if (/Windows|Win32/.test(m)) {
        if (h = "win", /Windows NT\s([^;]+)/.test(m))switch (j.$1) {
            case "5.0":
            case "5.1":
                h = "win2k";
                break;
            case "6.0":
                h = "winvista";
                break;
            case "6.1":
                h = "win7"
        }
    } else/Macintosh/.test(m) ? h = "mac" : "X11" === n ? h = "unix" : /rhino/i.test(m) ? h = "rhino" : "iPad" === n || "iPhone" === n || /i(?:Phone|Pad)/.test(m) ? h = "iOS" : /Linux/.test(m) && (h = "linux");
    f.os = h;
    /KHTML/.test(m) && (f.webkit = 1);
    (f.webkit = /AppleWebKit\/([^\s]*)/.test(m)) || (f.ie = /MSIE\s([^;]*)/.test(m)) || (f.ie = /MSIE([^;]*)/.test(m)) || (f.ie = /rv:([^\s]*)\) like Gecko/.test(m)) || (f.opera = /Opera[\s\/]([^\s]*)/.test(m)) || (f.gecko = /Gecko\/([^\s]*)/.test(m)) || (f.unknown = !0);
    n = j.$1;
    if (f.webkit) f.webkit = t(n), /Safari\/([^\s]*)/.test(m) && (h = "safari", c = "Version", /Chrome\/([^\s]*)/.test(m) && (h = "chrome", c = "Chrome"), f[h] = t((new j(c + "/([^s]*)")).test(m) && j.$1)); else if (f.gecko || !n) n = /rv:([^\s\)]*)/.test(m) && j.$1, /Firefox\/([^\s]*)/.test(m) && (f.firefox = t(j.$1));
    if (n = n || j.$1) f.version = t(n);
    if (f.ie && (f.ie = f.version, 8 <= f.ie && 5 !== u.documentMode && (f.ie = u.documentMode), 6 >= f.ie))try {
        u.execCommand("BackgroundImageCache", !1, !0)
    } catch (w) {
    }
    f.isStrict = "CSS1Compat" === u.compatMode;
    f.isFileAPISupported = !(!r.File || !r.FileList || !r.FileReader || !r.Blob);
    y(f, !0)
});
provide("cache", function (z, y) {
    z("r/base");
    var r = 0, u = {};
    y({
        set: function (j, m, n) {
            if (!j)throw Error("setting failed, invalid element");
            j = j["_ guid _"] || (j["_ guid _"] = ++r);
            j = u[j] || (u[j] = {});
            m && (j[m] = n);
            return j
        }, get: function (j, m, n) {
            if (!j)throw Error("getting failed, invalid element");
            j = j["_ guid _"] || (j["_ guid _"] = ++r);
            n = u[j] || n && (u[j] = {});
            return !n ? null : void 0 !== m ? n[m] || null : n
        }, has: function (j, m) {
            return null !== this.get(j, m)
        }, remove: function (j, m) {
            var n = "object" === typeof j ? j["_ guid _"] || (j["_ guid _"] = ++r) : j, x = u[n];
            if (!x)return !1;
            void 0 !== m ? delete x[m] : delete u[n];
            return !0
        }
    }, !0)
});
provide("event", function (z, y) {
    function r(b) {
        for (var d in b)if (b.hasOwnProperty(d))return !1;
        return !0
    }

    function u(b) {
        b = b || window.event;
        if (!b.guid) {
            b.guid = +new Date;
            b.target || (b.target = b.srcElement || c);
            3 === b.target.nodeType && (b.target = b.target.parentNode);
            !b.relatedTarget && b.fromElement && (b.relatedTarget = b.fromElement === b.target ? b.toElement : b.fromElement);
            for (var d in v)b[d] || (b[d] = v[d])
        }
        b.currentTarget || (b.currentTarget = this);
        var f;
        d = -1;
        var a = (l.get(this, "events", !0) || {})[b.type];
        if (a)for (; f = a[++d];)f = f.fn.call(f.scope, b), void 0 !== f && (b.result = f, !1 === f && b.stop())
    }

    function j(b, d, c, a) {
        var e = l.get(b, void 0, !0), k = e.events, v = e.handle;
        k || (e.events = k = {});
        v || (e.handle = v = function () {
            u.apply(v.elem, arguments)
        });
        v.elem = b;
        for (var h = -1, q, e = d.split(" "); d = e[++h];)f.env.firefox && "mousewheel" === d && (d = "DOMMouseScroll"), q = k[d], q || (q = k[d] = [], s(b, d, v)), q.some(function (a) {
            return a.fn == c
        }) || q.push({type: d, fn: c, scope: a || b});
        b = null
    }

    function m(b, c, k) {
        var a = l.get(b, void 0, !0), e = a.events, v, h, s = -1, q;
        if (e) {
            for (v = c.split(" "); c = v[++s];)if (f.env.firefox && "mousewheel" === c && (c = "DOMMouseScroll"), h = e[c]) {
                if (k)for (q = h.length; q--;)h[q].fn === k && h.splice(q, 1);
                h.length || (d(b, c, a.handle), delete e[c])
            }
            if (r(e)) {
                if (handle = a.handle) handle.elem = null;
                delete a.events;
                delete a.handle;
                r(a) && (c = l.get(b)) && r(c) && l.remove(b)
            }
        }
    }

    function n() {
        try {
            var b = l.getGlobalCache(), c, f, a, e, k;
            for (c in b)if (f = b[c], a = f.handle) {
                e = a.elem;
                for (k in f.events)d(e, k, a);
                delete f.handle;
                delete f.events;
                r(f) && l.remove(c)
            }
        } catch (v) {
            console.log(v.message)
        }
    }

    function x() {
        if (!B) {
            try {
                c.documentElement.doScroll("left")
            } catch (b) {
                setTimeout(x, 1);
                return
            }
            t()
        }
    }

    function t() {
        if (!B) {
            if (!c.body)return setTimeout(t, 13);
            d(window, "load", t);
            B = !0;
            if (k) {
                for (var b, f = 0; b = k[f++];)b.fn.call(b.scope);
                k = null
            }
        }
    }

    var f = z("r/base"), c = window.document, h = !!c.addEventListener, w = !!c.attachEvent, l = f.cache, s = h ? function (b, d, c) {
        b.addEventListener(d, c, !1)
    } : function (b, d, c) {
        b.attachEvent("on" + d, c)
    }, d = h ? function (b, d, c) {
        b.removeEventListener(d, c, !1)
    } : function (b, d, c) {
        b.detachEvent("on" + d, c)
    }, v = {
        stopPropagation: function () {
            this.cancelBubble = !0
        }, preventDefault: function () {
            this.returnValue = !1
        }, stop: function () {
            this.stopPropagation();
            this.preventDefault()
        }
    }, B = !1, b = !1, k = [], A = f.noop;
    h ? A = function () {
        c.removeEventListener("DOMContentLoaded", A, !1);
        t()
    } : w && (A = function () {
        "complete" === c.readyState && (c.detachEvent("onreadystatechange", A), t(), window.attachEvent("onunload", n))
    });
    y({
        on: function (b, d, c, a) {
            if (!b || "string" === typeof d && !c)throw Error("addListener failed, invalid element or callback");
            if ("object" === typeof d) {
                var e = d, a = c;
                for (d in e)j(b, d, e[d], a)
            } else j(b, d, c, a)
        }, un: function (b, d, c) {
            if (d)if ("object" === typeof d)for (d in c = d, c)m(b, d, c[d]); else m(b, d, c); else if (c = l.get(b, "events", !0))for (d in c)m(b, d)
        }, hover: function (b, d, c) {
            this.on(b, "mouseover", d);
            this.on(b, "mouseout", c)
        }, trigger: h ? function (b, d) {
            try {
                var f = c.createEvent("MouseEvents");
                f.initEvent(d, !0, !0);
                b.dispatchEvent(f)
            } catch (a) {
                console.log(a)
            }
        } : function (b, d) {
            try {
                b.fireEvent("on" + d)
            } catch (c) {
                console.log(c)
            }
        }, onReady: function (d, f) {
            if (!b)if (b = !0, "complete" === c.readyState) t(); else {
                if (h) c.addEventListener("DOMContentLoaded", A, !1); else if (w) {
                    c.attachEvent("onreadystatechange", A);
                    var v = !1;
                    try {
                        v = null == window.frameElement
                    } catch (a) {
                    }
                    c.documentElement.doScroll && v && x()
                }
                s(window, "load", t, !1)
            }
            f = f || c;
            B ? d.call(f) : k && k.push({fn: d, scope: f})
        }
    }, !0)
});
provide("dom", function (z, y) {
    function r(a, e) {
        return 1 !== a.nodeType || "string" !== typeof e ? !1 : !0
    }

    var u = z("r/base"), j = z("r/env"), m = u.global, n = m.document, x = n.documentElement, t = n.defaultView, j = j.ie, f = /<(?!area|br|col|embed|hr|img|input|link|meta|param)(([\w:]+)[^>]*)\/>/ig, c = /<([\w:]+)/, h = /<|&#?\w+;/, w = {
        option: [1, "<select>", "</select>"],
        legend: [1, "<fieldset>", "</fieldset>"],
        thead: [1, "<table>", "</table>"],
        tr: [2, "<table><tbody>", "</tbody></table>"],
        td: [3, "<table><tbody><tr>", "</tr></tbody></table>"],
        col: [2, "<table><tbody></tbody><colgroup>", "</colgroup></table>"],
        area: [1, "<map>", "</map>"],
        _default: [0, "", ""]
    }, l = Array.prototype.slice, s = function () {
        var a, e, b;
        a = document.createElement("div");
        a.className = "a";
        a.innerHTML = '<p style="color:red;"><a href="#" style="opacity:.45;float:left;">a</a></p>';
        a.setAttribute("class", "t");
        e = a.getElementsByTagName("p")[0];
        b = e.getElementsByTagName("a")[0];
        var d = "t" === a.className;
        e = /;/.test(e.style.cssText);
        var c = /^0.45$/.test(b.style.opacity);
        return {
            setAttr: d,
            cssText: e,
            opacity: c,
            classList: !!a.classList,
            cssFloat: !!b.style.cssFloat,
            getComputedStyle: !(!document.defaultView || !document.defaultView.getComputedStyle)
        }
    }(), d = s.getComputedStyle ? function (a) {
        return t.getComputedStyle(a, null)
    } : function (a) {
        return a.currentStyle
    }, v = {
        "for": "htmlFor",
        "class": "className",
        html: "innerHTML",
        readonly: "readOnly",
        maxlength: "maxLength",
        cellspacing: "cellSpacing",
        rowspan: "rowSpan",
        colspan: "colSpan",
        tabindex: "tabIndex",
        usemap: "useMap",
        frameborder: "frameBorder"
    }, B = {
        backgroundColor: 1,
        backgroundRepeat: 1,
        border: 1,
        borderBottom: 1,
        color: 1,
        cursor: 1,
        display: 1,
        filter: 1,
        font: 1,
        fontWeight: 1,
        height: 1,
        left: 1,
        lineHeight: 1,
        overflow: 1,
        overflowX: 1,
        padding: 1,
        position: 1,
        styleFloat: 1,
        textAlign: 1,
        top: 1,
        whiteSpace: 1,
        width: 1,
        verticalAlign: 1,
        zIndex: 1,
        tableLayout: 1,
        zoom: 1
    }, b = {fontWeight: 1, zIndex: 1, zoom: 1, opacity: 1}, x = x.hasAttribute ? function (a, e) {
        return a.hasAttribute && a.hasAttribute(e)
    } : function (a, e) {
        a = a.getAttributeNode(e);
        return !(!a || !a.specified && !a.nodeValue)
    }, k = function (a, e, b, d) {
        if (!a)return null;
        var k, d = d || document;
        "TABLE" === a.toUpperCase() && (a = "<table>" + (e.html || e.innerHTML || "") + "</table>");
        if ("<" === a.charAt(0)) {
            if (h.test(a)) {
                var a = a.replace(f, "<$1></$2>"), i = (c.exec(a) || ["", ""])[1].toLowerCase(), i = w[i] || w._default, l = i[0], d = d.createElement("div");
                for (d.innerHTML = i[1] + a + i[2]; l--;)d = d.lastChild;
                a = d.lastChild
            } else return d.createTextNode(a);
            e && (d = e.html ? "html" : e.innerHTML ? "innerHTML" : "") && delete e[d]
        } else a = d.createElement(a);
        if (e)for (k in e)d = a, i = k, l = e[k], i = v[i] || i, "className" === i || "innerHTML" === i ? d[i] = l : d.setAttribute(i, !0 === l ? i : l);
        if (b)for (k in b)a.style[k] = b[k];
        return a
    }, A, p, i, C;
    s.classList ? (A = function (a, e) {
        return r(a, e) ? a.classList.contains(e) : !1
    }, p = function (a, e) {
        var b = 0, d;
        if (r(a, e))for (e = e.split(" "); d = e[b++];)a.classList.add(d)
    }, i = function (a, e) {
        var b = 0, d;
        if (r(a, e))for (e = e.split(" "); d = e[b++];)a.classList.remove(d)
    }, C = function (a, e) {
        r(a, e) && a.classList.toggle(e)
    }) : (A = function (a, e) {
        return r(a, e) ? -1 != (" " + a.className + " ").indexOf(" " + e + " ") : !1
    }, p = function (a, e) {
        r(a, e) && !A(a, e) && (a.className += (a.className ? " " : "") + e)
    }, i = function (a, e) {
        r(a, e) && (a.className = a.className.replace(RegExp("\\b" + e + "\\b", "g"), ""))
    }, C = function (a, e) {
        A(a, e) ? i(a, e) : p(a, e)
    });
    y({
        getPos: function (a, e) {
            for (var b = a.ownerDocument, d = b.documentElement, b = b.body, e = e || b, c = 0, f = 0, k, g; a && a !== e && a !== b && a !== d;)k = a.offsetParent, g = k == e || k == b || k == d, c += a.offsetLeft - (k && !g ? k.scrollLeft : 0), f += a.offsetTop - (k && !g ? k.scrollTop : 0), a = k;
            return {x: c, y: f}
        }, isVisible: function (a) {
            var e;
            if (!a)return !1;
            for (; a && !("BODY" === a.nodeName);) {
                e = d(a);
                if ("none" === e.display || "hidden" === e.visibility)return !1;
                a = a.parentNode
            }
            return !0
        }, getStyle: function (a, e) {
            var b = d(a);
            return e ? (b = b[e], "auto" === b ? 0 : b) : b
        }, setCSSText: function (a, e) {
            var b = a.style, d = b.cssText || "";
            s.cssText || (d += ";");
            b.cssText = d + e
        }, create: k, node: function (a, e, b) {
            var d, c = {}, f = {};
            for (d in b)(B[d] ? f : c)[d] = b[d];
            e = k(e, c, f, a && a.ownerDocument);
            a && (a.appendChild(e), 11 === e.nodeType && (e = a.lastChild));
            return e
        }, next: function (a) {
            do a = a.nextSibling; while (a && 1 !== a.nodeType);
            return a
        }, prev: function (a) {
            do a = a.previousSibling; while (a && 1 !== a.nodeType);
            return a
        }, children: !j ? function (a) {
            return l.call(a.children)
        } : function (a) {
            for (var b = [], a = a.firstChild; a;)1 === a.nodeType && (b[b.length] = a), a = a.nextSibling;
            return b
        }, remove: function (a) {
            a.parentNode.removeChild(a)
        }, hasAttribute: x, attr: function (a, b, d) {
            var c = void 0 !== d, b = v[b] || b;
            if ("style" === b)return c && (a.style.cssText = "" + d), a.style.cssText;
            if (c) {
                if (b in a || void 0 !== a[b])return a[b] = d;
                "undefined" !== typeof a.setAttribute ? null === d ? a.removeAttribute(b) : a.setAttribute(b, !0 === d ? b : d) : a[b] = d
            } else return "undefined" !== typeof a.getAttribute && "boolean" !== typeof a[b] ? a.getAttribute(b) : a[b]
        }, getViewPort: function (a) {
            a = a || document.documentElement;
            return {x: a.scrollLeft, y: a.scrollTop, w: a.clientWidth, h: a.clientHeight}
        }, hasClass: A, addClass: p, removeClass: i, toggleClass: C, replaceClass: function (a, b, d) {
            i(a, b);
            p(a, d)
        }, contains: function (a, b) {
            return a.contains ? a.contains(b) : a === b || !!(a.compareDocumentPosition(b) & 16)
        }, setOpacity: function (a, b) {
            s.opacity ? a.style.opacity = 1 === b ? "" : "" + b : (a.style.filter = "alpha(opacity=" + 100 * b + ");", a.style.zoom = 1)
        }, getOpacity: function (a) {
            if (s.getComputedStyle)return style = m.getComputedStyle(a, null), opa = style.opacity, 1 < opa.length && (opa = opa.substr(0, 3)), parseFloat(opa);
            style = a.currentStyle;
            filter = style.filter;
            return 0 <= filter.indexOf("opacity=") ? parseFloat(filter.match(/opacity=([^)]*)/)[1]) / 100 : 1
        }, css: function (a, e, c) {
            if (void 0 === c)return (c = d(a)) ? c[e] : a.style[e];
            "number" == typeof c && !b[e] && (c += "px");
            a.style[e] = c
        }, getWH: function (a) {
            var b = d(a), a = parseInt(b.width, 10) || 0, b = parseInt(b.height, 10) || 0;
            return {w: a, h: b}
        }, setWH: function (a, b, d) {
            this.setCSSText(a, "width:" + b + "px;height:" + d + "px")
        }, hide: function (a, b) {
            b ? this.css(a, "visibility", "hidden") : this.css(a, "display", "none")
        }, show: function (a, b) {
            b ? this.css(a, "visibility", "visible") : this.css(a, "display", "")
        }, width: function (a, b) {
            if (void 0 === b)return this.css(a, "width");
            this.css(a, "width", b)
        }, height: function (a, b) {
            if (void 0 === b)return this.css(a, "height");
            this.css(a, "height", b)
        }, moveTo: function (a, b, d) {
            a.style.left = b + "px";
            a.style.top = d + "px"
        }, getForm: function (a, b) {
            var d;
            if (a)switch (a.tagName) {
                case "INPUT":
                    d = a.form;
                    break;
                case "FORM":
                    d = a;
                    break;
                case "A":
                case "SPAN":
                    for (; a = a.parentNode;)if ("FORM" === a.tagName) {
                        d = a;
                        break
                    }
            }
            return d || n.forms[b]
        }, ancestor: function (a, b, d, c) {
            var f = null;
            d && (f = !b || b(a) ? a : null);
            if (!(d = f))a:{
                for (d = "parentNode"; a && (a = a[d]);) {
                    if (1 === a.nodeType && (!b || b(a))) {
                        d = a;
                        break a
                    }
                    if (c && (c === a || "function" === typeof c && c(a)))break
                }
                d = null
            }
            return d
        }, addHTML: function (a, b) {
            if (u.env.gecko) {
                var d = a.ownerDocument.createRange();
                d.setStartBefore(a);
                d = d.createContextualFragment(b);
                a.appendChild(d)
            } else a.insertAdjacentHTML("BeforeEnd", b)
        }, insertHTML: function (a, b, d) {
            a = a || document.body;
            d = d ? d.toLowerCase() : "beforeend";
            if (a.insertAdjacentHTML)switch (d) {
                case "beforebegin":
                    return a.insertAdjacentHTML("BeforeBegin", b), a.previousSibling;
                case "afterbegin":
                    return a.insertAdjacentHTML("AfterBegin", b), a.firstChild;
                case "beforeend":
                    return a.insertAdjacentHTML("BeforeEnd", b), a.lastChild;
                case "afterend":
                    return a.insertAdjacentHTML("AfterEnd", b), a.nextSibling
            } else {
                var c = a.ownerDocument.createRange();
                switch (d) {
                    case "beforebegin":
                        return c.setStartBefore(a), b = c.createContextualFragment(b), a.parentNode.insertBefore(b, a), a.previousSibling;
                    case "afterbegin":
                        return a.firstChild ? (c.setStartBefore(a.firstChild), b = c.createContextualFragment(b), a.insertBefore(b, a.firstChild)) : a.innerHTML = b, a.firstChild;
                    case "beforeend":
                        return a.lastChild ? (c.setStartAfter(a.lastChild), b = c.createContextualFragment(b), a.appendChild(b)) : a.innerHTML = b, a.lastChild;
                    case "afterend":
                        return c.setStartAfter(a), b = c.createContextualFragment(b), a.parentNode.insertBefore(b, a.nextSibling), a.nextSibling
                }
            }
            throw'Illegal insertion point -> "' + d + '"';
        }, insertBefore: function (a, b) {
            b.parentNode.insertBefore(a, b)
        }, insertAfter: function (a, b) {
            var d = b.parentNode;
            d.lastChild == b ? d.appendChild(a) : d.insertBefore(a, b.nextSibling)
        }
    }, !0)
});
provide("selector", function (z, y) {
    function r(j, f, c) {
        function h(d) {
            var f = d.length;
            if (1 == f)return c ? d : d[0];
            if (1 < f)return d;
            if (0 == f)return null
        }

        function m(d, c, b) {
            for (var f = -1, l, p = -1, i = [], h = new x("(?:^|\\s+)" + b + "(?:\\s+|$)"); l = d[++f];) {
                var a;
                a:{
                    if (a = "className" == c ? l.className : l.getAttribute(c))if (b) {
                        if (h.test(a)) {
                            a = !0;
                            break a
                        }
                    } else {
                        a = !0;
                        break a
                    }
                    a = !1
                }
                a && (i[++p] = l)
            }
            return i
        }

        var l = /^([-\w]+)?\[([\w]+)(=(\w+))?\]/, f = f === u ? n : "string" === typeof f ? n.getElementById(f) : f;
        if (/^([-\w]+)?\.([-\w]+)/.test(j)) {
            var l = j.split("."), j = l[0], s = l[1], l = [];
            if (f.getElementsByClassName) {
                s = f.getElementsByClassName(s);
                if (j)for (var d = 0, f = s.length; d < f; d++)s[d].tagName.toLowerCase() == j && l.push(s[d]);
                return h(s)
            }
            j = f.getElementsByTagName(j || "*");
            return h(m(j, "className", s))
        }
        if (/^([\w\*]+)$/.test(j))return h(f.getElementsByTagName(j));
        if (l.test(j))return l = l.exec(j), j = f.getElementsByTagName(l[1] || "*"), h(m(j, l[2], l[4]))
    }

    var u, j = z("r/base"), m = j.global, n = m.document, x = m.RegExp;
    y(j.declare("dom", {
        $: function (j) {
            return "string" == typeof j ? document.getElementById(j) : j
        }, get: function (j, f) {
            return r(j, f)[0] || null
        }, query: r
    }))
});
provide("json", function (z, y) {
    function r(c) {
        t[c] || (t[c] = "\\u" + ("0000" + (+c.charCodeAt(0)).toString(16)).slice(-4));
        return t[c]
    }

    function u(f) {
        function d(f, b) {
            var k = f[b], h = typeof k, p = [], i, s, a, e;
            k && "object" === typeof k && "function" === typeof k.toJSON && (k = k.toJSON(b));
            k !== f[b] && (h = typeof k);
            if (null === k)return "null";
            switch (h) {
                case "object":
                    break;
                case "string":
                    return '"' + k.replace(n, r) + '"';
                case "number":
                    return isFinite(k) ? k + "" : "null";
                default:
                    return "" + k
            }
            for (i = l.length - 1; 0 <= i; --i)if (l[i] === k)throw Error("JSON.stringify. Cyclical reference");
            h = "[object Array]" === c.call(k) || "length" in k && k.slice;
            l.push(k);
            if (h)for (i = k.length - 1; 0 <= i; --i)p[i] = d(k, i) || "null"; else for (a in s = k, i = 0, s)s.hasOwnProperty(a) && (e = d(k, a)) && (p[i++] = '"' + a.replace(n, r) + '":' + e);
            l.pop();
            return h ? "[" + p.join(",") + "]" : "{" + p.join(",") + "}"
        }

        var l = [];
        return d({"": f}, "")
    }

    var j = z("r/base"), m = j.global, n = /[\\\"\x00-\x1f\x7f-\x9f\u00ad\u0600-\u0604\u070f\u17b4\u17b5\u200c-\u200f\u2028-\u202f\u2060-\u206f\ufeff\ufff0-\uffff]/g, x = /[\u0000\u00ad\u0600-\u0604\u070f\u17b4\u17b5\u200c-\u200f\u2028-\u202f\u2060-\u206f\ufeff\ufff0-\uffff]/g, t = {
        "\u0008": "\\b",
        "\t": "\\t",
        "\n": "\\n",
        "\u000c": "\\f",
        "\r": "\\r",
        '"': '\\"',
        "\\": "\\\\"
    }, f = j.global.JSON, c = Object.prototype.toString, u = (f = "[object JSON]" === c.call(f) && f) ? f.stringify : u, h = function (c, d) {
        function l(b, c) {
            var f, i, h = b[c];
            if (h && "object" === typeof h)for (f in h)Object.prototype.hasOwnProperty.call(h, f) && (i = l(h, f), void 0 !== i ? h[f] = i : delete h[f]);
            return d.call(b, c, h)
        }

        if ("" === c)return null;
        if (f.parse)try {
            return f.parse(c, d)
        } catch (h) {
            return j.error(h), null
        }
        var b, c = "" + c;
        x.lastIndex = 0;
        x.test(c) && (c = c.replace(x, function (b) {
            return "\\u" + ("0000" + b.charCodeAt(0).toString(16)).slice(-4)
        }));
        if (/^[\],:{}\s]*$/.test(c.replace(/\\(?:["\\\/bfnrt]|u[0-9a-fA-F]{4})/g, "@").replace(/"[^"\\\n\r]*"|true|false|null|-?\d+(?:\.\d*)?(?:[eE][+\-]?\d+)?/g, "]").replace(/(?:^|:|,)(?:\s*\[)+/g, "")))return b = m.eval.call(m, "(" + c + ")"), "function" === typeof d ? l({"": b}, "") : b;
        j.error(new SyntaxError("JSON.parse"));
        return null
    }, w = /^<[\s\S]*?>(?={)/, l = /(})<[\s\S]*?>$/;
    y({
        eval: function (c) {
            var d;
            if (d = c) d = (d = "" + c) ? j.string.cleanHtml(d).replace(w, "").replace(l, "$1") : "";
            return (c = d) ? h(c) : null
        }, parse: h, stringify: f ? f.stringify : u
    }, !0)
});
provide("io", function (z, y) {
    function r(d, l) {
        var l = m.merge(l, {
            type: "text",
            method: "POST",
            encode: "UTF-8",
            timeout: 15E3,
            success: h,
            failure: h
        }), j = !1 !== l.async, b = l.method, k = l.type, n = l.encode, p = l.timeout, i = l.params, r = l.scope, a = l.success, e = l.failure, b = b.toUpperCase();
        i && "object" == typeof i && (i = c(i));
        "GET" === b && i && (d += (-1 == d.indexOf("?") ? "?" : "&") + i);
        var w = s();
        if (w) {
            var t = !1, x;
            j && 0 < p && (x = f(function () {
                t = !0;
                w.abort()
            }, p));
            w.onreadystatechange = function () {
                4 == w.readyState && (t ? e(w, "request timeout") : (u(w, k, a, e, r), clearTimeout(x)))
            };
            w.open(b, d, j);
            "POST" == b && w.setRequestHeader("Content-type", "application/x-www-form-urlencoded;charset=" + n);
            w.send(i);
            return w
        }
    }

    function u(d, c, f, b, k) {
        var l = d.status, h;
        if (200 <= l && 300 > l) {
            switch (c) {
                case "text":
                    h = d.responseText;
                    break;
                case "json":
                    h = function (c) {
                        c && (c = c.replace(w[0], "").replace(w[1], ""));
                        try {
                            return m.json.parse(c)
                        } catch (f) {
                            try {
                                return (new Function("return " + c))()
                            } catch (a) {
                                try {
                                    return n.eval.call(n, "(" + c + ")")
                                } catch (e) {
                                    b(d, "parse json error", e)
                                }
                            }
                        }
                    }(d.responseText);
                    break;
                case "xml":
                    h = d.responseXML
            }
            void 0 !== h && f.call(k, h)
        } else b(d, d.status);
        d = null
    }

    function j(d, c) {
        var f = x.createElement(d), b;
        for (b in c)c.hasOwnProperty(b) && f.setAttribute(b, c[b]);
        return f
    }

    var m = z("r/base"), n = m.global, x = n.document, t = x.head || x.getElementsByTagName("head")[0] || x.documentElement, f = n.setTimeout, c = m.string.toQuery, h = m.noop, w = [/^<script[^\>]*>[\s\S]*<\/script>/gim, /<script[^\>]*>[\s\S]*<\/script>$/gim], l = {}, s = n.XMLHttpRequest ? function () {
        try {
            return new n.XMLHttpRequest
        } catch (d) {
        }
    } : function () {
        try {
            return new n.ActiveXObject("Microsoft.XMLHTTP")
        } catch (d) {
        }
    };
    l.request = r;
    m.each(["text", "json", "xml"], function (d) {
        l[d] = function (c, f) {
            f = f || {};
            f.type = d;
            return r(c, f)
        }
    });
    l.script = function (d, c, f, b) {
        b = "string" === typeof b ? {charset: b} : b || {};
        m.mixin(b, {type: "text/javascript", async: "true", src: d});
        var l = j("script", b), s = m.isFunction(c) ? f ? m.bind(c, f) : c : h;
        l.onload = l.onreadystatechange = function () {
            if (!l.readyState || /loaded|complete/.test(l.readyState)) l.onload = l.onreadystatechange = null, t && l.parentNode && t.removeChild(l), l = void 0, s()
        };
        l.onerror = function () {
            var b = Error("Syntax error or http error: ");
            if (s) s(b); else throw b;
            l.onload = l.onreadystatechange = null;
            t && l.parentNode && t.removeChild(l)
        };
        t.insertBefore(l, t.firstChild)
    };
    l.css = function () {
        function d(b, d) {
            b.attachEvent ? b.attachEvent("onload", d) : f(function () {
                c(b, d)
            }, 0)
        }

        function c(b, d) {
            if (!d.isCalled) {
                var h = !1;
                if (l) b.sheet && (h = !0); else if (b.sheet)try {
                    b.sheet.cssRules && (h = !0)
                } catch (j) {
                    1E3 === j.code && (h = !0)
                }
                h ? f(d, 1) : f(function () {
                    c(b, d)
                }, 1)
            }
        }

        var l = m.env.webkit;
        return function (b, c, f) {
            var l = x.createElement("link"), i = c;
            i && (f && (i = m.bind(c, f)), d(l, i));
            l.rel = "stylesheet";
            l.href = b;
            t.appendChild(l);
            return l
        }
    }();
    y(l, !0)
});
provide("util", function (z, y) {
    function r(f) {
        var c = [], h, j, l, s;
        switch (f.nodeType) {
            case 1:
                h = f.tagName;
                c.push("<" + h);
                s = -1;
                for (j = f.attributes; l = j[++s];)"style" == l.nodeName && f.style ? c.push(" " + l.nodeName + '="' + f.style.cssText + '"') : l.nodeValue && c.push(" " + l.nodeName + '="' + l.nodeValue + '"');
                if (f.hasChildNodes()) {
                    s = -1;
                    j = f.childNodes;
                    for (c.push(">"); l = j[++s];)c.push(r(l));
                    c.push("</" + h + ">")
                } else t.test(h) ? c.push(" />") : c.push("></" + h + ">");
                break;
            case 3:
                c.push(f.nodeValue);
                break;
            case 4:
                c.push("<![CDATA[" + f.data + "]]\>")
        }
        return c.join("")
    }

    var u = z("r/base"), j = u.global, m = j.document, n = u.later, x = j.clearTimeout, t = /^(?:area|br|col|embed|hr|img|input|link|meta|param)$/i;
    y({
        form2json: function (f, c, h, j) {
            c = c || ["INPUT", "TEXTAREA", "BUTTON", "SELECT"];
            "string" === typeof f && (f = m.forms[f]);
            if (!f || 1 !== f.nodeType)return !1;
            for (var l = {}, s = c.length >> 0, d; s--;) {
                d = f.getElementsByTagName(c[s]);
                for (var v = 0, n = d.length, b; v < n; v++) {
                    var k = d[v], r = j;
                    b = {};
                    var p = k.getAttribute("name") || k.getAttribute("id");
                    if (p && (r || !k.disabled))switch (k.tagName) {
                        case "INPUT":
                            r = k.getAttribute("type");
                            "radio" === r || "checkbox" === r ? k.checked ? (b.name = p, b.value = k.value) : b = !1 : "reset" === r || "submit" === r || "image" === r ? b = !1 : p ? (b.name = p, b.value = k.value) : b = !1;
                            break;
                        case "SELECT":
                            if (k.multiple) {
                                k = k.options;
                                b.name = p;
                                b.value = [];
                                p = 0;
                                for (r = k.length; p < r; p++)k[p].selected && b.value.push(k[p].value)
                            } else b.name = p, b.value = k.value;
                            break;
                        case "TEXTAREA":
                            b.name = p;
                            b.value = k.value;
                            break;
                        default:
                            b.name = p, b.value = k.value || k.getAttribute("value") || k.innerHTML || !1
                    } else b = !1;
                    b && !(h && "" === b.value) && (l[b.name] ? u.isArray(l[b.name]) ? l[b.name].push(b.value) : l[b.name] = [l[b.name]].concat(b.value) : l[b.name] = b.value)
                }
            }
            return l
        }, node2str: r, parseXML: function (f) {
            var c, h;
            try {
                j.DOMParser ? (h = new DOMParser, c = h.parseFromString(f, "text/xml")) : (c = new ActiveXObject("Microsoft.XMLDOM"), c.async = "false", c.loadXML(f))
            } catch (m) {
                c = void 0
            }
            (!c || !c.documentElement || c.getElementsByTagName("parsererror").length) && u.error("Invalid XML: " + f);
            return c
        }, cookie: function (f, c, h, j) {
            if (void 0 === c) {
                for (var f = f + "=", c = m.cookie.split(";"), h = 0, l = c.length; h < l; h++) {
                    for (j = c[h]; " " === j.charAt(0);)j = j.substring(1, j.length);
                    if (0 === j.indexOf(f))return decodeURIComponent(j.substring(f.length, j.length))
                }
                return null
            }
            l = "";
            h && (l = new Date, l.setTime(l.getTime() + 864E5 * h), l = "; expires=" + l.toGMTString());
            m.cookie = f + "=" + c + l + "; path=/" + (j ? ";domain=" + j : "")
        }, timer: function (f, c, h) {
            var j = n(function s() {
                !0 === f.call(h) ? j = n(s, c, this) : (x(j), j = null)
            }, c, h);
            return j
        }, convertTime: function (f) {
            if (isNaN(f) || 0 > f)return "00:00:00";
            var c = Math.floor(f / 3600), h = Math.floor(f % 3600 / 60), f = Math.floor(f % 60);
            10 > c && (c = "0" + c);
            10 > h && (h = "0" + h);
            10 > f && (f = "0" + f);
            return c + ":" + h + ":" + f
        }, hex2rgb: function (f) {
            for (var f = f.substring(1), f = f.toLowerCase(), c = [], h = 0; 3 > h; h++)c[0] = f.substr(2 * h, 2), c[3] = "0123456789abcdef", c[1] = c[0].substr(0, 1), c[2] = c[0].substr(1, 1), c[20 + h] = 16 * c[3].indexOf(c[1]) + c[3].indexOf(c[2]);
            return "rgb(" + c[20] + "," + c[21] + "," + c[22] + ")"
        }, dateOf: function (f, c) {
            var f = parseInt(f), c = parseInt(c), h = "", j = "", l = new Date(f), s = l.getDay(), d = l.getFullYear(), v = l.getMonth(), m = l.getDate(), b = new Date(c), l = b.getHours(), k = b.getMinutes(), r = b.getDate(), p = b.getDay(), i = b.getMonth(), b = b.getFullYear(), n = (new Date(d, v, m, 0, 0, 0)).getTime(), m = (new Date(d, v, m, 23, 59, 59)).getTime(), a = (new Date(n - 864E5 * (0 == s ? s + 1 : s - 1))).getTime(), s = (new Date(m + 864E5 * (7 - s))).getTime(), e = (new Date(a - 6048E5)).getTime(), t = (new Date(e + 6048E5 - 1E3)).getTime(), u = (new Date(s + 1)).getTime(), x = (new Date(s + 6048E5)).getTime(), q = (new Date(d, v, 1)).getTime(), v = (new Date((new Date(n)).getFullYear(), v + 1, 1)).getTime(), v = (new Date(v - 1E3)).getTime();
            switch (p) {
                case 0:
                    j = "\u5468\u65e5";
                    break;
                case 1:
                    j = "\u5468\u4e00";
                    break;
                case 2:
                    j = "\u5468\u4e8c";
                    break;
                case 3:
                    j = "\u5468\u4e09";
                    break;
                case 4:
                    j = "\u5468\u56db";
                    break;
                case 5:
                    j = "\u5468\u4e94";
                    break;
                case 6:
                    j = "\u5468\u516d"
            }
            if (c <= s && c >= a) 0 > f - c ? h = c >= n && c <= m ? "\u4eca\u5929" : c <= m + 864E5 && c > m ? "\u660e\u5929" : c <= m + 1728E5 && c > m + 864E5 ? "\u540e\u5929" : "\u672c" + j : 0 < f - c ? h = c >= n && c <= m ? "\u4eca\u5929" : c <= n - 864E5 && c < n ? "\u6628\u5929" : c <= m - 1728E5 && c < m + 864E5 ? "\u524d\u5929" : "\u672c" + j : f == c && (h = "\u4eca\u5929"); else if (c <= t && c >= e)switch (p) {
                case 0:
                    h = "\u4e0a\u5468\u65e5";
                    break;
                case 1:
                    h = "\u4e0a\u5468\u4e00";
                    break;
                case 2:
                    h = "\u4e0a\u5468\u4e8c";
                    break;
                case 3:
                    h = "\u4e0a\u5468\u4e09";
                    break;
                case 4:
                    h = "\u4e0a\u5468\u56db";
                    break;
                case 5:
                    h = "\u4e0a\u5468\u4e94";
                    break;
                case 6:
                    h = "\u4e0a\u5468\u516d"
            } else if (c <= x && c >= u)switch (p) {
                case 0:
                    h = "\u4e0b\u5468\u65e5";
                    break;
                case 1:
                    h = "\u4e0b\u5468\u4e00";
                    break;
                case 2:
                    h = "\u4e0b\u5468\u4e8c";
                    break;
                case 3:
                    h = "\u4e0b\u5468\u4e09";
                    break;
                case 4:
                    h = "\u4e0b\u5468\u56db";
                    break;
                case 5:
                    h = "\u4e0b\u5468\u4e94";
                    break;
                case 6:
                    h = "\u4e0b\u5468\u516d"
            } else h = c <= v && c >= q ? "\u672c\u6708" + r + "\u65e5" : d == b ? i + 1 + "\u6708" + r + "\u65e5" + j : b + "\u5e74" + (i + 1) + "\u6708" + r + "\u65e5" + j;
            0 > f - c ? c >= n && c <= m ? h = "\u4eca\u5929" : c <= m + 864E5 && c > m ? h = "\u660e\u5929" : c <= m + 1728E5 && c > m + 864E5 && (h = "\u540e\u5929") : 0 < f - c ? c >= n && c <= m ? h = "\u4eca\u5929" : c >= n - 864E5 && c < n ? h = "\u6628\u5929" : c >= n - 1728E5 && c < n - 864E5 && (h = "\u524d\u5929") : f == c && (h = "\u4eca\u5929");
            return 6 > l ? h + "\u51cc\u6668" : 6 <= l && 12 > l ? h + "\u65e9\u4e0a" : 12 <= l && 13 > l ? h + "\u4e2d\u5348" : 13 == l ? 30 > k ? h + "\u4e2d\u5348" : h + "\u4e0b\u5348" : 14 <= l && 18 > l ? h + "\u4e0b\u5348" : h + "\u665a\u4e0a"
        }
    }, !0)
});
provide("util/i18n", function (z, y) {
    var r = function (r, j) {
        var m = "", n = Array.prototype.slice.apply(arguments), x = n.length - 1;
        n.shift();
        try {
            m = sinamail_local[r]
        } catch (t) {
            window.console && console.log("\u56fd\u9645\u5316\u8d44\u6e90\u6587\u4ef6\u672a\u52a0\u8f7d\u6210\u529f\uff01")
        }
        return (m || r).replace(/\{(\d)\}/g, function (f, c) {
            return 0 <= c && c < x ? n[c] : "{" + c + "}"
        })
    };
    window.i18n = r;
    y({
        get: r, html: function (u) {
            return (u || "").replace(/\{\{(\w+)\}\}(\(([^\(\)]|\/\(|\/\))*[^\/]\))?/g, function (j, m, n) {
                if (n) {
                    n = n.replace(/\/\(/g, "(").replace(/\/\)/g, ")");
                    try {
                        n = eval(n.replace(/^\(/g, "[").replace(/\)$/g, "]"))
                    } catch (u) {
                        for (var n = n.replace(/^\(/, "").replace(/\)$/, "").split(","), j = 0, t = n.length; j < t; j++)n[j] = n[j].replace(/^['"]/, "").replace(/['"]$/, "")
                    }
                }
                return r.apply(null, [m].concat(n))
            })
        }
    })
});
provide("util/template", function (z, y) {
    function r(c, f, d) {
        for (var f = w[f], h = -1, j = Number.MAX_VALUE, b, k; b = f[++h];)b = c.indexOf(b.tag, d), -1 !== b && b < j && (k = f[h], k.p = j = b);
        return k || {tag: "#tag#", len: 0, p: -1}
    }

    function u(c, f) {
        var d, h = 0, j = 0, b = !1, k = [], m, p, f = f || "";
        k.push("function(" + f + "){");
        k.push("var __sb = [];");
        m = r(c, "start", 0);
        for (p = {tag: "%--\>", len: 4, p: -4}; -1 !== m.p;) {
            h = m.p + m.len;
            j = p.p + p.len;
            m.p > j && (b ? (d = k.pop(), k.push(d.substr(0, d.length - 2) + "+" + t(c.substring(j, m.p)) + "" + d.substr(d.length - 2))) : k.push("__sb.push(" + t(c.substring(j, m.p)) + ");"));
            p = r(c, "end", h);
            j = p.p + p.len;
            if (-1 !== p.p)switch (c.charAt(h)) {
                case "!":
                    f || (b = !1, k[0] = c.substring(h + 1, p.p - 1) + "{");
                    break;
                case "=":
                    b = !0;
                    d = k.pop();
                    k.push(d.substr(0, d.length - 2) + ("[" === d.charAt(d.length - 3) ? "" : "+") + c.substring(h + 1, p.p) + d.substr(d.length - 2));
                    break;
                default:
                    b = !1, k.push(c.substring(h, p.p))
            } else return 'start tag:"' + m.tag + '" not match with end tag: "' + p.tag + '"';
            m = r(c, "start", j)
        }
        0 <= j && j < c.length && k.push("__sb.push(" + t(c.substr(j)) + ");");
        k.push('return __sb.join("");');
        k.push("}");
        return eval("[" + k.join("\n") + "]")[0]
    }

    var j = z("r/base"), m = j.util, n = j.noop, x = Array.prototype.slice, t = j.string.inspect, f = m.parseXML, c = m.node2str, h = z("util/i18n"), w = {
        start: [{
            tag: "<\!--%",
            len: 5,
            p: -1
        }, {tag: "(%", len: 2, p: -1}], end: [{tag: "%--\>", len: 4, p: -1}, {tag: "%)", len: 2, p: -1}]
    }, m = j.klass("util.TemplateEngine", {
        _init: function () {
            this._h = {}
        }, add: function (c, f, d) {
            var h = this._h;
            if (j.isArray(c))for (d = c.length; d--;)f = c[d], h[f.name] || (h[f.name] = f); else h[c] || (h[c] = {
                name: c,
                type: f,
                data: d
            })
        }, item: function (c) {
            var f = this._h[c];
            if (!f)throw Error('template "' + c + '" not exist.');
            f.inited || (c = f.data, c = f.data = "xml" == f.type ? h.html(c.replace(/>\s\s*?</g, "><").replace(/\s\s+?/g, " ")) : c.replace(/>\s\s*?</g, "><").replace(/\s\s+?/g, " "), "asp" === f.type && (f.fn = u(c, f.params) || n, delete f.params), f.inited = !0);
            return f
        }, get: function (c) {
            c = this.item(c);
            c.data = h.html(c.data);
            return "xml" === c.type ? f(c.data) : c.data
        }, invoke: function (c) {
            var f = this.item(c), d = f.data;
            switch (f.type) {
                case "tpl":
                    d = this.callTpl(d, arguments[1]);
                    break;
                case "asp":
                    d = f.fn.apply(null, x.call(arguments, 1))
            }
            return h.html(d)
        }, callTpl: function (c, f) {
            if (!f)return c;
            var d = this;
            return c.replace(/\{([$=])(\w+)\}/g, function (c, h, b) {
                return "$" === h ? void 0 !== (h = f[b]) ? h : c : d.get(b + ".tpl")
            })
        }, render: function (c, f) {
            c.innerHTML = this.invoke.apply(this, x.call(arguments, 1))
        }, render2: function (c, f) {
            var d = this.invoke.apply(this, x.call(arguments, 1));
            return c.appendChild(j.dom.create(d))
        }, appendTo: function (c, f, d) {
            var h;
            3 < arguments.length ? (h = x.call(arguments, 3), h.unshift(f), h = this.invoke.apply(this, h)) : h = this.invoke(f);
            h = j.dom.create(h);
            for (var m in d)h.style[m] = d[m];
            c && c.appendChild(h);
            return h
        }, getInnerHTML: function (f) {
            for (var h = [], d = f.childNodes, j = -1; f = d[++j];)h.push(c(f));
            return h.join("")
        }
    });
    y(m)
});
provide("util/lazyload", function (z, y) {
    y(function (r) {
        function u(d, c) {
            var f = r.createElement(d), b;
            for (b in c)c.hasOwnProperty(b) && f.setAttribute(b, c[b]);
            return f
        }

        function j(d) {
            var c = h[d], f, b;
            c && (f = c.callback, b = c.urls, b.shift(), w = 0, b.length || (f && f.call(c.context, c.obj), h[d] = null, l[d].length && n(d)))
        }

        function m() {
            var d = navigator.userAgent;
            f = {async: !0 === r.createElement("script").async};
            (f.webkit = /AppleWebKit\//.test(d)) || (f.ie = /MSIE/.test(d)) || (f.opera = /Opera/.test(d)) || (f.gecko = /Gecko\//.test(d)) || (f.unknown = !0)
        }

        function n(d, n, s, b, k) {
            var w = "css" === d, p = [], i, y, a;
            f || m();
            if (n)if (n = "string" === typeof n ? [n] : n.concat(), w || f.async || f.gecko || f.opera) l[d].push({
                urls: n,
                callback: s,
                obj: k,
                context: b
            }); else for (i = 0, y = n.length; i < y; ++i)l[d].push({
                urls: [n[i]],
                callback: i === y - 1 ? s : null,
                obj: k,
                context: b
            });
            if (!h[d] && (a = h[d] = l[d].shift())) {
                c || (c = r.head || r.getElementsByTagName("head")[0]);
                n = a.urls;
                for (i = 0, y = n.length; i < y; ++i)(function (b, c) {
                    w ? c = f.gecko ? u("style") : u("link", {
                        href: b,
                        rel: "stylesheet"
                    }) : (c = u("script", {src: b}), c.async = !1);
                    c.setAttribute("charset", "utf-8");
                    !document.addEventListener && !w ? c.onreadystatechange = function () {
                        /loaded|complete/.test(c.readyState) && (c.onreadystatechange = null, j(d), c = null)
                    } : w && (f.gecko || f.webkit) ? f.webkit ? (a.urls[i] = c.href, t()) : (c.innerHTML = '@import "' + b + '";', x(c)) : c.onload = c.onerror = function () {
                        c.onload = c.onerror = null;
                        j(d);
                        c = null
                    };
                    p.push(c)
                })(n[i]);
                for (i = 0, y = p.length; i < y; ++i)n = p[i], w ? c.appendChild(n) : c.insertBefore(n, c.firstChild)
            }
        }

        function x(c) {
            var f;
            try {
                f = !!c.sheet.cssRules
            } catch (h) {
                w += 1;
                200 > w ? setTimeout(function () {
                    x(c)
                }, 50) : f && j("css");
                return
            }
            j("css")
        }

        function t() {
            var c = h.css, f;
            if (c) {
                for (f = s.length; 0 <= --f;)if (s[f].href === c.urls[0]) {
                    j("css");
                    break
                }
                w += 1;
                200 > w ? setTimeout(t, 50) : j("css")
            }
        }

        var f, c, h = {}, w = 0, l = {css: [], js: []}, s = r.styleSheets;
        return {
            css: function (c, f, h, b) {
                n("css", c, f, h, b)
            }, js: function (c, f, h, b) {
                n("js", c, f, h, b)
            }
        }
    }(window.document))
});
define("r/core", "r/base,r/lang,r/oop,r/env,cache,event,dom,selector,json,io,util,util/i18n".split(","), function (z) {
    return z
});