# Copyright (C) 2015 Niels Joubert
# Contact: Niels Joubert <njoubert@gmail.com>
#

# Following https://learn.adafruit.com/adafruit-ft232h-breakout/spi



import Adafruit_GPIO.FT232H as FT232H
from LoRa import *
import binascii

import logging, sys, time


class SX1276(object):
  '''
  Class to manage SX1276 radio
  '''
  def __init__(self, spi):
    self._log = logging.getLogger('MaraudersMap.SX1276')
    self._spi = spi
    self._log.debug("SX1276 Created")


def log_to_stdout(level=1):
  h1 = logging.StreamHandler(sys.stdout)
  log = logging.getLogger('MaraudersMap.SX1276')
  log.addHandler(h1)
  log.setLevel(level)


def print_temp(radio):
  ''' LET'S TRY TO READ THE TEMPERATURE SENSOR!! Only available in FSK/OOK Mode? '''
  # Here's the sequence (P89 from http://www.semtech.com/images/datasheet/sx1276_77_78_79.pdf)

  radio.rx_chain_calibration()

  # 1) Set device to Standby, wait for oscillator startup
  radio.set_mode(MODE.SLEEP)

  # 2) Set the device to FSRx mode (or should this be standby??)
  radio.set_mode(MODE.FSRX)

  # 3) set TempMonitorOff=0
  # set register IMAGE_CAL lowest bit to 0
  image_cal = (radio.get_register(REG.FSK.IMAGE_CAL))
  image_cal = image_cal & 0xFE
  radio.set_register(REG.FSK.IMAGE_CAL, image_cal)

  # 4) Wait for 140 microseconds
  time.sleep(0.1)

  # 5) Set TempMonitorOff=1
  image_cal = (radio.get_register(REG.FSK.IMAGE_CAL)) | 0x01
  radio.set_register(REG.FSK.IMAGE_CAL, image_cal)

  # 6) Set device back to Sleep mode
  radio.set_mode(MODE.SLEEP)

  # 7) Access temperature value in RegTemp (0x3C)
  val = radio.get_register(0x3C)
  print val

def transmit(radio, msg="PING"):

  max_len = radio.get_max_payload_length()
  # Truncate to maximum payload size
  # TODO: Loop to support longer messages
  msg = msg[:max_len]

  msg_ = map(ord, msg)
  radio.set_mode(MODE.STDBY)
  radio.set_pa_config(pa_select=0)
  radio.set_payload_length(len(msg_))
  radio.write_payload(msg_)
  radio.set_mode(MODE.TX)

  # Wait for tx_done
  while radio.get_irq_flags()['tx_done'] != 1:
      time.sleep(0.1)

  # Clear all IRQ flags
  radio.spi.transfer([REG.LORA.IRQ_FLAGS | 0x80, 0xFF])[1]

  radio.set_mode(MODE.STDBY)

def receive_loop(radio):
  radio.reset_ptr_rx()
  radio.set_max_payload_length(255)

  try:
    while True:
      radio.set_mode(MODE.RXCONT)

      time.sleep(0.1)

      flags = radio.get_irq_flags()
      if flags['rx_done']:
        payload = radio.read_payload(nocheck=True)
        if payload is not None:
          print "Received: ", payload
        else:
          print "I thought I received, but I couldn't extract message"
        # Clear the IRQs        
        radio.spi.transfer([REG.LORA.IRQ_FLAGS | 0x80, 0xFF])[1]

        
  except KeyboardInterrupt:
    return

def receive(radio):
  radio.reset_ptr_rx()
  radio.set_mode(MODE.RXCONT)

  print "Waiting 2 seconds for receive..."
  time.sleep(2.0)

  #radio.set_mode(MODE.STDBY)

  print radio.get_irq_flags()

  payload = radio.read_payload(nocheck=True)
  if payload is not None:
    print "Received: ", payload
  else:
    print "Nothing Receveived"


def main():
  log_to_stdout()

  FT232H.use_FT232H()
  ft232h = FT232H.FT232H()

  # Create a SPI interface from the FT232H using pin 8 (C0) as chip select.
  # Use a clock speed of 3mhz, SPI mode 0, and most significant bit first.
  spi = FT232H.SPI(ft232h, cs=8, max_speed_hz=3000000, mode=0, bitorder=FT232H.MSBFIRST)


  radio = LoRa(spi=spi, verbose=False)
  radio.set_freq(915)

  print radio

  a = raw_input("Transmit [T], Ping [P] or Receive [R]? ")

  if a == "P":
    try:
      while True:
        msg = "Ping: " + time.asctime()
        print msg
        transmit(radio, msg)
        time.sleep(1)
    except KeyboardInterrupt:
      pass
  elif a == "T":
    try:
      while True:
        msg = raw_input("Message:")
        transmit(radio, msg=msg)
    except KeyboardInterrupt:
      pass
  elif a == "R":
    receive_loop(radio)
  else:
    print "Unknown command:", a

if __name__ == "__main__":
  main()




# # Write three bytes (0x01, 0x02, 0x03) out using the SPI protocol.
# spi.write([0x01, 0x02, 0x03])

# # Read 3 bytes of data using the SPI protocol.
# response = spi.read(3)
# print 'Received {0}'.format(response)

# # Write 3 bytes and simultaneously read 3 bytes using the SPI protocl.
# response = spi.transfer([0x01, 0x02, 0x03])
# print 'Received {0}'.format(response)
