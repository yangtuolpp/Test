# test
# 2024/4/17
import requests
import time

# def log():
#     res=requests.get('http://127.0.0.1:9999/demo1')
#     print(res.text)
# log()
host = "http://127.0.0.1:9999"


def mock_get():
    url = f'{host}/api/order/create/'
    payload = {
        "user_id": "sq001",
        "goods_id": "9090",
        "num": 2,
        "amount": 10.1
    }
    res = requests.post(url, json=payload)
    return res.json()['order_id']


# 获取订单结果接口
# 概念：频率＋超时
def select(order_id, interval=3, timeout=10):
    '''

    :param order_id: 订单ID
    :param interval: 频率3秒一次
    :param timeout: 20秒超时
    :return: 查询结果
    '''
    url = f'{host}/api/order/get_result/'
    payload = {"order_id": order_id}
    # 1-查询开始计时
    start_time = time.time()  # 阻塞
    # 2-结束时间，开始时间+超时时间
    end_time = start_time + timeout
    count = 0  # 计算查询次数
    while time.time() < end_time:
        res = requests.get(url, params=payload)
        count = count + 1
        print('第{}次查询，结果是：'.format(count))
        if res.text:  # 如果在超时的范围内，提前查询到结果，直接退出循环
            break
        else:
            print(f'第{count}次查询结果是---','没有处理完成请稍等')
        time.sleep(interval)
    return res.text

import threading

if __name__ == '__main__':
    id = mock_get()
    result=select(mock_get())
    print(result)
    # # 创建线程
    # T1 = threading.Thread(target=select, args=(id,))
    # # 2-守护线程,意味着主线程结束，子线程结束
    # T1.deamon = True
    # # 3-启动线程
    # T1.start()
    # for i in range(5):
    #     time.sleep(1)
    #     print("我正在执行其他操作", i)
