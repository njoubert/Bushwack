# Marauder's Map

```WELCOME! THIS IS AN EXPERIMENTAL, UNTESTED, IN-PROGRESS PRE-ALPHA PROJECT! THAT BE DRAGONS AHEAD YET LADDY!```

```

  Marauder's Map is an exploration of building technology 
  that toes a fine line between two seemingly opposite ideals:

  One: Helping you find what you're looking for 
       "achieve your goals", one might say

  Two: Create a space for serendipidy, immediacy, and impromptu adventure 
       "discovering the unexpected", one might say.
```

<br/>

## Intetion: This is an Art Project

Marauder's Map is a project, not to quickly build out a product or produce new research results. The intent in creating this is to take part in the act of creation for aesthetic and exploration purposes. There are many pictures of mountains. I want to paint my own, not hang yours. 

In doing this, we'll learn a lot - new skills and a new appreciation for what others have produced. Once on-playa, we'll learn a lot about technology's relationship to people. Collecting this knowledge is the second intent of doing this project.

<br/>

## Some Terminology and Conventions

For our design process, we're borrowing terms from the US Government's Design Review System. "Mission Concept Review", "System Requirements Review", and "System Design Review" leading to a "Preliminary Design Review" and a "Critical Design Review". The first 3 we do upfront, once we have a preliminary design we do a PDR, and once we're ready to go to manufacturing, we do a CDR.

As for the actual manufactured artifact, we're using three main stages: Engineering Validation Test (EVT), Design Validation Test (DVT) and Production Validation Test (PVT). Initially we're just getting to a place where the functionality works. After that we become concerned with physical design and finally the artifact itself.


<br/>

## MCR - Mission Concept Review




*What is the need, objectives and concept for meeting said objectives?*

At large outdoor venues, such as Burning Man or ski resorts, it is easy to lose your friends, and difficult to locate them again. Often this is a *good* thing since it leads to serendipidous adventures and a forced relaxation of scheduling stress. Often, though, it's a source of stress and frustration. 

This project aims to make it possible to find your friends, while staying true to the principles of immediacy, serendipitously meeting people, and going on adventures together! 

This project consists of a cheap, self-contained person locator to help you find your friends and share points of interest. But it doesn't make it too easy!

- Everyone only gets a very limited set of points they can save - so everyone has their own Top 5 places!
- We only provide an approximate distance and direction to a friend, so it's an adventure to try and find them!
- The system might sometimes lie to you, who knows?

