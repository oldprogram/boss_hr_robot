

# 1.介绍

这个是用 python 写的，自动搜索 boss 直聘上目标简历的简陋机器人：

https://www.cnblogs.com/zjutlitao/p/13782277.html#top


# 2.环境

安装依赖：

```
pip3 install PyUserInput
pip3 install pyperclip
```

运行：

到 BOSS 直聘推荐牛人页面，点开一个牛人简历，之后运行脚本：（浏览器窗口和terminal窗口并排放，terminal窗口占10%比例宽度）

```
python3 robot.py
```

程序需要手动或自动标记4个点：简历的左上角、打招呼按钮、对话框输入文字处、关闭对话框按钮（当前程序是默认关闭自动标记的，可以在代码中打开注释：get_key_pos）

<br>

**注：**     
1）如果出现： Pyperclip could not find a copy/paste mechanism for your system. 错误，请参考：https://pyperclip.readthedocs.io/en/latest/#:~:text=You%20may%20get%20an%20error,paste%20mechanism%20for%20your%20system.&text=You%20can%20fix%20this%20by,to%20install%20the%20xclip%20utility.

