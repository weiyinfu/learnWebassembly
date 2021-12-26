# 学习Webassembly
webassembly简称wasm。 
webassembly中文网：http://webassembly.org.cn/


# Python
https://pyodide.org/en/stable/usage/quickstart.html

pyodide的原理：将Python源代码与常用科学计算包的源代码一起使用emscripten进行编译生成一个Python运行时。这个运行时大概有20M。  

pyodide团队提出了集成Python的四个层级：
* 第一级，调用python代码获取控制台输出
* 第二级，交互式地调用python代码
* 第三级，dom操作与python打通
* 第四级，js与python可以进行ndarray等库的打通

pyodide快速学习示例。
https://alpha.iodide.io/notebooks/300/
# Lua

# C/C++
emscripten是C/C++编译成wasm的编译器。  
https://emcc.zcopy.site/docs/introducing_emscripten/about_emscripten/

# Rust
Python、Lua、Java等语言需要运行时，而Go、Rust、C/C++等没有运行时。以后如果浏览器把Python、Lua、Java的运行时打包在浏览器中，这些脚本语言就会获得更大的优势。  
Rust的优势在于生成的wasm文件更小、运行速度更快。  