import argparse
import pymysql

# 连接 Doris
conn = pymysql.connect(
    host='127.0.0.1',   # Doris 的 FE 或 BE 地址
    port=9030,          # Doris 的默认 MySQL 端口
    user='root',        # 用户名
    password='',        # 密码
    database='test_db'    # 数据库名
)

def main():
    # 创建 ArgumentParser 对象
    parser = argparse.ArgumentParser(description="Python script with --base_FORD argument")

    # 添加 --base_FORD 参数
    parser.add_argument('--base_FORD', type=str, help='Specify the base_FORD value', required=True)

    # 解析命令行参数
    args = parser.parse_args()

    # 使用解析到的参数
    base_ford_value = args.base_FORD
    print(f"The value of base_FORD is: {base_ford_value}")


    # 创建游标
    cursor = conn.cursor()

    # 打开文件并逐行读取SQL语句
    with open(base_ford_value, 'r') as file:
        for line in file:
            # 去除每行的空白字符（如换行符等）
            sql = line.strip()
            if sql:
                try:
                    cursor.execute(sql)  # 执行SQL语句
                    conn.commit()  # 提交事务
                    print(f"执行SQL语句: {sql}")
                except Exception as e:
                    print(f"执行SQL语句时出错: {e}")

    # 关闭连接
    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()
