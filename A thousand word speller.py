import socket
import os
import io
import warnings
from PIL import Image
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation
import openai

PORT=5231

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('', 5231))
lis = []

while True:
    message, address = server_socket.recvfrom(100240)
    message = str(message)
    message=message.split("Diego")
    message=str(message[2])
    index = message.find(".jpg")
    if message[index-2:index] == "a1":
        print("surrealism")
        lis.append("style: surrealism")
    elif message[index-2:index] == "a2":
        print("pixel-art")
        lis.append("style: pixel-art")
    elif message[index-2:index] == "a3":
        print('anime-style')
        lis.append("style: anime-style")
    elif message[index-2:index] == "a4":
        print("oil-painting")
        lis.append("style: oil-painting")
    elif message[index-2:index] == "a5":
        print("digital-art")
        lis.append("style: digital-art")
    elif message[index-2:index] == "a6":
        print("car")
        lis.append("car")
    elif message[index-2:index] == "a7":
        print("tree")
        lis.append("tree")
    elif message[index-2:index] == "a8":
        print("dog")
        lis.append("dog")
    elif message[index-2:index] == "a9":
        print("man")
        lis.append("man")
    elif message[index-2:index] == "a0":
        print("apple")
        lis.append("apple")
    elif message[index-2:index] == "b1":
        print("red")
        lis.append("color: red")
    elif message[index-2:index] == "b2":
        print("green")
        lis.append("color: green")
    elif message[index-2:index] == "b3":
        print("blue")
        lis.append("color: blue")
    elif message[index-2:index] == "b4":
        print("purple")
        lis.append("color: purple")
    elif message[index-2:index] == "b5":
        print("turquoise")
        lis.append("color: turquoise")
    elif message[index-2:index] == "b6":
        print("boat")
        lis.append("boat")
    elif message[index-2:index] == "b7":
        print("smartphone")
        lis.append("smartphone")
    elif message[index-2:index] == "b8":
        print("cat")
        lis.append("cat")
    elif message[index-2:index] == "b9":
        print("woman")
        lis.append("woman")
    elif message[index-2:index] == "b0":
        print("ice-cream")
        lis.append("ice-cream")
    elif message[index-2:index] == "c1":
        print("black")
        lis.append("color: black")
    elif message[index-2:index] == "c2":
        print("white")
        lis.append("color: white")
    elif message[index-2:index] == "c3":
        print("gray")
        lis.append("color: gray")
    elif message[index-2:index] == "c4":
        print("orange")
        lis.append("color: orange")
    elif message[index-2:index] == "c5":
        print("yellow")
        lis.append("color: yellow")
    elif message[index-2:index] == "c6":
        print("plane")
        lis.append("plane")
    elif message[index-2:index] == "c7":
        print("flower")
        lis.append("flower")
    elif message[index-2:index] == "c8":
        print("bird")
        lis.append("bird")
    elif message[index-2:index] == "c9":
        print("family")
        lis.append("family")
    elif message[index-2:index] == "c0":
        print("banana")
        lis.append("banana")
    elif message[index-2:index] == "d1":
        print("city")
        lis.append("city")
    elif message[index-2:index] == "d2":
        print("forest")
        lis.append("forest")
    elif message[index-2:index] == "d3":
        print("outer-space")
        lis.append("outer-space")
    elif message[index-2:index] == "d4":
        print("house")
        lis.append("house")
    elif message[index-2:index] == "d5":
        print("dessert")
        lis.append("dessert")
    elif message[index-2:index] == "d6":
        print("rocket")
        lis.append("rocket")
    elif message[index-2:index] == "d7":
        print("computer")
        lis.append("computer")
    elif message[index-2:index] == "d8":
        print("axolotl")
        lis.append("axolotl")
    elif message[index-2:index] == "d9":
        print("friends")
        lis.append("friends")
    elif message[index-2:index] == "d0":
        print("planet")
        lis.append("planet")
    elif message[index-2:index] == "e1":
        print("mountain")
        lis.append("mountain")
    elif message[index-2:index] == "e2":
        print("school")
        lis.append("school")
    elif message[index-2:index] == "e3":
        print("room")
        lis.append("room")
    elif message[index-2:index] == "e4":
        print("restaurant")
        lis.append("restaurant")
    elif message[index-2:index] == "e5":
        print("ocean")
        lis.append("ocean")
    elif message[index-2:index] == "e6":
        print("train")
        lis.append("train")
    elif message[index-2:index] == "e7":
        print("pencil")
        lis.append("pencil")
    elif message[index-2:index] == "e8":
        print("lion")
        lis.append("lion")
    elif message[index-2:index] == "e9":
        print("couple")
        lis.append("couple")
    elif message[index-2:index] == "e0":
        print("star")
        lis.append("star")
    elif message[index-2:index] == "f1":
        print("sky")
        lis.append("sky")
    elif message[index-2:index] == "f2":
        print("office")
        lis.append("office")
    elif message[index-2:index] == "f3":
        print("fantasy")
        lis.append("fantasy")
    elif message[index-2:index] == "f4":
        print("beach")
        lis.append("beach")
    elif message[index-2:index] == "f5":
        print("volcano")
        lis.append("volcano")
    elif message[index-2:index] == "f6":
        print("dinosaur")
        lis.append("dinosaur")
    elif message[index-2:index] == "f7":
        print("notebook")
        lis.append("notebook")
    elif message[index-2:index] == "f8":
        print("dolphin")
        lis.append("dolphin")
    elif message[index-2:index] == "f9":
        print("robot")
        lis.append("robot")
    elif message[index-2:index] == "f0":
        print("stop")
        break


