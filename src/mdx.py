import os
import gradio as gr
from audio_separator.separator import Separator

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
output_dir = os.path.join(BASE_DIR, 'uvr_output')



def separate_audio(input_audio):
    separator = Separator(output_dir=output_dir)
    
    # Load the model
    separator.load_model(model_filename='model_bs_roformer_ep_317_sdr_12.9755.ckpt')
    
    # Separate into vocal and instrumental
    voc_inst = separator.separate(input_audio.name)
    
    # Set file paths for the output
    vocals = os.path.join(output_dir, 'Vocals.wav')
    instrumental = os.path.join(output_dir, 'Instrumental.wav')
    
    # Rename the separated files to match expected output
    os.rename(os.path.join(output_dir, voc_inst[0]), instrumental)
    os.rename(os.path.join(output_dir, voc_inst[1]), vocals)
    
    return vocals, instrumental
