# SketchMS
SketchMS is a program to make a sketch from picture that you have

# How to get Started
Install the required packages : pip install -r requirements.txt

## Dowload Pretrained Weight 
Please download the weights from [GoogleDrive](https://drive.google.com/file/d/1t-HtOuC3Bs4wAbU3h4FUr2G2xPP6XgvR/view?usp=drive_link), and put it into the weight/ folder

## Test
```Shell
python3 test.py --dataroot /your_input/dir --load_size 512 --output_dir /your_output/dir
```

The above commands includes three arguments:
- dataroot : your test file or directory
- load_size : due to memory limit, we need to resize the input image before processing, By default, we resize it to 512x512
- output_dir : path of the output directory

Run Our Example
```Shell
python3 test.py --dataroot test_samples/madoka.jpg --load_size 512 --output_dir results/
```

## Made By 
- rifqanzalbina

