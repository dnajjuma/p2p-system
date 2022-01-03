import pythonp2p
import time

class Mynode(pythonp2p.Node):
  def on_message(message, sender, private):
    # Gets called everytime there is a new message
    print(message)

 
node = Mynode(host='127.0.0.1', port=2000, file_port=2001)
node.setfiledir('./data-2/')
node.start()

time.sleep(1)
node.connect_to(host='192.168.43.75', port=3000)
time.sleep(3)
node.requestFile('cb2ae6d780411406e10e1e781c209e0e')