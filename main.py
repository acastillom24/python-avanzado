import pymysql


if __name__ == "__main__":
    connect = pymysql.Connect(
        host="localhost", port=3306, user="root", passwd="", db="pythondb"  # 127.0.0.1
    )

    print("Successful Connection!")
