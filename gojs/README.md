# 运行步骤
* IDEA设置：打开Preference/Go/Vendoring&BuildTags，OS设置为js，arch设置为wasm
* 编译：`make one`
* 准备js：`python prepare.py`
* 运行并打开浏览器：`http-server -p80`，访问`localhost/one/