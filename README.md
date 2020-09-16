# Enhancing HDR
The Keras Implementation of the [Deep HDR Imaging via A Non-Local Network](https://ieeexplore.ieee.org/document/8989959) - TIP 2020
## Content
- [Enhancing HDR](#enhancing-hdr)
- [Getting Started](#getting-tarted)
- [Running](#running)
- [References](#references)
- [Citations](#citation)

## Getting Started

- Clone the repository

### Prerequisites
- opencv
- Python 3.6+
- Keras 2.3.0
- numpy

```python
pip install -r requirements.txt
```

## Running
### Training 
    ```
    python main.py
    ```
## Usage
### Training
```
usage: main.py [-h] [--image_path IMAGES_PATH]
               [--filter True]
```

```
optional arguments: -h, --help                show this help message and exit
                    --images_path             path to image
                    --filter                  use guided filter or weighted least square filter
```

#### Result
![INPUT](imgs/Duck.png) | ![OUTPUT](imgs/rs_Duck.png) |
|:---:|:---:|
![INPUT](imgs/test2.jpg) | ![OUTPUT](imgs/rs_test2.jpg) |
| input | output |

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/tuvovan/NHDRRNet/blob/master/LICENSE) file for details

## Acknowledgments
- This work based on different scientific papers with the following modification:
    - replacing the weighted least square filter by guided filter to enhance the speed.
    - changing the weighting solution for merging images.
- Any ideas on updating or misunderstanding, please send me an email: <vovantu.hust@gmail.com>
- If you find this repo helpful, kindly give me a star.