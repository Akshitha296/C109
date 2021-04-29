import pandas as pd
import statistics
import csv

df = pd.read_csv("SOCR-HeightWeight.csv")
height_list = df["Height(Inches)"].to_list()
weight_list = df["Weight(Pounds)"].to_list()

height_mean = statistics.mean(height_list)
height_median = statistics.median(height_list)
height_mode = statistics.mode(height_list)

print("Mean, Median, Mode for height is ", height_mean, height_median, height_mode)

weight_mean = statistics.mean(weight_list)
weight_median = statistics.median(weight_list)
weight_mode = statistics.mode(weight_list)

print("Mean, Median, Mode for weight is ", weight_mean, weight_median, weight_mode)

height_sd = statistics.stdev(height_list)
weight_sd = statistics.stdev(weight_list)

print("Height SD is ", height_sd)
print("Weight SD is ", weight_sd)

height_first_sd_start = height_mean - height_sd
height_first_sd_end = height_mean + height_sd

height_second_sd_start = height_mean-(height_sd*2)
height_second_sd_end = height_mean+(height_sd*2)

height_third_sd_start = height_mean-(height_sd*3)
height_third_sd_end = height_mean+(height_sd*3)

height_data_within_first_sd = [result for result in height_list if result>height_first_sd_start and result<height_first_sd_end]
height_data_within_second_sd = [result for result in height_list if result>height_second_sd_start and result<height_second_sd_end]
height_data_within_third_sd = [result for result in height_list if result>height_third_sd_start and result<height_third_sd_end]

percentage_height_1 = len(height_data_within_first_sd)*100/len(height_list)
percentage_height_2 = len(height_data_within_second_sd)*100/len(height_list)
percentage_height_3 = len(height_data_within_third_sd)*100/len(height_list)

print("Percentage of height data within 1st sd is ", percentage_height_1)
print("Percentage of height data within 2nd sd is ", percentage_height_2)
print("Percentage of height data within 3st sd is ", percentage_height_3)

weight_first_sd_start = weight_mean - weight_sd
weight_first_sd_end = weight_mean + weight_sd

weight_second_sd_start = weight_mean-(weight_sd*2)
weight_second_sd_end = weight_mean+(weight_sd*2)

weight_third_sd_start = weight_mean-(weight_sd*3)
weight_third_sd_end = weight_mean+(weight_sd*3)

weight_data_within_first_sd = [result for result in weight_list if result>weight_first_sd_start and result<weight_first_sd_end]
weight_data_within_second_sd = [result for result in weight_list if result>weight_second_sd_start and result<weight_second_sd_end]
weight_data_within_third_sd = [result for result in weight_list if result>weight_third_sd_start and result<weight_third_sd_end]

percentage_weight_1 = len(weight_data_within_first_sd)*100/len(weight_list)
percentage_weight_2 = len(weight_data_within_second_sd)*100/len(weight_list)
percentage_weight_3 = len(weight_data_within_third_sd)*100/len(weight_list)

print("Percentage of weight data within 1st sd is ", percentage_weight_1)
print("Percentage of weight data within 2nd sd is ", percentage_weight_2)
print("Percentage of weight data within 3st sd is ", percentage_weight_3)