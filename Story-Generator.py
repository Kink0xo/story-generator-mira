from mira_sdk import MiraClient
from dotenv import load_dotenv
import os


# Initialize the Mira client
load_dotenv()
api_key = os.getenv("API_KEY")
client = MiraClient(config={"API_KEY": api_key})

flow_name1 = "@kink0xo/character-generator"
flow_name2 = "@kink0xo/short-story-generator"
flow_name3 = "@kink0xo/story-refiner/1.2.0"

print("Please provide inputs. For multiple values, separate them with commas.")
important_characters = input("Enter important character names: ").strip()
filler_characters = input("Enter filler character names: ").strip()
setting = input("Enter the story setting: ").strip()
genres = input("Enter the genres of the story: ").strip()
themes = input("Enter the themes of the story: ").strip()
try:
    words = int(input("Enter the approximate word count for the story: ").strip())
except e:
    raise e("Please enter an integer value for the word count.")

# Input for Flow 1
input_data1 = {
    "important character names": important_characters,
    "filler character names": filler_characters,
    "setting": setting,
}
# Output of flow 1
flow1_output = client.flow.execute(flow_name1, input_data1)
print("Flow 1 completed.")

# Input for Flow 2
input_data2 = {
    "flow1": flow1_output,
    "genres": genres,
    "themes": themes,
    "words": words,
}
# Output of flow 2
flow2_output = client.flow.execute(flow_name2, input_data2)
print("Flow 2 completed.")

# Input for flow 3
input_data3 = {
    "flow2": flow2_output,
}
# Output of flow 3
flow3_output = client.flow.execute(flow_name3, input_data3)
print("Flow 3 completed.")
print(flow3_output)