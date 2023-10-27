#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# (c) Copyright 2023 Sensirion AG, Switzerland
#
#     THIS FILE IS AUTOMATICALLY GENERATED!
#
# Generator:     sensirion-driver-generator 0.33.0
# Product:       sts3x
# Model-Version: 1.0.0
#
"""
The transfer classes specify the data that is transferred between host and sensor. The generated transfer classes
are used by the driver class and not intended for direct use.
"""

from enum import Enum
from sensirion_driver_adapters.transfer import Transfer
from sensirion_driver_adapters.rx_tx_data import TxData, RxData
from sensirion_driver_support_types.bitfield import BitField, BitfieldContainer


class MeasureSingleShotHighRepeatability(Transfer):
    """Single shot measurement with high repeatability"""

    CMD_ID = 0x2400

    def pack(self):
        return self.tx_data.pack([])

    tx = TxData(CMD_ID, '>H', device_busy_delay=0.016, slave_address=None, ignore_ack=False)
    rx = RxData('>H')


class MeasureSingleShotHighRepeatabilityClockStretching(Transfer):
    """Single shot measurement with high repeatability and clock stretching enabled."""

    CMD_ID = 0x2c06

    def pack(self):
        return self.tx_data.pack([])

    tx = TxData(CMD_ID, '>H', device_busy_delay=0.016, slave_address=None, ignore_ack=False)
    rx = RxData('>H')


class MeasureSingleShotMediumRepeatability(Transfer):
    """Single shot measurement with medium repeatability"""

    CMD_ID = 0x240b

    def pack(self):
        return self.tx_data.pack([])

    tx = TxData(CMD_ID, '>H', device_busy_delay=0.007, slave_address=None, ignore_ack=False)
    rx = RxData('>H')


class MeasureSingleShotMediumRepeatabilityClockStretching(Transfer):
    """Single shot measurement with medium repeatability and clock stretching enabled"""

    CMD_ID = 0x2c0d

    def pack(self):
        return self.tx_data.pack([])

    tx = TxData(CMD_ID, '>H', device_busy_delay=0.007, slave_address=None, ignore_ack=False)
    rx = RxData('>H')


class MeasureSingleShotLowRepeatability(Transfer):
    """Single shot measurement with low repeatability"""

    CMD_ID = 0x2416

    def pack(self):
        return self.tx_data.pack([])

    tx = TxData(CMD_ID, '>H', device_busy_delay=0.005, slave_address=None, ignore_ack=False)
    rx = RxData('>H')


class MeasureSingleShotLowRepeatabilityClockStretching(Transfer):
    """Single shot measurement with low repeatability and clock stretching enabled"""

    CMD_ID = 0x2c10

    def pack(self):
        return self.tx_data.pack([])

    tx = TxData(CMD_ID, '>H', device_busy_delay=0.005, slave_address=None, ignore_ack=False)
    rx = RxData('>H')


class StartMeasurement05MpsHighRepeatability(Transfer):
    """Start periodic measurement mode with 0.5 mps and high repeatability."""

    CMD_ID = 0x2032

    def pack(self):
        return self.tx_data.pack([])

    tx = TxData(CMD_ID, '>H', device_busy_delay=0.016, slave_address=None, ignore_ack=False)


class StartMeasurement05MpsMediumRepeatability(Transfer):
    """Start periodic measurement mode with 0.5 mps and medium repeatability."""

    CMD_ID = 0x2024

    def pack(self):
        return self.tx_data.pack([])

    tx = TxData(CMD_ID, '>H', device_busy_delay=0.007, slave_address=None, ignore_ack=False)


class StartMeasurement05MpsLowRepeatability(Transfer):
    """Start periodic measurement mode with 0.5 mps and low repeatability."""

    CMD_ID = 0x202f

    def pack(self):
        return self.tx_data.pack([])

    tx = TxData(CMD_ID, '>H', device_busy_delay=0.005, slave_address=None, ignore_ack=False)


class StartMeasurement1MpsHighRepeatability(Transfer):
    """Start periodic measurement mode with 1 mps and high repeatability."""

    CMD_ID = 0x2130

    def pack(self):
        return self.tx_data.pack([])

    tx = TxData(CMD_ID, '>H', device_busy_delay=0.016, slave_address=None, ignore_ack=False)


class StartMeasurement1MpsMediumRepeatability(Transfer):
    """Start periodic measurement mode with 1 mps and medium repeatability."""

    CMD_ID = 0x2126

    def pack(self):
        return self.tx_data.pack([])

    tx = TxData(CMD_ID, '>H', device_busy_delay=0.007, slave_address=None, ignore_ack=False)


class StartMeasurement1MpsLowRepeatability(Transfer):
    """Start periodic measurement mode with 1 mps and low repeatability."""

    CMD_ID = 0x212d

    def pack(self):
        return self.tx_data.pack([])

    tx = TxData(CMD_ID, '>H', device_busy_delay=0.005, slave_address=None, ignore_ack=False)


class StartMeasurement2MpsHighRepeatability(Transfer):
    """Start periodic measurement mode with 2 mps and high repeatability."""

    CMD_ID = 0x2236

    def pack(self):
        return self.tx_data.pack([])

    tx = TxData(CMD_ID, '>H', device_busy_delay=0.016, slave_address=None, ignore_ack=False)


