class Logger:
    def __init__(self):
        print("Object Created")

    def __del__(self):
        print("Object Destroy")

if __name__ == "__main__":
   log = Logger()
   del log
        