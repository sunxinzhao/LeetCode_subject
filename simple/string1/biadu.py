# coding=utf-8
'''
输入：
    1) station.json: 站点坐标信息，示例如下：
    [
        {
            "x":400000.000,
            "y":4000000.000,
            "name":"第一站"
        },
        {
            "x":400100.000,
            "y":4000100.000,
            "name":"第二站"
        },
        {
            "x":400200.000,
            "y":4000100.000,
            "name":"第三站"
        },
        {
            "x":400200.000,
            "y":4000200.000,
            "name":"第四站"
        }
    ]
    2) record.json: 记录路线坐标，示例如下：
    [
        {
            "timestamp" : 1234567890000,
            "x":400000.000,
            "y":4000000.000,
        },
        {
            "timestamp" : 1234567890010,
            "x":400000.003,
            "y":4000000.004,
        },
        {
            "timestamp" : 1234567890020,
            "x":400000.022,
            "y":4000000.019,
        },
        {
            "timestamp" : 1234567890030,
            "x":400100.000,
            "y":4000100.000,
        },
        {
            "timestamp" : 1234567890040,
            "x":400100.022,
            "y":4000100.000,
        },
        {
            "timestamp" : 1234567890050,
            "x":400200.000,
            "y":4000100.000,
        },
        {
            "timestamp" : 1234567890040,
            "x":400200.000,
            "y":4000100.022,
        },
        {
            "timestamp" : 1234567890050,
            "x":400200.000,
            "y":4000200.000,
        }
    ]
输出：
    每两站点间的里程/时长/平均速度。
    打印出如下格式：
    "station【站点名】->station【站点名】distance:【数字】m, time:【数字】s, average speed: 【数字】m/s."

说明：
    1) 时间戳为13位整数毫秒级时间戳；
    2) 坐标(x,y)为墨卡托坐标系，可以认为是平面直角坐标系，单位为米；
    3) record.json的实际路线经过为：第一站->第二站->第三站->第四站->第一站；
    4) 不考虑坐标误差，认为坐标重合为停站；
    5) 不考虑路线交叉重合；
    6) 站点可能停车等待，此等待时间不计算在时长内；路线上也可能停车等待，但此时间计算在时长内；
    7) 路线非直线行进，故而不能以站点间直线距离作为站点里程；
        由于record采集密度较高，可使用累加每两条记录点的直线距离方式计算总距离；

主函数定义：
def calcStationAverageSpeed(station_file_path, record_file_path):
'''

import json
import math


def calcStationAverageSpeed(station_file_path, record_file_path):
    # 读取站点信息
    with open(station_file_path) as file_obj:
        station_data = file_obj.read()
    station_list = json.loads(station_data)

    # 读取行车记录信息
    with open(record_file_path, "r") as f:
        data = f.read()
    record_list = json.loads(data)
    record_site = 0  # 行车记录读到的位置

    for i in range(len(station_list) - 1):
        start_station_site = 0  # 开始站记录的位置
        end_station_site = 0  # 下一站记录的位置
        station_distance = 0  # 站点间的距离
        for j in range(record_site, len(record_list) - 1):
            start_station = station_list[i]  # 开始站信息
            end_station = station_list[i + 1]  # 下一站信息

            # 确定开始站点的位置
            if record_list[j].get('x') == start_station.get('x') and record_list[j].get(
                    'y') == start_station.get('y') and record_list[j + 1].get('x') != start_station.get('x') and \
                    record_list[j + 1].get('y') != start_station.get('y'):
                start_station_site = j
                continue

            # 计算距离
            distance = get_distance(record_list[j].get('x'), record_list[j].get('y'), record_list[j + 1].get('x'),
                                    record_list[j + 1].get('y'))
            station_distance += distance

            # 确定结束站点的位置
            if record_list[j].get('x') != end_station.get('x') and record_list[j].get(
                    'y') != end_station.get('y') and record_list[j + 1].get('x') == end_station.get('x') and \
                    record_list[j + 1].get('y') == end_station.get('y'):
                end_station_site = j
                record_site = j  # 记录行车记录读到的位置
                break

        # 计算时间
        start_time = record_list[start_station_site].get('timestamp', 0)
        end_time = record_list[end_station_site].get('timestamp', 0)
        use_time = end_time - start_time
        station1_name = station_list[i].get('name')
        station2_name = station_list[i + 1].get('name')
        if use_time:
            ave_speed = station_distance / use_time
        else:
            ave_speed = '无穷大'

        print("station【{}】->station【{}】distance:【{}】m, time:【{}】s, average speed: 【{}】m/s.".format(station1_name,
                                                                                                   station2_name,
                                                                                                   station_distance,
                                                                                                   use_time, ave_speed))


def get_distance(x1, y1, x2, y2):
    return round(math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2)), 2)


if __name__ == "__main__":
    station_file_path = '/Users/sunxinzhao/station.txt'
    record_file_path = '/Users/sunxinzhao/record.txt'
    calcStationAverageSpeed(station_file_path, record_file_path)
