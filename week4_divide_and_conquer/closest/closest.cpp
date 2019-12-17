#include <algorithm>
#include <cmath>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <cfloat>

using std::min;
using std::pair;
using std::sqrt;
using std::string;
using std::vector;
// using namespace std;

class Point {
public:
  int x;
  int y;
  Point(int x, int y) {
    this->x = x;
    this->y = y;
  }
  double distance(const Point &b) {
    return sqrt((this->x - b.x) * (this->x - b.x) + (this->y - b.y) * (this->y - b.y));
  }
};

double naive_min(Point points[], int n) {
  double m = std::FLT_MAX;
  for (auto i = 0; i < n - 1; ++i) {
    for (auto j = i + 1; j < n; ++j) {
      auto d = points[i].distance(points[j]);
      if (d < m) {
        m = d;
      }
    }
  }
  return m;
}

double strip_min(vector<Point> points, int n, double m) {
  for (auto i = 0; i < n - 1; ++i) {
    for (auto j = i + 1; j < n && points[j].y - points[i].y < m; ++j) {
      auto d = points[i].distance(points[j]);
      if (d < m) {
        m = d;
      }
    }
  }
  return m;
}

double minimal_distance(vector<int> x, vector<int> y) {


  // write your code here
  return 0.;
}

int main() {
  // size_t n;
  // std::cin >> n;
  // vector<int> x(n);
  // vector<int> y(n);
  // for (size_t i = 0; i < n; i++) {
  //   std::cin >> x[i] >> y[i];
  // }
  // std::cout << std::fixed;
  // std::cout << std::setprecision(9) << minimal_distance(x, y) << "\n";

  Point p = Point(1, 2);
  std::cout << p.x << p.y;

  // return 0;
}
