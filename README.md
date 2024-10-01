# Influx
A Client that will connect to gas tank gauges.

## Features

- Connect to ATG consoles using Python Telnet Client
- Execute a wide range of commands to retrieve and configure ATG settings if it works.
- Sequentially test all available commands with a single `command_test` function.
- `get_inventory`: Get In-Tank Inventory Report
- `get_setup`: Get Setup Parameters
- `get_test_results`: Get Tank Test Results
- `get_alarm_history`: Get Alarm History
- `get_status`: Get System Status
- + Much more!

## Prerequisites

- Python 3.11 or higher
- `telnetlib3` package

## Installation

1. **Clone the repository**:
```sh
git clone https://github.com/PlayerFridei/Influx
```

```sh
cd atg-telnet-client
```

2. **Install the required packages**:
```sh
pip install -r requirements.txt
```

## Usage

Run the client using the following command:
```sh
python gasstation.py <IP> <PORT>
```

# Disclaimer

> Before using this software, you agree to the terms outlined in our [SECURITY.md](SECURITY.md) policy.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
