#!/usr/bin/python3

from mn_wifi.net import Mininet_wifi
from mininet.node import Controller
from mn_wifi.node import OVSKernelAP
from mininet.link import TCLink
from mininet.log import setLogLevel, info
from mn_wifi.cli import CLI
import time

def move_cars(net, cars):
    """
    Simulates the movement of cars by updating their position in a loop.
    """
    # Define the total simulation time and update interval (in seconds)
    total_time = 30  # Total simulation time in seconds
    update_interval = 1  # Interval to update positions in seconds

    for t in range(total_time):
        info(f"*** Timestep {t+1}/{total_time} - Moving cars\n")
        for i, car in enumerate(cars):
            # Simulate movement by changing the car's x position
            x, y, z = car.params['position']
            new_x = x + 5  # Move 5 units in the x direction
            if new_x > 200:  # Reset position if out of bounds
                new_x = 50
            car.setPosition(f"{new_x},{y},{z}")
            info(f"*** Position of {car.name}: {car.params['position']}\n")
        
        # Update the network to recognize the new positions
        net.updateNodePos()
        
        # Pause for the update interval
        time.sleep(update_interval)

def topology():
    "Create a network."
    net = Mininet_wifi(
        controller=Controller,
        link=TCLink,
        accessPoint=OVSKernelAP
    )

    info("*** Creating nodes\n")
    
    # Add controller
    c1 = net.addController('c1')

    # Add and configure access points with specific parameters
    ap1 = net.addAccessPoint('ap1', 
                            ssid='RSU1',
                            mode='g',
                            channel='1',
                            position='50,50,0',
                            failMode='standalone',
                            range=100)
    
    ap2 = net.addAccessPoint('ap2',
                            ssid='RSU2',
                            mode='g',
                            channel='6',
                            position='150,50,0',
                            failMode='standalone',
                            range=100)

    # Add cars (stations)
    cars = []
    for i in range(5):
        car = net.addStation(
            name='car%d' % (i + 1),
            mac='00:00:00:00:00:%02d' % (i + 1),
            ip='10.0.0.%d/24' % (i + 1),
            position='%d,30,0' % (50 + i * 20),
            range=50
        )
        cars.append(car)

    info("*** Configuring wifi nodes\n")
    net.configureWifiNodes()

    info("*** Creating links\n")
    net.addLink(ap1, c1)
    net.addLink(ap2, c1)

    info("*** Starting network\n")
    net.build()
    c1.start()
    ap1.start([c1])
    ap2.start([c1])

    # Initial positions of nodes for verification
    for car in cars:
        info(f"*** Initial position of {car.name}: {car.params['position']}\n")
    info(f"*** Initial position of ap1: {ap1.position}\n")
    info(f"*** Initial position of ap2: {ap2.position}\n")

    # Run the car movement simulation
    move_cars(net, cars)

    info("*** Running CLI\n")
    CLI(net)

    info("*** Stopping network\n")
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    topology()
