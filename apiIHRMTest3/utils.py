import app
import json


# 编写断言代码函数
def assert_common(self, response, http_code, success, code, message):
    self.assertEqual(http_code, response.status_code)  # 断言响应状态码
    self.assertEqual(success, response.json().get("success"))  # 断言success
    self.assertEqual(code, response.json().get("code"))  # 断言code
    self.assertIn(message, response.json().get("message"))  # 断言message


def read_login_data():
    data_path = app.BASE_DIR + "/data/login_data.json"
    with open(data_path, mode='r', encoding='utf-8') as f:
        # 加载文件为json格式的数据
        jsonData = json.load(f)
        # 遍历文件取出其中数据并保存在列表中
        p_list = []
        for data in jsonData:
            mobile = data.get("mobile")
            password = data.get("password")
            http_code = data.get("http_code")
            success = data.get("success")
            code = data.get("code")
            message = data.get("message")
            p_list.append( (mobile, password, http_code, success, code, message) )
    print(p_list)
    return p_list


def read_add_emp_data():
    path = app.BASE_DIR + "/data/employee.json"
    # 打开文件
    with open(path, mode='r', encoding='utf-8') as f:
        jsonData = json.load(f)
        # 由于employee.json是一个字典数据，那么我们可以使用字典的get方法获取其中数据
        add_emp_data = jsonData.get("add_emp")
        result_list = []
        username = add_emp_data.get("username")
        mobile = add_emp_data.get("mobile")
        success = add_emp_data.get("success")
        code = add_emp_data.get("code")
        message = add_emp_data.get("message")
        http_code = add_emp_data.get("http_code")
        result_list.append( (username, mobile, success, code,message,http_code) )

    print("读取添加员工的数据： ", result_list)
    return result_list

def read_query_emp_data():
    path = app.BASE_DIR + "/data/employee.json"
    # 打开文件
    with open(path, mode='r', encoding='utf-8') as f:
        # 加载Json数据文件
        jsonData = json.load(f)
        # 由于employee.json是一个字典数据，那么我们可以使用字典的get方法获取
        result_list = []
        query_emp_data = jsonData.get("query_emp")
        success = query_emp_data.get("success")
        code = query_emp_data.get("code")
        message = query_emp_data.get("message")
        http_code = query_emp_data.get("http_code")
        result_list.append( (success, code, message, http_code) )
    print("查询员工数据为：", result_list)
    return result_list

def read_modify_emp_data():
    path = app.BASE_DIR + "/data/employee.json"
    # 打开文件
    with open(path, mode='r', encoding='utf-8') as f:
        # 加载Json数据文件
        jsonData = json.load(f)
        # 由于employee.json是一个字典数据，那么我们可以使用字典的get方法获取
        result_list = []
        modify_emp_data = jsonData.get("modify_emp")
        username = modify_emp_data.get("username")
        success = modify_emp_data.get("success")
        code = modify_emp_data.get("code")
        message = modify_emp_data.get("message")
        http_code = modify_emp_data.get("http_code")
        result_list.append( (username, success, code, message, http_code) )
    print("修改员工数据为：", result_list)
    return result_list

def read_delete_emp_data():
    path = app.BASE_DIR + "/data/employee.json"
    # 打开文件
    with open(path, mode='r', encoding='utf-8') as f:
        # 加载Json数据文件
        jsonData = json.load(f)
        # 由于employee.json是一个字典数据，那么我们可以使用字典的get方法获取
        result_list = []
        delete_emp_data = jsonData.get("delete_emp")
        success = delete_emp_data.get("success")
        code = delete_emp_data.get("code")
        message = delete_emp_data.get("message")
        http_code = delete_emp_data.get("http_code")
        result_list.append((success, code, message, http_code))
    print("删除员工数据为：", result_list)
    return result_list

if __name__ == '__main__':
    # main函数的作用？
    # 防止调用这个模块或者类时，自动执行代码
    read_delete_emp_data()