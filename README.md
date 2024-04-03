# Darknet Detector Test Wrapper

This repository contains a wrapper for the Darknet neural network, which was originally obtained from [AlexeyAB/darknet.git](https://github.com/AlexeyAB/darknet.git). 

The wrapper utilizes the `.so` file generated from the aforementioned repository. It provides functionality for image processing through pixel computations obtained by invoking `darknet detector test...`.

Additionally, it includes a Darknet manager responsible for managing instances of the neural network, enabling parallel processing of up to 16 images.

## Features

- **Darknet Wrapper**: Utilizes Darknet framework for image processing.
- **Parallel Processing**: Darknet manager facilitates parallel processing of images.
- **Stability**: Production-ready solution, stable for deployment.

## Initialization and Usage

To utilize this Darknet Detector Test Wrapper, follow the steps below:

1. **Initialization**: 
   Before performing any detections, initialize the Darknet manager by calling:
   ```python
   DarknetManager.prepare_instances()
   ```
2. **Perform detection**
   When you need to process an image, retrieve an available instance and perform the detection:
   ```python
   image_path = "..."
   darknet_process = DarknetManager.get_available_instance()
   detections = darknet_process.process(image_path)
   ```
4. **Release Instance**
  Once detection is complete, release the instance to make it available for subsequent requests:
  ```python
  DarknetManager.release_instance(darknet_process)
  ``` 
4. **Data Parsing**
  Data obtained from the detection can be parsed using the following method provided in the wrapper:
  ```python
  def parse_data(detections):
    matrix = []
    for detection in detections:
        percentage = float(detection[1])
        left_x = int(detection[2][0])
        top_y = int(detection[2][1])
        width = int(detection[2][2])
        height = int(detection[2][3])
    return matrix
   ```
## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- [AlexeyAB](https://github.com/AlexeyAB) for the Darknet.

## Notes

- Contributions and suggestions are welcome. Feel free to open an issue or create a pull request.
