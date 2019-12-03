import pandas as pd
import numpy as np

df = pd.read_excel('E:/PycharmProjects/6-1/missing_data_processed.xlsx',header=None)

# 计算电量趋势采用最小二乘法，计算K值，由于取前后5天为统计窗口，则以第6天的数据为首位数据，倒数第5天的数据为末尾数据。

def calculate_k(df):
    rows, cols = df.shape
    tmp_list = []
    for col in range(cols):
        tmp_list1 = []
        for row in range(5, rows - 5):

            # print(row)
            j_begin = row - 5
            # print(j_begin)
            j_end = row + 5
            f_mean = df.iloc[j_begin:j_end, col].mean()
            # print(f_mean)
            l_mean = np.mean(range(j_begin + 1, j_end + 1))
            total_top = 0
            total_under = 0
            for d in range(j_begin + 1, j_end + 1):
                f_tmp = df.iloc[d - 1, col]
                # print(f_tmp)
                total_top += (f_tmp - f_mean) * (d - l_mean)
                # print(total_top)
                total_under += (d - l_mean) ** 2
                # print(total_under)
            k = total_top / total_under
            tmp_list1.append(k)
        tmp_list.append(tmp_list1)

    df_D = pd.DataFrame(tmp_list).T
    df_D = df_D.diff()
    df_D = np.where(df_D > 0, 0, 1)
    return pd.DataFrame(df_D)
# 将时间添加进去,并进行逆透视，即可得到书中专家样本数据的格式




