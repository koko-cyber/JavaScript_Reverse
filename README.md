# JavaScript 逆向 - 基础	

😅😥👶😃🧥🐶🍏⚽️✂🈲🚗⌚️❤️🏁▶

<br>

！！！ 如有侵权请联系，本人会在第一时间删除，本文以学习为目的，切勿用于非法途径🈲



## 常见加密、解密、调试手段

<br>

- API 参数加密 发起请求时会校验附带的参数，如 token、sign等

- Cookie 参数解密 cookie 由 JavaScript 动态生成

<br>

- 加密

  - ob 混淆：开源的混淆工具
  
  
  - webpack： 一种打包方式
  
  
  - worker：多线程调试
  
  
  - async：异步调试
  
  
  - jsl 加速乐：加速乐
  
  
  - sojsonv6：基于 ob 混淆
  - tls
  - 瑞数
  - 极验
  - 5秒盾
  
  
  
  

<br>

- 解密

  - hook

  - AST

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





案例网址：[Scrape | Movie](https://spa6.scrape.center/)

通过抓包发现，数据接口由 token 值是经过加密的

<br>

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

知道所有参数的加密方式后就可以扣 JS 代码，或者直接用 Python 还原加密算法



