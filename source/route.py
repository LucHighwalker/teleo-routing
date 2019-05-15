from binarytree import BinarySearchTree
import datetime


class RouteFinder(object):

    def __init__(self, file):
        self.routes = []
        with open(file, 'r') as f:
            contents = f.read().split()
            for content in contents:
                split = content.split(',')
                self.routes.append((split[0], split[1]))

        self.routes_tree = BinarySearchTree(self.routes)

    def find_best_route(self, number):
        return self._find_best_route_recursive(number)

    def _find_best_route_recursive(self, number):
        if number == '+':
            return None
        else:
            route = self.routes_tree.search(number)
            if route is not None:
                return route
            else:
                return self._find_best_route_recursive(number[:-1])

if __name__ == "__main__":
    print('generation scenario 1 and 2 classes...\n\n')
    router = RouteFinder('../data/route-costs-106000.txt')


    """Scenario 1: excluding class generation, < 0.0003 seconds"""

    print('scenario 1 starting search...\n')
    scene_1_search_start = datetime.datetime.now()
    print(router.find_best_route('+1537615345245'))
    scene_1_search_time = datetime.datetime.now() - scene_1_search_start
    print('scenario 1 search time: {}\n\n'.format(scene_1_search_time))


    """Scenario 2: get all the numbers to look up, and repeat scenario 1 for each number"""

    print('getting numbers for scenario 2...\n')

    with open('../data/phone-numbers-1000.txt', 'r') as f:
            numbers = f.read().split()

    print('scenario 2 starting search...\n')
    scene_2_search_start = datetime.datetime.now()
    results = ''
    for number in numbers:
        route = router.find_best_route(number)
        results = '{}{}: {}\n'.format(results, number, route)

    # print(results)

    scene_2_search_time = datetime.datetime.now() - scene_2_search_start
    print('scenario 2 search time: {}\n\n'.format(scene_2_search_time))
