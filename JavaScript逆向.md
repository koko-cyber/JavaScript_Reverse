# JavaScript 逆向 - 基础





## 常见加密、解密、调试手段



API 参数加密 发起请求时会校验附带的参数，如 token、sign等

Cookie 参数解密 cookie 由 JavaScript 动态生成



ob 混淆：开源的混淆工具

webpack： 一种打包方式

worker：多线程调试

async：异步调试

jsl 加速乐：加速乐

sojsonv6：基于 ob 混淆



hook

AST



## ob 混淆篇

官网：https://obfuscator.io/

ob 混淆是常见的一种混淆方式，关于介绍可以去百度或者官网了解



混淆前

![image-20220421161133168.png (1554×420) (raw.githubusercontent.com)](https://raw.githubusercontent.com/koko-cyber/JavaScript---/main/picture/image-20220421161133168.png?token=GHSAT0AAAAAABTA6WMVXJSXKHZMKIS7ESFIYTBD7XQ)

混淆后部分截图

![image-20220421161230992.png (2774×1092) (raw.githubusercontent.com)](https://raw.githubusercontent.com/koko-cyber/JavaScript---/main/picture/image-20220421161230992.png?token=GHSAT0AAAAAABTA6WMUNQVYVFECBKMOHFLSYTBEBMA)



如果是利用开源库进行混淆的 JS 可以用下面解混淆

 [Tsaiboss/decodeObfuscator: 免安装一键还原Obfuscator混淆过的代码 (github.com)](https://github.com/Tsaiboss/decodeObfuscator)













## webpack 篇





## worker 多线程调试篇





## Jsl 加速乐篇





## sojson 篇



sojsonv6：sojsonv6调试案例 [中国人民银行 (pbc.gov.cn)](http://www.pbc.gov.cn/)



打上 script 断点之后可以发现 这是一个经过 sojsonv6 加密的网站

![image-20220421152915876](C:\Users\29434\AppData\Roaming\Typora\typora-user-images\image-20220421152915876.png)



## async 异步篇



async：异步调试案例 [网易云音乐 (163.com)](https://music.163.com/)

网易云音乐登录（手机号-密码）：加密参数 encSecKey parmas

异步调试，不知道有没有 js 异步调试技巧的文章分享一下...

分析思路：输入手机号、密码、点击登录



![image-20220421141420597.png (1918×1055) (raw.githubusercontent.com)](https://raw.githubusercontent.com/koko-cyber/JavaScript---/main/picture/image-20220421141420597.png?token=GHSAT0AAAAAABTA6WMV4S75LCMBBKXMZSOEYTBDXUQ)

可以看见该 post 请求下面有两个加密参数 **params** 和 **encSecKey**



查看堆栈打上断点进入调试

​	

![image-20220421143552838.png (1920×772) (raw.githubusercontent.com)](https://raw.githubusercontent.com/koko-cyber/JavaScript---/main/picture/image-20220421143552838.png?token=GHSAT0AAAAAABTA6WMUAZHOW25V5Z65THKCYTBD2AA)





打上断点之后我们可以看见参数 **d**

![image-20220421142136225.png (1920×1080) (raw.githubusercontent.com)](https://raw.githubusercontent.com/koko-cyber/JavaScript---/main/picture/image-20220421142136225.png?token=GHSAT0AAAAAABTA6WMU2FNPD54XOJHFCYS2YTBDYZQ)



通过观察可以发现 **d** 这个参数是 **b** 这个包的加密参数 **d**

![image-20220421142711181.png (1912×739) (raw.githubusercontent.com)](https://raw.githubusercontent.com/koko-cyber/JavaScript---/main/picture/image-20220421142711181.png?token=GHSAT0AAAAAABTA6WMU3LNBHH47SKGAHAJAYTBDZYA)



点击该按钮跳过该断点时出现 **params** 

![image-20220421144011047.png (1918×1055) (raw.githubusercontent.com)](https://raw.githubusercontent.com/koko-cyber/JavaScript---/main/picture/image-20220421144011047.png?token=GHSAT0AAAAAABTA6WMUSUMSYY6BIUXG2TRMYTBD3BA)

然后我们查看堆栈，发现在进入这个 **g.asrsea** 这个函数时 **params** 参数生成

且 **g.asrsea** 这个函数传入 **f** 这个值，**f** 里面包含了 手机号、密码、和一个 **checktoken** 这几个关键信息



![image-20220421144817135.png (1918×1055) (raw.githubusercontent.com)](https://raw.githubusercontent.com/koko-cyber/JavaScript---/main/picture/image-20220421144817135.png?token=GHSAT0AAAAAABTA6WMVPIO4TXZOWRJGFLMUYTBD25A)





单步调试跟进去，发现加密函数，此时 password 和 checktoken 是未知的

![image-20220421145238863.png (1918×1055) (raw.githubusercontent.com)](https://raw.githubusercontent.com/koko-cyber/JavaScript---/main/picture/image-20220421145238863.png?token=GHSAT0AAAAAABTA6WMVHLG2YOMZIDGTOJCCYTBD3YA)

重新点击登录，重新打上断点，刚刚我们是在 **f** 这里我们继续往下看，找到 checktoken 和 password 的生成方式

![image-20220421150034193.png (1918×857) (raw.githubusercontent.com)](https://raw.githubusercontent.com/koko-cyber/JavaScript---/main/picture/image-20220421150034193.png?token=GHSAT0AAAAAABTA6WMUP35WBXEWGCFX5LV2YTBD4KA)





当我们找到 **m.ia** 时我们可以看到 **checktoken** 是 **dc** 这个函数通过 **r** 和 **x** 参数加密得来



而 **r** 参数 由 **bc** 这个函数得来，至此就差 **password** 加密了

![image-20220421151105878](C:\note\study\js逆向\picture\image-20220421151105878.png)



和上面一样继续找堆栈就可以发现 **password** 是由 MD5 加密得来

![image-20220421151704924.png (1918×1055) (raw.githubusercontent.com)](https://raw.githubusercontent.com/koko-cyber/JavaScript---/main/picture/image-20220421151704924.png?token=GHSAT0AAAAAABTA6WMUJ2LVWBC7JBUV2RDQYTBD5SQ)

知道所有参数的加密方式后就可以扣 JS 代码，或者直接用 Python 还原加密算法



