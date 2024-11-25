def processlog(logs):
    """
    Processes a log string and returns a list of dictionaries representing each log entry.

    Args:
    logs (str): Multiline string containing log entries separated by newlines.

    Returns:
    list: A list of dictionaries with keys "timestamp", "severity", and "message".
    """
    res = []
    lines = logs.split("\n")
    for line in lines:
        words = line.split(" ", 1)
        message = words[1]
        timestamp, severity, message = message.split("-",2)
        record = {
            "timestamp" : timestamp,
            "severity" : severity,
            "message" : message,
        }
        res.append(record)

    return res

{
    "timestamp": "<timestamp>",
    "severity": "<severity>",
    "message": "<message>"
}


# 测试代码
if __name__ == "__main__":
    logs = """20170627 00:00:31-ERROR-Internet down
20170627 00:01:31-CRITICAL-Alien attack
20170627 00:02:31-PANIC-Zombies"""

    # 处理日志
    records = processlog(logs)

    # 打印每条记录
    for record in records:
        print(record)
