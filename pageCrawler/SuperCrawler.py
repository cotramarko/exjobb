import os
import imp


def call_minions():
    basepath = os.path.dirname(os.path.realpath(__file__))
    crawlers = [f for f in os.listdir() if f.endswith('exjobb.py')]
    #print(*crawlers, sep='\n')
    total_list_thesis = []
    for crawler in crawlers:

        module = imp.load_source(crawler[:-3], basepath + '/' + crawler)

        result = module.crawl()
        total_list_thesis += result

    print(total_list_thesis)

if __name__ == '__main__':
    call_minions()