openai.api_key=""


mensaje = "Engineer an efficient image prompt to input in Stable Difussion based on the following elements: "+", ".join(lis)


response=openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "user", "content": mensaje}
    ]
)

entrada=(response['choices'][0]['message']['content'])
print(entrada)

# Our Host URL should not be prepended with "https" nor should it have a trailing slash.
os.environ['STABILITY_HOST'] = 'grpc.stability.ai:443'

# Sign up for an account at the following link to get an API Key.
# https://dreamstudio.ai/

# Click on the following link once you have created an account to be taken to your API Key.
# https://dreamstudio.ai/account

# Paste your API Key below.

os.environ['STABILITY_KEY'] = ''


# Set up our connection to the API.
stability_api = client.StabilityInference(
    key=os.environ['STABILITY_KEY'], # API Key reference.
    verbose=True, # Print debug messages.
    engine="stable-diffusion-xl-beta-v2-2-2", # Set the engine to use for generation.
    # Available engines: stable-diffusion-v1 stable-diffusion-v1-5 stable-diffusion-512-v2-0 stable-diffusion-768-v2-0
    # stable-diffusion-512-v2-1 stable-diffusion-768-v2-1 stable-diffusion-xl-beta-v2-2-2 stable-inpainting-v1-0 stable-inpainting-512-v2-0
)

# Set up our initial generation parameters.
answers = stability_api.generate(
    prompt=entrada,
    steps=50, # Amount of inference steps performed on image generation. Defaults to 30.
    cfg_scale=7.0, # Influences how strongly your generation is guided to match your prompt.
                   # Setting this value higher increases the strength in which it tries to match your prompt.
                   # Defaults to 7.0 if not specified.
    width=512, # Generation width, defaults to 512 if not included.
    height=512, # Generation height, defaults to 512 if not included.
    samples=1, # Number of images to generate, defaults to 1 if not included.
    sampler=generation.SAMPLER_K_DPMPP_2M # Choose which sampler we want to denoise our generation with.
                                                 # Defaults to k_dpmpp_2m if not specified. Clip Guidance only supports ancestral samplers.
                                                 # (Available Samplers: ddim, plms, k_euler, k_euler_ancestral, k_heun, k_dpm_2, k_dpm_2_ancestral, k_dpmpp_2s_ancestral, k_lms, k_dpmpp_2m, k_dpmpp_sde)
)

# Set up our warning to print to the console if the adult content classifier is tripped.
# If adult content classifier is not tripped, save generated images.
for resp in answers:
    for artifact in resp.artifacts:
        if artifact.finish_reason == generation.FILTER:
            warnings.warn(
                "Your request activated the API's safety filters and could not be processed."
                "Please modify the prompt and try again.")
        if artifact.type == generation.ARTIFACT_IMAGE:
            img = Image.open(io.BytesIO(artifact.binary))
            img.show()
            img.save(str(artifact.seed)+ ".png") # Save our generated images with their seed number as the filename.