*Note: in many ways this revisits the ideas that originally went into my iPhone app [Burble](https://github.com/njoubert/UndergraduateProjects/tree/master/Burble/trunk)*

**Other Ideas**

- **Visual Component**  animating EL wire or the like as you get closer to a friend! Or letting you shoot lightrays to a person!
- **Lying?** - What if the system only gives you a true value part of the time? What if it deliberately lies?
- **Only works part of the time?** - What if you can't always use the system, you have to wait for it to become active?
- **Doesn't tell you which person you're walking towards**
- **Exchanging physical tokens to track people?** - What if your device comes with 10 little "chips" that represent your location, and you have to exchange them with other people so they can track you and you can track them?
- **A completely analog, physical UI?** - what if it had a big analog compass, an analog set of lights (or a simple multi-segment display), something with NO "screen"?


Design Idea:
- **Watch/Arm-mounted Bracelet** so it's hands free! 
- **Make it the LED/EL Wire driver**

<br/>

## SRR - System Requirements Review




*What is the functional and performance requirements for the system?*

This project needs to be:

- A completely homogenous, decentralized position reporting system.
- A mesh network where the typical communication scheme is NOT all-to-all, but might be.
- Stand-alone, with no dependency on wifi or cell signals.
- A small, cheap (ideally <$50) handheld device.
- Weather-resistant in dusty and extreme temperature environments.
- Resilient to power-cycling
- Support 20 to 50 people.
- Be as passive as possible: don't interfere with people's burn, it's not a cellphone.




<br/>

## SDR - System Design Review




*What is the proposed system architecture and design, and the flow of data through the system?*

Each unit has:

- Sensors:
  - a GPS for positioning
  - a compass for orientation
- User Interface:
  - a small OLED screen for information display
  - a few buttons for interaction
- Power
  - a rechargeable battery (most likely LiPo or Li-Ion)
  - a battery charging circuit
  - a power regulator and battery protection circuit
- Radio
  - long range (ideally 1.5 miles to cover entire Black Rock City diameter)
  - doesn't depend on pairing with another device (support one-to-many broadcast)
  - license-free spectrum
  - ~5kbps data rates
  - reasonable latency (<1s)




#### Suggested System Architecture


**Draft BoM Rev 1**

| Unit                    | Source        | Qty | Price  |
| ------------------------|---------------|-----|--------|
| RPi Zero                | ?             | 1   | $5     |
| SX1276 radio module     | Modtronix     | 1   | $13.46 |
| 0.96" OLED display      | ebay          | 1   | $5.99  |
| Neo-6M GPS w Compass    | ebay          | 1   | $13.60 |
| 4gb microSD card        | amazon        | 1   | $2.73  |
| ------------------------|---------------|-----|--------|
|                         |               |     | $40.88 |


** Small Embedded Computer **

*Raspberry Pi Zero as command center.*

[Specs:](http://www.raspberrypi-spy.co.uk/2015/11/introducing-the-raspberry-pi-zero/)

- Price: $5
- Fast: 1Ghz ARM1 Core (Same as Raspberry Pi 1, BCM2836), 512MB Ram, microSD card
- Low Power: 160mA power draw
- Tiny: 65mm x 30mm x 5mm, 9g
- [Good Peripherals](http://elinux.org/RPi_Low-level_peripherals): [SPI Bus](https://www.raspberrypi.org/documentation/hardware/raspberrypi/spi/README.md), two I2C buses, a Display Serial Interface connector, and HDMI out

*STM32 board*

[Specs](http://www.mouser.com/ProductDetail/STMicroelectronics/STM32VLDISCOVERY/?qs=%2fha2pyFaduipj54b2yiocvG8C3d30WMaeLqL6x14%252bec%3d)

- Price: $9.88

See all the [dev boards Mouser supplies here.](http://www.mouser.com/Embedded-Solutions/Engineering-Tools/Embedded-Development-Tools/Embedded-Processor-Development-Kits/Development-Boards-Kits-ARM/_/N-cxd2t/?Ns=Pricing|0)

**Displays**

OLED: 128x64 yellow and blue 0.96"[Amazon](http://www.amazon.com/gp/product/B00O2LLT30?keywords=arduino%20oled&qid=1451557496&ref_=sr_1_1&sr=8-1), [ebay](http://www.ebay.com/itm/3-5V-0-96-SPI-Serial-128X64-OLED-LCD-LED-Display-Module-for-Arduino-/171756285171?hash=item27fd78ecf3:g:facAAOSw~otWgkoi)

- Price: $5.99, $15
- SSD1306 SPI controller
- 8 lines of text, 22 characters wide (176 characters total)

[TFT: 160x128 full-color 1.8"](https://www.adafruit.com/products/358)

- Price: $20
- SPI

[LCD: Monochrome Nokia Display 84x48](https://www.adafruit.com/products/338)

- Price: $10
 
**Radio Modem**

[CC1101]/[CC1110](http://www.ti.com/tool/cc1110emk868-915)/[CS1111]() Radio Modem



[LoRa Modems: Semtech SX1272 and SX1276]()

- This uses a spread spectrum technique to significantly increase sensitivity (like GPS!)
- Useful Blog posts etc:
  - http://dangerousprototypes.com/2014/07/17/sx1278sx1276-rfm98wrfm96w-lora-module/
- Price: $13.46 [inAir9](http://modtronix.com/inair9.html) with expected range of [4km in urban environments](http://forum.modtronix.com/index.php?topic=2222.0)
- Price: $16 for [SX1278 board (433MHz)](https://www.tindie.com/products/DORJI_COM/long-range-semtech-lora-sx1276-sx1278-data-radio-modem-drf1278dm/)  or [SX1276 board (915MHz)](https://www.tindie.com/products/DORJI_COM/868mhz-lora-sx1276-data-radio-modem-drf1276dm/)
- [HopeRF implementation](http://www.hoperf.com/rf_transceiver/lora/)


[WirelessThings ARF](https://www.wirelessthings.net/arf-high-power-radio-transceiver)

- Price: $45
- CC1111 Radio Model Chip with LNA
- Claims tens of kilometers of range

**GPS Module**

[NavSpark-GL GPS/GLONASS Dev Board](https://navspark.mybigcommerce.com/navspark-gl-arduino-compatible-development-board-with-gps-glonass/)

- Price: $25 + $9 antenna = $34
- Arduino-compatible, hackable
- Very sensitive, GPS, GLONASS, SBAS, QZSS for amazing coverage, Venus 8 167 channel engine, 10Hz update, 2.5m CEP accuracy 
- 38mm x 18mm
- Serial and Serial-Over-USB IO

[AdaFruit Ultimate GPS Module](https://www.adafruit.com/products/746)

- Price: $40
- 15mm x 15mm x 4mm with patch antenna
- Built-in datalogging to flash memory
- Serial out
 
[UBlox Neo6 GPS Module on eBay](http://www.ebay.com/itm/Ublox-NEO-6M-GPS-Module-Aircraft-Flight-Controller-For-Arduino-MWC-IMU-APM2-/200911914297?hash=item2ec7488539:g:s7IAAOSwYHxWFgLf)

[uBlox Neo6M with Compass on eBay](http://www.ebay.com/itm/Ublox-neo-6M-GPS-Module-W-box-Built-in-Compass-for-PIX-Pixhawk-PX4-Autopilo-New-/281835342531?hash=item419eb20ac3:g:czYAAOSw~gRV0tSn)

- Price: $11 to $17
- 9600 baud serial out

**Power System**

Alkaline Batteries?

Rechargeable Battery Power?

Solar Power?




<br/>

## Resources and Inspiration


**Related Burning Man Projects:**

[Everything by Bunny Studios (Andrew Huang)](http://www.bunniestudios.com/blog/?tag=burning-man)
done as part of The Phage, including [Dr Brainlove Art Car](http://drbrainlove.tumblr.com/post/124592528476/brain-whisperers-aka-communicator-badges)



**System Design Inspiration:**

[Wolfgang Klerk's Arduino and Raspberry Pi Projects](https://wolfgangklenk.wordpress.com/) and his [SPI protocol driver for TI CC11001](https://github.com/wklenk/CC1101SocketDriver)

[Henry Hellam and co.'s Girl Tech IM-ME Hack for a previous Burn](https://github.com/henryhallam/puellaardens)

**Product Design Inspiration:**

[goTenna cellphone radio system](http://www.gotenna.com/index) and [teardown](https://learn.adafruit.com/gotenna-teardown/inside-gotenna)

[Teenage Engineering's PO-16 synth](https://www.teenageengineering.com/products/po)

[Lisa/S Autopilot](http://1bitsquared.com/collections/autopilots/products/lisa-s)

**Other Resources:**

[Design Review Cycle](https://en.wikipedia.org/wiki/Design_review_(U.S._government)#System_Requirements_Review_.28SRR.29)


<br/>

## Discarded System Designs (Dead Kittens)

**APRS-based system**

APRS radios are to expensive, too clunky, power hungry, and way too slow (<1kbps). Building my own from scratch is painful. APRS is also a notoriously inefficient use of spectrum: we should be able to push significantly higher throughput at the same power and range without using more spectrum.
