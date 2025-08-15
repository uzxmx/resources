#!/usr/bin/env python

"""
Example for a BLE 4.0 Server
"""
import sys
import logging
import asyncio
import threading
import random

from typing import Any, Union

from bless import (  # type: ignore
    BlessServer,
    BlessGATTCharacteristic,
    GATTCharacteristicProperties,
    GATTAttributePermissions,
)

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(name=__name__)

# NOTE: Some systems require different synchronization methods.
trigger: Union[asyncio.Event, threading.Event]
if sys.platform in ["darwin", "win32"]:
    trigger = threading.Event()
else:
    trigger = asyncio.Event()

def read_request(characteristic: BlessGATTCharacteristic, **kwargs) -> bytearray:
    logger.debug(f"Reading {characteristic.value}")
    return characteristic.value

def write_request(characteristic: BlessGATTCharacteristic, value: Any, **kwargs):
    characteristic.value = value
    logger.debug(f"Char value set to {characteristic.value}")
    if characteristic.value == b"\x0f":
        logger.debug("Start generating random numbers")
        trigger.set()

async def run(loop):
    trigger.clear()

    if len(sys.argv) > 1:
        my_service_name = sys.argv[1]
    else:
        my_service_name = "Test Service"
    logger.info('Service name: {}'.format(my_service_name))

    server = BlessServer(name=my_service_name, loop=loop)
    server.read_request_func = read_request
    server.write_request_func = write_request

    # Add Service
    my_service_uuid = "A07498CA-AD5B-474E-940D-16F1FBE7E8CD"
    await server.add_new_service(my_service_uuid)

    # Add a Characteristic to the service
    my_char_uuid = "51FF12BB-3ED8-46E5-B4F9-D64E2FEC021B"
    char_flags = (
        GATTCharacteristicProperties.read
        | GATTCharacteristicProperties.write
        | GATTCharacteristicProperties.indicate
    )
    permissions = GATTAttributePermissions.readable | GATTAttributePermissions.writeable
    await server.add_new_characteristic(
        my_service_uuid, my_char_uuid, char_flags, None, permissions
    )

    await server.start()
    logger.info(f"Write '0xF' to the advertised characteristic: {my_char_uuid} to continue")
    if trigger.__module__ == "threading":
        trigger.wait()
    else:
        await trigger.wait()

    my_char = server.get_characteristic(my_char_uuid)
    while True:
        numbers = [random.randint(1, 255) for i in range(4)]
        logger.info('Numbers: {}'.format(numbers))
        my_char.value = bytearray(b''.join([num.to_bytes(4) for num in numbers]))
        server.update_value(my_service_uuid, my_char_uuid)
        await asyncio.sleep(1)

    await server.stop()

loop = asyncio.get_event_loop()
loop.run_until_complete(run(loop))
