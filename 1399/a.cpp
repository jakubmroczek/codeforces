#include <algorithm>
#include <iostream>
#include <vector>

template<typename T>
T read() {
  T t;
  std::cin >> t;
  return t;
}

auto read_vector(int length) {
  std::vector<int> vector;
  while (length-- != 0) {
    vector.push_back(read<int>());
  }
  return vector;
}

bool solve(std::vector<int>&& vector) {
  std::sort(vector.begin(), vector.end());
  for (size_t i = 0; i < vector.size() - 1; i++) {
    const int a = vector[i];
    const int b = vector[i + 1];
    if ((b - a) > 1) {
      return false;
    }
  }

  return true;
}

int main(int argc, char const *argv[]) {
  auto tests_number = read<int>();

  while (tests_number-- != 0) {
    auto vector_length = read<int>();
    auto vector = read_vector(vector_length);
    const auto solution = solve(std::move(vector));

    if (solution == true) {
      std::cout << "YES" << std::endl;
    } else {
      std::cout << "NO" << std::endl;
    }

  }

  return 0;
}
