import pingmonitor

def main():
    config_file = "config.yaml"
    pingmonitor.start(config_file)

if __name__ == "__main__":
    main()
