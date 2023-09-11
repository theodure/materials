#开始要写项目了，对于创建整体项目集和项目文件的编写需要注意什么呢？

# 对于每个新建立的编程文件，在文件开头建议引用以下格式：

# Starting to write a project,
# what do I need to be aware of for creating the overall project set and writing the project file?

# For each newly created programming file, the
# following format is recommended to be quoted at the beginning of the file:

#------------------------------------------------------------------------------------------------
'''
@File:
@copyright:
@Description: 
@Author:
@Date:
@modified by:
@modified on:
@modified content:

'''
#------------------------------------------------------------------------------------------------

# 推崇的项目层级结构
# Promoted project hierarchy

#------------------------------------------------------------------------------------------------
# package
# --__init__.py
# --manage.py (main)  #程序主入口
# --src_dir(my_project)   # scr文件夹  在package文件夹下
# -----crm_dir   在src文件夹下
# ----------admin.py
# ----------app.py
# ----------models.py
# ----------tests.py
# ----------views.py
# -----pro_dir  在src文件夹下
# ----------__init__.py
# ----------setting.py
# ----------urls.py
# ----------wsgi.py

#------------------------------------------------------------------------------------------------
# package
# --__init__.py
# --manage.py (main) # main entry point of the programme
# ---src_dir(my_project) # scr folder in package folder
# -----crm_dir in src folder
# ----------admin.py
# ----------app.py
# ----------models.py
# ----------tests.py
# ----------views.py
# -----pro_dir in src folder
# ----------__init__.py
# ----------setting.py
# ----------urls.py
# ----------wsgi.py
#------------------------------------------------------------------------------------------------


# 编写文件后，还可以输出一个测试报告

# 终端输入语句：coverage html -d coverage_result  
#             利用coverage输出一个测试报告，输出结果为 coverage_result文件名的文件
#             这个是一个简明的测试报告，它有3个html文件；其中就可以看到所有内容的检测报告，是否检测覆盖全。
# After writing the file, you can also output a test report

# Terminal input statement: coverage html -d coverage_result  
# Use coverage to output a test report to a file with the name of the coverage_result file.
# This is a concise test report, it has 3 html files; 
# which will be able to see all the content of the test report, whether the test coverage full.