class StartMeasurement2MpsMediumRepeatability(Transfer):
    """Start periodic measurement mode with 2 mps and medium repeatability."""

    CMD_ID = 0x2220

    def pack(self):
        return self.tx_data.pack([])

    tx = TxData(CMD_ID, '>H', device_busy_delay=0.007, slave_address=None, ignore_ack=False)


class StartMeasurement2MpsLowRepeatability(Transfer):
    """Start periodic measurement mode with 2 mps and low repeatability."""

    CMD_ID = 0x222b

    def pack(self):
        return self.tx_data.pack([])

    tx = TxData(CMD_ID, '>H', device_busy_delay=0.005, slave_address=None, ignore_ack=False)


class StartMeasurement4MpsHighRepeatability(Transfer):
    """Start periodic measurement mode with 4 mps and high repeatability."""

    CMD_ID = 0x2334

    def pack(self):
        return self.tx_data.pack([])

    tx = TxData(CMD_ID, '>H', device_busy_delay=0.016, slave_address=None, ignore_ack=False)


class StartMeasurement4MpsMediumRepeatability(Transfer):
    """Start periodic measurement mode with 4 mps and medium repeatability."""

    CMD_ID = 0x2322

    def pack(self):
        return self.tx_data.pack([])

    tx = TxData(CMD_ID, '>H', device_busy_delay=0.007, slave_address=None, ignore_ack=False)


class StartMeasurement4MpsLowRepeatability(Transfer):
    """Start periodic measurement mode with 4 mps and low repeatability."""

    CMD_ID = 0x2329

    def pack(self):
        return self.tx_data.pack([])

    tx = TxData(CMD_ID, '>H', device_busy_delay=0.005, slave_address=None, ignore_ack=False)


class StartMeasurement10MpsHighRepeatability(Transfer):
    """Start periodic measurement mode with 10 mps and high repeatability."""

    CMD_ID = 0x2737

    def pack(self):
        return self.tx_data.pack([])

    tx = TxData(CMD_ID, '>H', device_busy_delay=0.016, slave_address=None, ignore_ack=False)


class StartMeasurement10MpsMediumRepeatability(Transfer):
    """Start periodic measurement mode with 10 mps and medium repeatability."""

    CMD_ID = 0x2721

    def pack(self):
        return self.tx_data.pack([])

    tx = TxData(CMD_ID, '>H', device_busy_delay=0.007, slave_address=None, ignore_ack=False)


class StartMeasurement10MpsLowRepeatability(Transfer):
    """Start periodic measurement mode with 10 mps and low repeatability."""

    CMD_ID = 0x273a

    def pack(self):
        return self.tx_data.pack([])

    tx = TxData(CMD_ID, '>H', device_busy_delay=0.005, slave_address=None, ignore_ack=False)


class ReadMeasurement(Transfer):
    """Read out data after a "start measurement" command has been issued."""

    CMD_ID = 0xe000

    def pack(self):
        return self.tx_data.pack([])

    tx = TxData(CMD_ID, '>H')
    rx = RxData('>H')


class StopMeasurement(Transfer):
    """Stop the periodic measurement mode."""

    CMD_ID = 0x3093

    def pack(self):
        return self.tx_data.pack([])

    tx = TxData(CMD_ID, '>H', device_busy_delay=0.001, slave_address=None, ignore_ack=False)


class ReadStatusRegister(Transfer):
    """Read out the status register"""

    CMD_ID = 0xf32d

    def pack(self):
        return self.tx_data.pack([])

    tx = TxData(CMD_ID, '>H', device_busy_delay=0.01, slave_address=None, ignore_ack=False)
    rx = RxData('>H')


class ClearStatusRegister(Transfer):
    """Clear (set to zero) all flags (Bit 15, 10, 4) in the status register."""

    CMD_ID = 0x3041

    def pack(self):
        return self.tx_data.pack([])

    tx = TxData(CMD_ID, '>H', device_busy_delay=0.01, slave_address=None, ignore_ack=False)


class SoftReset(Transfer):
    """Perform a soft reset."""

    CMD_ID = 0x30a2

    def pack(self):
        return self.tx_data.pack([])

    tx = TxData(CMD_ID, '>H', device_busy_delay=0.002, slave_address=None, ignore_ack=False)


class StatusRegisterT(BitfieldContainer):
    write_data_checksum_status = BitField(offset=0, width=1)
    command_status = BitField(offset=1, width=1)
    system_reset_detected = BitField(offset=4, width=1)
    tracking_alert = BitField(offset=10, width=1)
    heater_status = BitField(offset=13, width=1)
    alert_pending_status = BitField(offset=15, width=1)


class Repeatability(Enum):
    LOW = 0
    MEDIUM = 1
    HIGH = 2

    def __int__(self):
        return self.value


class Mps(Enum):
    EVERY_TWO_SECONDS = 0
    ONE_PER_SECOND = 1
    TWO_PER_SECOND = 2
    FOUR_PER_SECOND = 4
    TEN_PER_SECOND = 10

    def __int__(self):
        return self.value
