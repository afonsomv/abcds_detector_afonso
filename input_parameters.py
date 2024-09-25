#!/usr/bin/env python3

###########################################################################
#
#  Copyright 2024 Google LLC
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
###########################################################################

import os

"""Module that defines the colab parameters"""

# @markdown ### Google Cloud Project Details

PROJECT_ID = "" # @param {type:"string", placeholder:"Google Cloud Project ID"}
BUCKET_NAME = "shape-shifters" # @param {type:"string", placeholder:"Google Cloud Sotrage Bucket for annotations"}
ANNOTATION_PATH = f"gs://{BUCKET_NAME}/ABCD/"

VIDEO_URIS = [
  "gs://cloud-samples-data/generative-ai/video/pixel8.mp4",
] # use helpers/input_helper.py to load this

FFMPEG_BUFFER = "reduced/buffer.mp4"
if not os.path.exists('reduced'):
  os.makedirs('reduced')

# @markdown ### Solution Setup

VIDEO_SIZE_LIMIT_MB = 40  # @param {type:"number"}
VERBOSE = True  # @param {type:"boolean"}
use_llms = True  # @param {type:"boolean"}
use_annotations = True # @param {type:"boolean"}
# For local testing outside colab ONLY, set to False for colab
ASSESSMENT_FILE = "" # @param {type:"string", placeholder:"optional local file to write assesments to"} 
TEST_RESULTS = []

# @markdown #### Knowledge Graph API Configuration

KNOWLEDGE_GRAPH_API_KEY = ""  # @param {type:"string", placeholder:"Google Cloud Project API Key"}

# @markdown ### Brand and Product Details

brand_name = "Google"  # @param {type:"string"}
brand_variations_str = "google"  # @param {type:"string"}
branded_products_str = "Google pixel, Google pixel buds, Google pixel watch"  # @param {type:"string"}
branded_products_categories_str = "phone, watch, buds"  # @param {type:"string"}
branded_call_to_actions_str = "buy it!"  # @param {type:"string"}


# @markdown ### ABCD Framework Details

# @markdown #### ABCD Assessment Thresholds
early_time_seconds = 5
confidence_threshold = 0.5  # @param {type:"number"}
face_surface_threshold = 0.15  # @param {type:"number"}
logo_size_threshold = 3.5  # @param {type:"number"}
avg_shot_duration_seconds = 2  # @param {type:"number"}
dynamic_cutoff_ms = 3000  # @param {type:"number"}


# @markdown ### LLM Configuration

# @markdown #### LLM names and versions

GEMINI_PRO_VISION = "gemini-1.0-pro-vision-001"  # @param {type:"string"}
GEMINI_PRO = "gemini-1.5-pro-preview-0409"  # @param {type:"string"}
llm_location = "us-central1"  # @param {type:"string"}
max_output_tokens = 8192  # @param {type:"number"}
temperature = 1  # @param {type:"number"}
top_p = 0.95  # @param {type:"number"}
top_k = 32  # @param {type:"number"}


### DO NOT EDIT, vars built from user's input ###
def convert_string_to_list(list_str: str):
    """Converts a string to a list and
    removes white spaces from strings in list
    Args:
        list_str
    """
    cleaned_list = []
    for item in list_str.split(","):
        cleaned_list.append(item.strip())
    return cleaned_list

brand_variations = convert_string_to_list(brand_variations_str)
brand_variations.append(brand_name)
branded_products = convert_string_to_list(branded_products_str)
branded_products_categories = convert_string_to_list(branded_products_categories_str)
branded_call_to_actions = convert_string_to_list(branded_call_to_actions_str)

if VERBOSE:
    print("ABCD Detector parameters:")
    print(f"Brand Variations: {brand_variations}")
    print(f"Brand products: {branded_products}")
    print(f"Brand categories: {branded_products_categories}")
    print(f"Brand call to actions: {branded_call_to_actions}")

llm_generation_config = {
    "max_output_tokens": max_output_tokens,
    "temperature": temperature,
    "top_p": top_p,
    "top_k": top_k,
}

context_and_examples = """Only base your answers strictly on what information is available in the video attached.
Do not make up any information that is not part of the video.
Explain in a very detailed way the reasoning behind your answer.
Please present the extracted information in a VALID JSON format like this:
{
    "feature_detected": "True/False",
    "explanation": "..."
}
"""
