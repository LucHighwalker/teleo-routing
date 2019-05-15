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
        if len(number) == 0:
            return None
        else:
            route = self.routes_tree.search(number)
            if route is not None:
                return route
            else:
                return self._find_best_route_recursive(number[:-1])

if __name__ == "__main__":
    """Scenario 1: excluding class generation, < 0.0003 seconds"""
    print('generation scenario 1 classes...')
    router_scene_1 = RouteFinder('../data/route-costs-106000.txt')
    print('scenario 1 starting search...')
    time_start = datetime.datetime.now()
    print(router_scene_1.find_best_route('+1537615345245'))
    search_time = datetime.datetime.now() - time_start
    print('scenario 1 search time: {}'.format(search_time))
