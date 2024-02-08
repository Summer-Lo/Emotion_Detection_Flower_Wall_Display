import torch
import torch.backends.cudnn as cudnn
import torchvision.transforms as transforms

from PIL import Image
from repvgg import create_RepVGG_A0 as create
import LED_control_jetson as LED
import threading
import Jetson.GPIO as GPIO
import time


# Load model
model = create(deploy=True)

# 8 Emotions
emotions = ("anger","contempt","disgust","fear","happy","neutral","sad","surprise")
LED_ready = True
on_status = 0


def init(device):
    # Initialise model
    global dev
    dev = device
    model.to(device)
    model.load_state_dict(torch.load("weights/repvgg.pth"))

    # Save to eval
    cudnn.benchmark = True
    model.eval()

def on_led(emotion, second):
    global on_status
    done = False
    if on_status == 1:
        print("LED busy now!")
        done = False
        return done
    else:
        if emotion in LED.emotions:
            on_status = 1
            index = LED.emotions.index(str(emotion))
            GPIO.output(LED.led_emo[index],GPIO.HIGH)
            time.sleep(second)
            GPIO.output(LED.led_emo[index],GPIO.LOW)
            on_status = 0
            print("LED is free now!")
            done = True
            return done

def detect_emotion(images,conf=True):
    global LED_ready, on_status
    with torch.no_grad():
        # Normalise and transform images
        normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                        std=[0.229, 0.224, 0.225])
        x = torch.stack([transforms.Compose([
                transforms.Resize(256),
                transforms.CenterCrop(224),
                transforms.ToTensor(),
                normalize,
            ])(Image.fromarray(image)) for image in images])
        # Feed through the model
        y = model(x.to(dev))
        result = []
        for i in range(y.size()[0]):
            # Add emotion to result
            emotion = (max(y[i]) == y[i]).nonzero().item()
            # Add appropriate label if required
            result.append([f"{emotions[emotion]}{f' ({100*y[i][emotion].item():.1f}%)' if conf else ''}",emotion])
            print(f"{emotions[emotion]} is detected!")
            if(on_status == 0):
                #on_status = 1       # Busy
                LED_on = threading.Thread(target=on_led, args=(emotions[emotion],5,))
                LED_on.start()
                #LED.on_led(emotions[emotion],1)
            else:
                print("LED is busy now, please wait")
                pass
    return result
