
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
import re
import json
import requests


tokenizer = AutoTokenizer.from_pretrained("AquilaX-AI/NL-JSON-Start-Scan")
model = AutoModelForSeq2SeqLM.from_pretrained("AquilaX-AI/NL-JSON-Start-Scan")

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")


def convert_to_json(answer):
    """
    Convert a string representation of a dictionary to a JSON object.

    This function takes a string representation of a dictionary, cleans it by removing
    specific unwanted tokens and correcting boolean representations, and then converts
    it into a JSON object.

    Parameters:
    answer (str): The input string representing a dictionary.

    Returns:
    dict: The JSON object converted from the input string.
    """
    answer = answer.replace("<pad>", "").replace("</s>", "")
    answer = answer.strip("'")
    answer = answer.replace("false", "False").replace("true", "True")
    answer_dict = eval(answer)
    answer_json = json.dumps(answer_dict)
    json_data = json.loads(answer_json)
    return json_data

def valid_url(url):
    """
    Validate the given URL against a list of supported platforms.

    This function checks if the provided URL belongs to one of the supported
    platforms for scanning. If the URL is valid, it returns True. Otherwise,
    it returns a message indicating that the URL is not supported and lists the
    available scanners.

    Parameters:
    url (str): The URL to be validated.

    Returns:
    bool or dict: Returns True if the URL is valid, otherwise returns a
                  dictionary with a message indicating the URL is not supported
                  and lists the available scanners.
    """
    valid_list = [
        "github.com", "bitbucket.org", "sourceforge.net", "aws.amazon.com",
        "dev.azure.com", "gitea.com", "gogs.io", "phabricator.com",
        "gitkraken.com", "beanstalkapp.com", "gitlab.com"
    ]
    platform = url.split("//")[1].split("/")[0]

    if platform in valid_list:
        return True

    return {
        'message': 'Provide a valid URL for scanning. Currently, we support PII_Scanner, SAST_Scanner, Sac_Scanner (Open_Source_Security), IaC_Scanner, Container_Scanner'
    }



query = "Translate the following text to JSON: " + "hello dude, https://github.com/TheAILearner/GenAI-with-Open-Source-LLMs/blob/main, this is my repo can you scan this on 30 days?".lower()
query = query.replace(',', '')

inputs = tokenizer(query, return_tensors="pt")
model.to(device)
inputs = inputs.to(device)
outputs = model.generate(**inputs, max_length=256)
answer = tokenizer.decode(outputs[0])
json_data = convert_to_json(answer)
# print(json_data)
to_return = json_data.copy()

try:
    valid = valid_url(json_data["repo"])
    if valid != True:
        to_return = valid
    else:
      url = re.findall(r'https?://\S+', query)
      to_return['repo'] = url

except:
    pass


print(to_return)
