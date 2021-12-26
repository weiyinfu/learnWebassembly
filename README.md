# 学习Webassembly

webassembly中文网：http://webassembly.org.cn/


# Python
https://pyodide.org/en/stable/usage/quickstart.html

pyodide的原理：将Python源代码与常用科学计算包的源代码一起使用emscripten进行编译生成一个运行时。这个运行时大概有20M。  

pyodide团队提出了集成Python的四个层级：
* 第一级，调用python代码获取控制台输出
* 第二级，交互式地调用python代码
* 第三级，dom操作与python打通
* 第四级，js与python可以进行ndarray等库的打通

pyodide快速学习示例。
https://alpha.iodide.io/notebooks/300/
# Lua

# C/C++
emscripten:
https://emcc.zcopy.site/docs/introducing_emscripten/about_emscripten/
# Rust
wasm