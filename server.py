import asyncio
import configparser
import os.path
import websockets

from lib.AlarmServer import AlarmServer


async def main():
    config_file = os.path.dirname(os.path.abspath(__file__)) + '/config.ini'
    if not os.path.exists(config_file):
        raise FileNotFoundError('Configuration file not found: ' + config_file)

    config = configparser.ConfigParser()
    config.read(config_file)
    sound_file = config.get('DEFAULT', 'SoundFile')
    web_socket_port = int(config.get('DEFAULT', 'Port'))

    sound_file = os.path.dirname(os.path.abspath(__file__)) + '/sound/' + sound_file
    if not os.path.exists(sound_file):
        raise FileNotFoundError('Sound file not found: ' + sound_file)

    alarm_server = AlarmServer(sound_file)
    start_server = websockets.serve(alarm_server.handle_socket_client, '0.0.0.0', web_socket_port)
    alarm_task = asyncio.create_task(alarm_server.loop())
    await asyncio.gather(alarm_task, start_server)

if __name__ == '__main__':
    asyncio.run(main())
