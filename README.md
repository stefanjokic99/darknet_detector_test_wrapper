# Darknet Detector Test Wrapper

This repository contains a wrapper for the Darknet neural network, which was originally obtained from [AlexeyAB/darknet.git](https://github.com/AlexeyAB/darknet.git). 

The wrapper utilizes the `.so` file generated from the aforementioned repository. It provides functionality for image processing through pixel computations obtained by invoking `darknet detector test...`.

Additionally, it includes a Darknet manager responsible for managing instances of the neural network, enabling parallel processing of up to 16 images.

## Features

- **Darknet Wrapper**: Utilizes Darknet framework for image processing.
- **Parallel Processing**: Darknet manager facilitates parallel processing of images.
- **Stability**: Production-ready solution, stable for deployment.

## Contributors

- [Stefan Jokic](https://github.com/stefanjokic99)

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- [AlexeyAB](https://github.com/AlexeyAB) for the Darknet.

## Notes

- Contributions and suggestions are welcome. Feel free to open an issue or create a pull request.
