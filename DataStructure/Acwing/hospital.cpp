#include <iostream>
#include <vector>

using namespace std;

// Function to calculate the maximum distance from a given hospital location to any other area
int calculateMaxDistance(const vector<vector<int>> &graph, int hospital)
{
    int maxDistance = 0;
    for (int i = 0; i < graph.size(); ++i)
    {
        if (i != hospital && graph[hospital][i] > maxDistance)
        {
            maxDistance = graph[hospital][i];
        }
    }
    return maxDistance;
}

// Function to find the best hospital location
int findHospitalLocation(const vector<vector<int>> &graph)
{
    int n = graph.size();
    int minMaxDistance = INT_MAX;
    int bestHospital = -1;

    // Iterate through each area to find the best hospital location
    for (int i = 0; i < n; ++i)
    {
        int maxDistance = calculateMaxDistance(graph, i);
        if (maxDistance < minMaxDistance)
        {
            minMaxDistance = maxDistance;
            bestHospital = i;
        }
    }

    return bestHospital;
}

int main()
{
    // Input graph representing distances between areas
    vector<vector<int>> graph = {
        {0, 3, 2, 5},
        {3, 0, 1, 6},
        {2, 1, 0, 4},
        {5, 6, 4, 0}};

    // Find the best hospital location
    int hospital = findHospitalLocation(graph);

    // Output the best hospital location
    cout << "The best location for the hospital is Area " << hospital + 1 << "." << endl;

    return 0;
}
