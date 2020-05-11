"""Unit 6 Assignment 2 - John Paul Aguilar"""
import json
import requests
from matplotlib import pyplot as plt

MAX_DATE = 20200225
US_POP = 328200200


def main():
    api_url = 'https://covidtracking.com/api/v1/us/daily.json'
    response = requests.get(url=api_url)
    us_daily_data = json.loads(response.text)
    print("   Date\t\t\tPositive Cases\t\tDeaths\t\t Total")
    print("----------\t\t--------------\t\t------\t\t-------")
    date_list = []
    pos_cases_list = []
    total_deaths_list = []
    total_cases_list = []
    index = 0
    while us_daily_data[index + 1]['date'] != MAX_DATE:
        index += 1
    for num in range(index, -1, -1):
        day = us_daily_data[num]
        str_date = f"{str(day['date'])[4:6]}/{str(day['date'])[6:]}/" \
                   f"{str(day['date'])[:4]}"
        pos_cases_list.append(int(day['positive']))
        total_deaths_list.append(int(day["death"]))
        total_cases_list.append(int(day['total']))
        date_list.append(day['date'])
        difference = (index - num)
        print(f"{str_date}\t\t\t{pos_cases_list[difference]:6}\t\t\t{total_deaths_list[difference]:5}\t\t"
              f"{total_cases_list[difference]:7}")
    x_axis_values = [i for i in range(index + 1)]
    print(x_axis_values[0])
    plot_graph(1, x_axis_values, pos_cases_list)
    plot_graph(2, x_axis_values, total_deaths_list)
    plot_graph(3, x_axis_values, total_cases_list)
    x_eq_values_pos, y_eq_values_pos = get_equation_data(x_axis_values, pos_cases_list)
    plot_graph(4, x_eq_values_pos, y_eq_values_pos)
    x_eq_values_deaths, y_eq_values_deaths = get_equation_data(x_axis_values, total_deaths_list)
    plot_graph(5, x_eq_values_deaths, y_eq_values_deaths)
    x_eq_values_total, y_eq_values_total = get_equation_data(x_axis_values, total_cases_list)
    plot_graph(6, x_eq_values_total, y_eq_values_total)
    plt.show()


def plot_graph(num_figure, x_list, y_list):
    """Plots the data on a plypot graph"""
    plt.figure(num_figure)
    y_axis_max_length = str(y_list[-1])
    print(len(y_axis_max_length))
    y_axis = []
    for i in range(12):
        if 2 <= num_figure <= 3:
            y_axis.append(i * (10 ** (len(y_axis_max_length) - 1)))
        else:
            y_axis.append(round(i * (y_list[-1] / 10)))
    print(y_axis)
    y_axis_label = []
    for num in y_axis:
        str_num = str(num)
        for index in range(len(str_num)):
            if index // 3 == 0:
                print("3rd figure")
    if num_figure == 1:
        plt.plot(x_list, y_list, label="Positive Cases")
        plt.ylabel("Positive Cases")
        plt.title("Positive Cases Data")
    elif num_figure == 2:
        plt.plot(x_list, y_list, label="Total Deaths")
        plt.ylabel("Total Deaths")
        plt.title("Total Deaths Data")
    elif num_figure == 3:
        plt.plot(x_list, y_list)
        plt.ylabel("Total Cases")
        plt.title("Total Cases Data")
    elif num_figure == 4:
        plt.plot(x_list, y_list)
        plt.ylabel("Positive Cases")
        plt.title("Positive Cases Projection")
    elif num_figure == 5:
        plt.plot(x_list, y_list)
        plt.ylabel("Total Deaths")
        plt.title("Total Deaths Projection")
    elif num_figure == 6:
        plt.plot(x_list, y_list)
        plt.ylabel("Total Cases")
        plt.title("Total Cases Data")
    plt.yticks(y_axis, y_axis_label)
    plt.xlabel("Days since 2/25/20")


def get_equation_data(x_list, y_list):
    a = (US_POP / y_list[0]) - 1
    b = (((US_POP / y_list[-1]) - 1) / a) ** (1 / x_list[-1])
    y_eq_values_list = []
    x_eq_values_list = []
    for num in range(150):
        x_eq_values_list.append(num)
        new_y_value = US_POP / (1 + (a * (b ** num)))
        y_eq_values_list.append(new_y_value)
    return x_eq_values_list, y_eq_values_list


main()
r"""

My plan: My plan is still to put this data on a graph, but in a better and 
more easily viewable way. My plan is to become proficient with pyplot and 
use to graph the data accurately. After that, the rest of the plan includes
using my trigonometry skills that I learned this year I am going to create an
equation for each variable and then if I am able to, make regression equations
 to determine the accuracy of the equations. This is so one can use the 
 equation to predict where the virus is heading towards.
"""
