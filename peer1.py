import pythonp2p
import time

class Mynode(pythonp2p.Node):
  def on_message(self, message, sender, private):
    # Gets called everytime there is a new message
    print(message)

 
node = Mynode(host='0.0.0.0', port=3000, file_port=65433)
node.setfiledir('./data')
filehash = node.addfile('./pic.png')
print(f'filehash {filehash}')
node.start()
print(f'id: {node.id}')


# count = 0

# while True:
#     count +=1
#     time.sleep(1)
#     print(f'counting...{count}')
#     node.send_message(f'count {count}')