"""
Math problem: find the number of connected components in a graph

Leetcode story:
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b,
and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly
connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.
Example 1:

Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
"""

from typing import List


def find_circle_num(is_connected: List[List[int]]) -> int:
    points_visited = set()
    num_provinces = 0
    # for each point...
    for i in range(len(is_connected)):
        # if this point is not already part of a province...
        if i not in points_visited:
            # get all the points that could be visited from that point, and add them to the total of points visited
            points_visited = get_points_part_of_cohort(is_connected=is_connected, point=i,
                                                       points_visited=points_visited)
            # add a cohort (the one that point belongs to)
            num_provinces += 1
    return num_provinces


def get_points_part_of_cohort(is_connected: List[List[int]], point: int, points_visited):
    """ Should return all points that are visitable from that given point """
    points_visited.add(point)  # if we start from this point, then we have visited it...
    # for every point that we can to from this point...
    for i in range(len(is_connected)):
        if is_connected[point][i]:  # we can go to point i from here
            # if this point was not already visited (i.e. we don't want the algorithm to do back and forth between
            # points...)
            if i not in points_visited:
                # start over from that point, thinking that we may go to even further places from that point
                get_points_part_of_cohort(is_connected=is_connected, point=i, points_visited=points_visited)
    return points_visited
