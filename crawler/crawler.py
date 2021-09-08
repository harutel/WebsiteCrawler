import sys
import yaml

def main():
    with open("./config.yaml", 'r') as configFile:
        defaultConfig = yaml.load(configFile, Loader=yaml.FullLoader)

    baseUrl = defaultConfig['global']['base_url']
    print("Crawling the website: " + baseUrl)


if __name__ == "__main__":
    main()
