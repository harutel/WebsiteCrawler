import sys
import yaml

class Crawler(object):
    def __init__(self):
        self.baseUrl = url

    def read_global_config(self):
        with open("./config.yaml", 'r') as configFile:
            defaultConfig = yaml.load(configFile, Loader=yaml.FullLoader)

        baseUrl = defaultConfig['global']['base_url']
        print("Crawling the website: " + baseUrl)

    def get_base_url(self):
        return(self.baseUrl)


def main():

    print(Crawler(baseUrl).get_base_url())


if __name__ == "__main__":
    main()
