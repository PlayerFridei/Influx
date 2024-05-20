# Version 0.1 Early Testing

import telnetlib3
import argparse
import readline  # Enables command history and editing
import sys

class ATGClient:
    def __init__(self, host, port=10001):
        self.host = host
        self.port = port
        self.reader = None
        self.writer = None

    async def connect(self):
        try:
            self.reader, self.writer = await telnetlib3.open_connection(self.host, self.port)
            print(f"Connected to {self.host}:{self.port}")
        except Exception as e:
            print(f"Failed to connect to {self.host}:{self.port} - {e}")
            sys.exit(1)

    async def send_command(self, command):
        try:
            self.writer.write(command + '\n')
            await self.writer.drain()
            response = await self.reader.read(1024)
            return response
        except Exception as e:
            print(f"Error sending command: {e}")
            return None

    async def close(self):
        if self.writer:
            self.writer.close()
            await self.writer.wait_closed()
            print("Connection closed")

    # Existing functions
    async def get_in_tank_inventory(self, args=None):
        return await self.send_command('\x01I20100')

    async def get_setup_parameters(self, args=None):
        return await self.send_command('\x01I20200')

    async def get_tank_test_results(self, args=None):
        return await self.send_command('\x01I20300')

    async def get_alarm_history(self, args=None):
        return await self.send_command('\x01I20400')

    async def get_system_status(self, args=None):
        return await self.send_command('\x01I20000')

    async def set_system_datetime(self, datetime_str):
        command = f'\x01I300{datetime_str}'
        return await self.send_command(command)

    async def get_configuration_data(self, args=None):
        return await self.send_command('\x01I20500')

    async def set_alarm_thresholds(self, threshold):
        command = f'\x01I30100{threshold}'
        return await self.send_command(command)

    # New functions
    async def get_firmware_version(self, args=None):
        return await self.send_command('\x01I20600')

    async def reset_system(self, args=None):
        return await self.send_command('\x01S00100')

    async def clear_power_reset_flag(self, args=None):
        return await self.send_command('\x01S00200')

    async def remote_alarm_reset(self, args=None):
        return await self.send_command('\x01S00300')

    async def cancel_autodial_mode(self, args=None):
        return await self.send_command('\x01S01000')

    async def confirm_clear_function(self, args=None):
        return await self.send_command('\x01S03100')

    async def clear_in_tank_delivery_reports(self, args=None):
        return await self.send_command('\x01S05100')

    async def start_in_tank_leak_detect_test(self, args=None):
        return await self.send_command('\x01S05200')

    async def stop_in_tank_leak_detect_test(self, args=None):
        return await self.send_command('\x01S05300')

    async def delete_csld_rate_table(self, args=None):
        return await self.send_command('\x01S05400')

    async def start_pressure_line_leak_test(self, args=None):
        return await self.send_command('\x01S08100')

    async def stop_pressure_line_leak_test(self, args=None):
        return await self.send_command('\x01S08200')

    async def start_wplld_line_leak_test(self, args=None):
        return await self.send_command('\x01S08300')

    async def stop_wplld_line_leak_test(self, args=None):
        return await self.send_command('\x01S08400')

    async def start_pressure_line_leak_test_by_type(self, args=None):
        return await self.send_command('\x01S08700')

    async def start_wplld_line_leak_test_by_type(self, args=None):
        return await self.send_command('\x01S08800')

    async def pressure_line_leak_pressure_offset_reset(self, args=None):
        return await self.send_command('\x01S08900')

    async def wplld_line_leak_pressure_offset_reset(self, args=None):
        return await self.send_command('\x01S09000')

    async def close_current_shift(self, args=None):
        return await self.send_command('\x01S09100')

    async def start_vacuum_sensor_manual_test(self, args=None):
        return await self.send_command('\x01S09500')

    async def stop_vacuum_sensor_manual_test(self, args=None):
        return await self.send_command('\x01S09600')

    async def start_vacuum_sensor_evacuation_hold(self, args=None):
        return await self.send_command('\x01S09700')

    async def stop_vacuum_sensor_evacuation_hold(self, args=None):
        return await self.send_command('\x01S09800')

    async def start_mag_sump_leak_test(self, args=None):
        return await self.send_command('\x01S09900')

    async def start_mag_sump_leak_test_measuring_height_phase(self, args=None):
        return await self.send_command('\x01S09A00')

    async def stop_mag_sump_leak_test(self, args=None):
        return await self.send_command('\x01S09B00')

    async def get_system_status_report(self, args=None):
        return await self.send_command('\x01I10100')

    # Additional functions from manual
    async def set_print_header(self, line_number, text):
        command = f'\x01S503{line_number:02}{text:20}'
        return await self.send_command(command)

    async def set_rs232_security_code(self, code):
        command = f'\x01S50400{code:6}'
        return await self.send_command(command)

    async def set_system_type_language(self, units, language):
        command = f'\x01S50500{units}{language}'
        return await self.send_command(command)

    async def get_probe_last_sample_buffers(self, tank_number):
        command = f'\x01IA10{tank_number:02}'
        return await self.send_command(command)

    async def get_liquid_sensor_diagnostic(self, sensor_number):
        command = f'\x01IB01{sensor_number:02}'
        return await self.send_command(command)

    async def get_vapor_sensor_diagnostic(self, sensor_number):
        command = f'\x01IB06{sensor_number:02}'
        return await self.send_command(command)

    async def get_vapor_sensor_concentration(self, sensor_number):
        command = f'\x01IB07{sensor_number:02}'
        return await self.send_command(command)

    async def set_ticketed_delivery_variance_printout_flags(self, period, weekly, daily):
        command = f'\x01S53400{period}{weekly}{daily}'
        return await self.send_command(command)

    async def set_receiver_retry_number(self, receiver_number, retry_number):
        command = f'\x01S526{receiver_number:02}{retry_number:02}'
        return await self.send_command(command)

    async def set_receiver_retry_delay_time(self, receiver_number, delay_time):
        command = f'\x01S527{receiver_number:02}{delay_time:02}'
        return await self.send_command(command)

    async def set_receiver_confirmation_report_flag(self, receiver_number, flag):
        command = f'\x01S528{receiver_number:02}{flag}'
        return await self.send_command(command)

    async def set_fax_auto_dial_method(self, method):
        command = f'\x01S52900{method}'
        return await self.send_command(command)

    async def set_receiver_report_list(self, receiver_number, report_list):
        command = f'\x01S52A{receiver_number:02}{report_list:04}'
        return await self.send_command(command)

    async def set_receiver_auto_dial_type(self, receiver_number, start_time):
        command = f'\x01S52B{receiver_number:02}{start_time}'
        return await self.send_command(command)

    async def set_tank_max_volume_limit(self, tank_number, volume):
        command = f'\x01S628{tank_number:02}{volume:06}'
        return await self.send_command(command)

    async def set_tank_delivery_required_limit(self, tank_number, limit):
        command = f'\x01S629{tank_number:02}{limit:06}'
        return await self.send_command(command)

    async def set_line_disable_alarm_assignments(self, pipeline_number, alarm_category, alarm_type, tank_number, status):
        command = f'\x01S75B{pipeline_number:02}{alarm_category:02}{alarm_type:02}{tank_number:02}{status:02}'
        return await self.send_command(command)

    async def set_vapor_processor_control(self, control):
        command = f'\x01SVC000149{control}'
        return await self.send_command(command)

    async def command_test(self, args=None):
        commands = [
            (self.get_in_tank_inventory, []), (self.get_setup_parameters, []), (self.get_tank_test_results, []), (self.get_alarm_history, []),
            (self.get_system_status, []), (self.set_system_datetime, ['050620241230']), (self.get_configuration_data, []), 
            (self.set_alarm_thresholds, ['10']), (self.get_firmware_version, []), (self.reset_system, []), (self.clear_power_reset_flag, []), 
            (self.remote_alarm_reset, []), (self.cancel_autodial_mode, []), (self.confirm_clear_function, []), 
            (self.clear_in_tank_delivery_reports, []), (self.start_in_tank_leak_detect_test, []), (self.stop_in_tank_leak_detect_test, []), 
            (self.delete_csld_rate_table, []), (self.start_pressure_line_leak_test, []), (self.stop_pressure_line_leak_test, []), 
            (self.start_wplld_line_leak_test, []), (self.stop_wplld_line_leak_test, []), (self.start_pressure_line_leak_test_by_type, []), 
            (self.start_wplld_line_leak_test_by_type, []), (self.pressure_line_leak_pressure_offset_reset, []), 
            (self.wplld_line_leak_pressure_offset_reset, []), (self.close_current_shift, []), (self.start_vacuum_sensor_manual_test, []), 
            (self.stop_vacuum_sensor_manual_test, []), (self.start_vacuum_sensor_evacuation_hold, []), (self.stop_vacuum_sensor_evacuation_hold, []), 
            (self.start_mag_sump_leak_test, []), (self.start_mag_sump_leak_test_measuring_height_phase, []), (self.stop_mag_sump_leak_test, []), 
            (self.get_system_status_report, []), (self.set_print_header, [1, 'Header']), (self.set_rs232_security_code, ['123456']), 
            (self.set_system_type_language, ['1', 'EN']), (self.get_probe_last_sample_buffers, [1]), (self.get_liquid_sensor_diagnostic, [1]), 
            (self.get_vapor_sensor_diagnostic, [1]), (self.get_vapor_sensor_concentration, [1]), 
            (self.set_ticketed_delivery_variance_printout_flags, ['1', '1', '1']), (self.set_receiver_retry_number, [1, 3]), 
            (self.set_receiver_retry_delay_time, [1, 5]), (self.set_receiver_confirmation_report_flag, [1, 1]), 
            (self.set_fax_auto_dial_method, ['0']), (self.set_receiver_report_list, [1, 'ABCD']), (self.set_receiver_auto_dial_type, [1, '1200']), 
            (self.set_tank_max_volume_limit, [1, 10000]), (self.set_tank_delivery_required_limit, [1, 500]), 
            (self.set_line_disable_alarm_assignments, [1, '01', '01', '01', '01']), (self.set_vapor_processor_control, ['1'])
        ]

        results = []
        for command, args in commands:
            try:
                result = await command(*args)
                results.append((command.__name__, result))
                print(f"{command.__name__}: {result}")
            except Exception as e:
                results.append((command.__name__, f"Error: {e}"))
                print(f"{command.__name__}: Error: {e}")

        return results

    async def help(self, args=None):
        help_text = """
        Available commands:
        - get_inventory: Get In-Tank Inventory Report
        - get_setup: Get Setup Parameters
        - get_test_results: Get Tank Test Results
        - get_alarm_history: Get Alarm History
        - get_status: Get System Status
        - set_datetime <DDMMYYHHMM>: Set System Date and Time
        - get_config: Get Configuration Data
        - set_alarm <THRESHOLD>: Set Alarm Thresholds
        - get_firmware: Get Firmware Version
        - reset_system: Reset System
        - clear_power_reset: Clear Power Reset Flag
        - remote_alarm_reset: Remote Alarm Reset
        - cancel_autodial: Cancel Autodial Computer Mode Session
        - confirm_clear: Confirm Clear Function
        - clear_in_tank_reports: Clear In-Tank Delivery Reports
        - start_in_tank_leak_test: Start In-Tank Leak Detect Test
        - stop_in_tank_leak_test: Stop In-Tank Leak Detect Test
        - delete_csld_rate: Delete CSLD Rate Table
        - start_pressure_line_test: Start Pressure Line Leak Test
        - stop_pressure_line_test: Stop Pressure Line Leak Test
        - start_wplld_test: Start WPLLD Line Leak Test
        - stop_wplld_test: Stop WPLLD Line Leak Test
        - start_pressure_test_by_type: Start Pressure Line Leak Test by Type
        - start_wplld_test_by_type: Start WPLLD Line Leak Test by Type
        - pressure_line_offset_reset: Pressure Line Leak Pressure Offset Reset
        - wplld_line_offset_reset: WPLLD Line Leak Pressure Offset Reset
        - close_shift: Close Current Shift
        - start_vacuum_test: Start Vacuum Sensor Manual Test
        - stop_vacuum_test: Stop Vacuum Sensor Manual Evacuation Test
        - start_vacuum_hold: Start Vacuum Sensor Evacuation Hold
        - stop_vacuum_hold: Stop Vacuum Sensor Evacuation Hold
        - start_mag_sump_test: Start Mag Sump Leak Test
        - start_mag_sump_height: Start Mag Sump Leak Test Measuring Height Phase
        - stop_mag_sump_test: Stop Mag Sump Leak Test
        - get_system_report: Get System Status Report
        - set_print_header <LINE_NUMBER> <TEXT>: Set Print Header Line
        - set_security_code <CODE>: Set RS-232 Security Code
        - set_system_type_language <UNITS> <LANGUAGE>: Set System Type & Language
        - get_probe_sample_buffers <TANK_NUMBER>: Get Probe Last Sample Buffers
        - get_liquid_sensor_diagnostic <SENSOR_NUMBER>: Get Liquid Sensor Diagnostic
        - get_vapor_sensor_diagnostic <SENSOR_NUMBER>: Get Vapor Sensor Diagnostic
        - get_vapor_sensor_concentration <SENSOR_NUMBER>: Get Vapor Sensor Concentration
        - set_ticketed_delivery_flags <PERIOD> <WEEKLY> <DAILY>: Set Ticketed Delivery Variance Printout Flags
        - set_receiver_retry_number <RECEIVER_NUMBER> <RETRY_NUMBER>: Set Receiver Retry Number
        - set_receiver_retry_delay <RECEIVER_NUMBER> <DELAY_TIME>: Set Receiver Retry Delay Time
        - set_receiver_confirmation_flag <RECEIVER_NUMBER> <FLAG>: Set Receiver Confirmation Report Flag
        - set_fax_auto_dial <METHOD>: Set Fax Auto Dial Method
        - set_receiver_report_list <RECEIVER_NUMBER> <REPORT_LIST>: Set Receiver Report List
        - set_auto_dial_type <RECEIVER_NUMBER> <START_TIME>: Set Receiver Auto Dial Type
        - set_max_volume_limit <TANK_NUMBER> <VOLUME>: Set Tank Max Volume Limit
        - set_delivery_required_limit <TANK_NUMBER> <LIMIT>: Set Tank Delivery Required Limit
        - set_line_disable_alarm_assignments <PIPELINE_NUMBER> <ALARM_CATEGORY> <ALARM_TYPE> <TANK_NUMBER> <STATUS>: Set Line Disable Alarm Assignments
        - set_vapor_processor_control <CONTROL>: Set Vapor Processor Control
        - command_test: Run all available commands for testing
        - help: Show this help message
        - exit: Exit the client
        """
        return help_text.strip()

    async def command_handler(self, command):
        commands = {
            'get_inventory': self.get_in_tank_inventory,
            'get_setup': self.get_setup_parameters,
            'get_test_results': self.get_tank_test_results,
            'get_alarm_history': self.get_alarm_history,
            'get_status': self.get_system_status,
            'set_datetime': self.set_system_datetime,
            'get_config': self.get_configuration_data,
            'set_alarm': self.set_alarm_thresholds,
            'get_firmware': self.get_firmware_version,
            'reset_system': self.reset_system,
            'clear_power_reset': self.clear_power_reset_flag,
            'remote_alarm_reset': self.remote_alarm_reset,
            'cancel_autodial': self.cancel_autodial_mode,
            'confirm_clear': self.confirm_clear_function,
            'clear_in_tank_reports': self.clear_in_tank_delivery_reports,
            'start_in_tank_leak_test': self.start_in_tank_leak_detect_test,
            'stop_in_tank_leak_test': self.stop_in_tank_leak_detect_test,
            'delete_csld_rate': self.delete_csld_rate_table,
            'start_pressure_line_test': self.start_pressure_line_leak_test,
            'stop_pressure_line_test': self.stop_pressure_line_leak_test,
            'start_wplld_test': self.start_wplld_line_leak_test,
            'stop_wplld_test': self.stop_wplld_line_leak_test,
            'start_pressure_test_by_type': self.start_pressure_line_leak_test_by_type,
            'start_wplld_test_by_type': self.start_wplld_line_leak_test_by_type,
            'pressure_line_offset_reset': self.pressure_line_leak_pressure_offset_reset,
            'wplld_line_offset_reset': self.wplld_line_leak_pressure_offset_reset,
            'close_shift': self.close_current_shift,
            'start_vacuum_test': self.start_vacuum_sensor_manual_test,
            'stop_vacuum_test': self.stop_vacuum_sensor_manual_test,
            'start_vacuum_hold': self.start_vacuum_sensor_evacuation_hold,
            'stop_vacuum_hold': self.stop_vacuum_sensor_evacuation_hold,
            'start_mag_sump_test': self.start_mag_sump_leak_test,
            'start_mag_sump_height': self.start_mag_sump_leak_test_measuring_height_phase,
            'stop_mag_sump_test': self.stop_mag_sump_leak_test,
            'get_system_report': self.get_system_status_report,
            'set_print_header': self.set_print_header,
            'set_security_code': self.set_rs232_security_code,
            'set_system_type_language': self.set_system_type_language,
            'get_probe_sample_buffers': self.get_probe_last_sample_buffers,
            'get_liquid_sensor_diagnostic': self.get_liquid_sensor_diagnostic,
            'get_vapor_sensor_diagnostic': self.get_vapor_sensor_diagnostic,
            'get_vapor_sensor_concentration': self.get_vapor_sensor_concentration,
            'set_ticketed_delivery_flags': self.set_ticketed_delivery_variance_printout_flags,
            'set_receiver_retry_number': self.set_receiver_retry_number,
            'set_receiver_retry_delay': self.set_receiver_retry_delay_time,
            'set_receiver_confirmation_flag': self.set_receiver_confirmation_report_flag,
            'set_fax_auto_dial': self.set_fax_auto_dial_method,
            'set_receiver_report_list': self.set_receiver_report_list,
            'set_auto_dial_type': self.set_receiver_auto_dial_type,
            'set_max_volume_limit': self.set_tank_max_volume_limit,
            'set_delivery_required_limit': self.set_tank_delivery_required_limit,
            'set_line_disable_alarm_assignments': self.set_line_disable_alarm_assignments,
            'set_vapor_processor_control': self.set_vapor_processor_control,
            'command_test': self.command_test,
            'help': self.help,
        }

        parts = command.split(' ')
        cmd = parts[0]
        args = parts[1:] if len(parts) > 1 else []

        if cmd in commands:
            try:
                return await commands[cmd](*args)
            except TypeError as e:
                return f"Error: {e}. Command '{cmd}' requires more arguments. Type 'help' for usage."
        else:
            return f"Unknown command: {cmd}. Type 'help' to see available commands."

    async def interactive_mode(self):
        print("Enter commands to send to the ATG (type 'help' for commands, 'exit' to quit):")
        while True:
            try:
                command = input("telnet> ")
            except EOFError:
                print("\nExiting.")
                break

            if command.lower() == 'exit':
                break

            response = await self.command_handler(command)
            if response:
                print(response)

async def main():
    parser = argparse.ArgumentParser(description='Telnet client for TLS-3XX consoles')
    parser.add_argument('ip', help='IP address of the TLS-3XX console')
    parser.add_argument('port', nargs='?', default=10001, type=int, help='Port number, default is 10001')
    args = parser.parse_args()

    client = ATGClient(args.ip, args.port)
    await client.connect()
    await client.interactive_mode()
    await client.close()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
