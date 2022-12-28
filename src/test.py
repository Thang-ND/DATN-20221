from crawler.store24h import Store24h


if __name__ == '__main__':
    test = Store24h("24hstore")
    try:
        test.crawl()
        test.saveDataToLocalFile()
    except Exception as e:
        print(e)
        pass