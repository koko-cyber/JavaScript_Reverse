# JavaScript 逆向 - 基础	

😅😥👶😃🧥🐶🍏⚽️✂🈲🚗⌚️❤️🏁▶

<br>

！！！ 如有侵权请联系，本人会在第一时间删除，本文以学习为目的，切勿用于非法途径🈲





## 常见加密、解密、调试手段

<br>

- API 参数加密 发起请求时会校验附带的参数，如 token、sign等

- Cookie 参数解密 cookie 由 JavaScript 动态生成

<br>

- [ ] 加密

  - [x] [ob 混淆：开源的混淆工具](https://github.com/koko-cyber/JavaScript_Reverse#ob-%E6%B7%B7%E6%B7%86%E7%AF%87)
  
  
    - [x] [webpack： 一种打包方式](https://github.com/koko-cyber/JavaScript_Reverse#webpack-%E7%AF%87)
  
  
    - [ ] worker：多线程调试
  
  
    - [ ] async：异步调试
  
  
    - [ ] jsl 加速乐：加速乐
  
  
    - [ ] sojsonv6：基于 ob 混淆
  
  
    - [ ] [tls指纹](https://github.com/koko-cyber/JavaScript_Reverse#tls)
  
  
    - [ ] 瑞数
  
  
    - [ ] 极验
  
  
    - [ ] 5秒盾
  
  
    - [ ] 字体反爬
  
  
  
  
  

<br>

- [ ] 解密

  - [ ] hook

  - [ ] AST

<br>

<br>



## ob 混淆篇

官网：https://obfuscator.io/

ob 混淆是常见的一种混淆方式，关于介绍可以去百度或者官网了解

<br>

混淆前

```javascript
function hi() {
	console.log("Hello World!");
}
hi();
```

<br>

混淆后部分截图

![image](https://github.com/koko-cyber/JavaScript_Reverse/blob/main/picture/image-20220421205700908.png?raw=true)

<br>

如果是利用开源库进行混淆的 JS 可以用下面解混淆

 [Tsaiboss/decodeObfuscator: 免安装一键还原Obfuscator混淆过的代码 (github.com)](https://github.com/Tsaiboss/decodeObfuscator)

<br>

也可以利自行编写 AST 代码，这里暂时不展开讨论

<br>

ob混淆案例网址：aHR0cHM6Ly9qb2JzLjUxam9iLmNvbS8=

此网址的 cookie 设置了有效时间，打上 script 断点后很容易找到生成 cookie 的函数入口

![image](https://github.com/koko-cyber/JavaScript_Reverse/blob/main/picture/image-20220422141408444.png?raw=true)

![image](https://github.com/koko-cyber/JavaScript_Reverse/blob/main/picture/image-20220422141952842.png?raw=true)

<br>

可以发现 name 是一个固定的字符串我们可以定死，而 x 参数通过堆栈中得知 x = arg2

arg2 由 _0x23a392 得来，arg1 参数是由服务器发的固定字符串

![image](https://github.com/koko-cyber/JavaScript_Reverse/blob/main/picture/image-20220422142442341.png?raw=true)

<br>

为了方便我们看代码我们可以利用 decodeObfuscator 解混淆，解混淆前后

![image](https://github.com/koko-cyber/JavaScript_Reverse/blob/main/picture/image-20220422142832558.png?raw=true)



<br>

我们可以更清楚的去分析函数之间的关系

![image](https://github.com/koko-cyber/JavaScript_Reverse/blob/main/picture/image-20220422142955089.png?raw=true)

<br>

分析结束后就是扣代码的流程了，这里就不多赘述了，直接贴上运行结果

![image](https://github.com/koko-cyber/JavaScript_Reverse/blob/main/picture/image-20220422143355073.png?raw=true)

<br>

<br>

## webpack 篇

<br>

webpack 是前端打包常用手段，并不是加密手段，只是经过 webpack 打包的 js 对逆向有一定的影响

中文官网：[概念 | webpack 中文网 (webpackjs.com)](https://www.webpackjs.com/concepts/)

<br>

webpack 标识

```javascript

!(function(e) {
    //分发器
    function u(n) {
        .....
        return e[n].call(t.exports, t, t.exports, u),
        t.l = !0,
        t.exports
}({
// 模块
'test': function(){},

}));
```

<br>

经过 webpack 打包的代码一般长这样，由分发器和待加载的模块组成

![image](https://github.com/koko-cyber/JavaScript_Reverse/blob/main/picture/image-20220422150332156.png?raw=true)

<br>

<br>

案例网址：[Scrape | Movie](https://spa6.scrape.center/)

通过抓包发现，数据接口由 token 值是经过加密的

<br>

经过查找堆栈可以发现加密函数入口，我们在此处下断点刷新页面，断住后单步调试跟进去

![image](https://github.com/koko-cyber/JavaScript_Reverse/blob/main/picture/image-20220422151257413.png?raw=true)



<br>

跟进去后我们就可以找到该分发器，然后将该分发器导出方便我们使用里面的模块

![image](https://github.com/koko-cyber/JavaScript_Reverse/blob/main/picture/image-20220422151429261.png?raw=true)

扣下来，将其他无用的函数注释掉，定义一个 window（当然什么变量都行只是我习惯了）

```javascript
var window = global;

window._0x3ff111\_ = _0x3ff111;  //将分发器导出
```

<br>

![image-20220422151555774](https://github.com/koko-cyber/JavaScript_Reverse/blob/main/picture/image-20220422151555774.png?raw=true)

<br>

扣完后可以测试一下该分发器有没有效果

![image-20220422153622477](https://github.com/koko-cyber/JavaScript_Reverse/blob/main/picture/image-20220422153622477.png?raw=true)

<br>

接下来就是扣加密所需的模块了

比如在控制台输出 _0x2fa7bd['a'] 发现是这个函数，它所在的模块是 ‘7d92’

![image-20220422152051489](https://github.com/koko-cyber/JavaScript_Reverse/blob/main/picture/image-20220422152051489.png?raw=true)

将他整个扣下来，缺什么模块就扣什么

![image](https://github.com/koko-cyber/JavaScript_Reverse/blob/main/picture/image-20220422152615458.png?raw=true)

<br>

也可以直接全部复制下来，建议用到什么模块就扣什么模块。我偷个懒

![image-20220422153847349](https://github.com/koko-cyber/JavaScript_Reverse/blob/main/picture/image-20220422153847349.png?raw=true)

<br>

调用模块还原加密逻辑

_0x2fa7bd 是由 "7d92" 模块加载来的

![image](https://github.com/koko-cyber/JavaScript_Reverse/blob/main/picture/image-20220422154051923.png?raw=true)





## worker 多线程调试篇

<br>

<br>

## Jsl 加速乐篇

<br>

<br>

## sojson 篇

<br>

sojsonv6：sojsonv6调试案例 aHR0cDovL3d3dy5wYmMuZ292LmNuLw==

<br>

<br>

## async 异步篇

<br>

异步调试，不知道有没有 js 异步调试技巧的文章分享一下... (待补充)

<br>

async：异步调试案例 aHR0cHM6Ly9tdXNpYy4xNjMuY29tLw==

<br>

登录（手机号-密码）：加密参数 encSecKey parmas

<br>

分析思路：输入手机号、密码、点击登录

<br>

![image-20220421141420597.png](https://github.com/koko-cyber/JavaScript---/blob/main/picture/image-20220421141420597.png?raw=true)

可以看见该 post 请求下面有两个加密参数 **params** 和 **encSecKey**

<br>

查看堆栈打上断点进入调试

<br>

![image](https://github.com/koko-cyber/JavaScript---/blob/main/picture/image-20220421143552838.png?raw=true)

<br>

打上断点之后我们可以看见参数 **d**

![image](https://github.com/koko-cyber/JavaScript---/blob/main/picture/image-20220421142136225.png?raw=true)

<br>

通过观察可以发现 **d** 这个参数是 **b** 这个包的加密参数 **d**

![image](https://github.com/koko-cyber/JavaScript---/blob/main/picture/image-20220421142711181.png?raw=true)

<br>

点击该按钮跳过该断点时出现 **params** 

![image](https://github.com/koko-cyber/JavaScript---/blob/main/picture/image-20220421144011047.png?raw=true)

然后我们查看堆栈，发现在进入这个 **g.asrsea** 这个函数时 **params** 参数生成

且 **g.asrsea** 这个函数传入 **f** 这个值，**f** 里面包含了 手机号、密码、和一个 **checktoken** 这几个关键信息

<br>

![image](https://github.com/koko-cyber/JavaScript---/blob/main/picture/image-20220421144817135.png?raw=true)

<br>

单步调试跟进去，发现加密函数，此时 password 和 checktoken 是未知的

![image](https://github.com/koko-cyber/JavaScript---/blob/main/picture/image-20220421145238863.png?raw=true)

重新点击登录，重新打上断点，刚刚我们是在 **f** 这里我们继续往下看，找到 checktoken 和 password 的生成方式

![image](https://github.com/koko-cyber/JavaScript---/blob/main/picture/image-20220421150034193.png?raw=true)

<br>

当我们找到 **m.ia** 时我们可以看到 **checktoken** 是 **dc** 这个函数通过 **r** 和 **x** 参数加密得来

<br>

而 **r** 参数 由 **bc** 这个函数得来，至此就差 **password** 加密了

![image](https://github.com/koko-cyber/JavaScript---/blob/main/picture/image-20220421151105878.png?raw=true)

<br>

和上面一样继续找堆栈就可以发现 **password** 是由 MD5 加密得来

![image](https://github.com/koko-cyber/JavaScript---/blob/main/picture/image-20220421151704924.png?raw=true)



## TLS 指纹



TLS 指纹又叫 SSl 指纹，或者 JA3 指纹，是根据客户端向服务端发送的 `Client Hello` 计算得到

在TLS握手中还有服务端响应的`Server Hello`，也有特征，可以得到JA3S指纹

又由于服务端会根据不同的`Client Hello`响应不同的`Server Hello`，根据这个又可以得到JARM指纹

<br>

简单来说

> JA3是标记客户端的指纹
>
> JA3S是标记服务端的指纹
>
> JARM是升级版的JA3S指纹



ja3：[JA3 is a standard for creating SSL client fingerprints in an easy to produce and shareable way](https://github.com/salesforce/ja3)

[TLS Fingerprinting with JA3 and JA3S | by John Althouse | Salesforce Engineering](https://engineering.salesforce.com/tls-fingerprinting-with-ja3-and-ja3s-247362855967)



推荐文章：[深度剖析ja3指纹及突破 (qq.com)](https://mp.weixin.qq.com/s/-i730kN_f5sIvh6kj7k5JQ)
