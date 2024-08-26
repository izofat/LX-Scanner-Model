# LX-Scanner-Model

## Introduction
LX-Scanner-Model is a project that aims to provide a model for the LX-Scanner project. 
The model is a simple representation of the scanner that can be used to test the scanner's functionality.

## Installation
To install the model, simply clone the repository and run the following command:

```bash
make install
```

After installing all packages and dependencies, you can simply test if project configured successfully

```bash
make test
```

Alternatively, you can test with other image and languages
    
```bash
make test PATH=<path_to_image> LANG=<language>
```

## Configuration
This project uses rabbitmq as a message broker. To configure the project,
you need to set the following environment variables in the config.toml file:
    
```toml
[rabbitmq]
input_queue = "<input_queue>"
output_queue = "<output_queue>"

[rabbitmq."<env>"]
username = "guest"
password = "guest"
host = "localhost"
port = 5672
vhost = "/"
```
Change the input_queue and output_queue to the desired queue names.
You can also change the username, password, host, port, and vhost to the desired values.

## Usage
To use the model, you can simply run the following command:

```bash
make launch
```

This will launch the model and display the scanner's output.

