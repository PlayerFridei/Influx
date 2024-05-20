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

By downloading and using this tool, you agree to the following terms:

1. The tool is provided without any warranty, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and non-infringement.

2. The creator of the tool shall not be liable for any direct, indirect, incidental, special, consequential, or exemplary damages, including but not limited to, damages for loss of profits, goodwill, use, data, or other intangible losses.

3. You understand and acknowledge that the tool is still under development and may not be fully polished. As such, it might contain bugs or other issues that could affect its performance.

4. You understand and acknowledge that the creator of the tool may, at their sole discretion, discontinue support for the tool at any time and without notice. This means that there is no guarantee of ongoing maintenance, updates, or technical assistance.

5. You agree to use the tool at your own risk and understand that the creator of the tool does not provide any assurances regarding its functionality, reliability, or suitability for any purpose.

6. The creator of the tool reserves the right to modify, suspend, or terminate the tool at any time, with or without cause, and without liability to you or any third party.

By downloading and using the tool, you acknowledge that you have read, understood, and agreed to these terms. If you do not agree with any part of these terms, you should not download or use the tool.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
