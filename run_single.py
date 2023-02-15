from model import SegModel

# Set your parameter values for one run
# Reminder that the model takes on these parameter values:
# width, height, schedule_type, num_agents, minority_pc, intolerance, inequality
model = SegModel(width=20, height=20, schedule_type="Random", num_agents=350, minority_pc=0.5,
                 intolerance=0.375, inequality=0.7)
for t in range(200):
    model.step()

# extract data as a pandas Data Frame
model_df = model.datacollector.get_model_vars_dataframe()

## NOTE: to do data collection, you need to be sure your pathway is correct to save this!
# export the data to a csv file for graphing/analysis
model_df.to_csv("seg_model_single_run_data2.csv")
