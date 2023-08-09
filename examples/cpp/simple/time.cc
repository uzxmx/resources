#include <iostream>

// See http://en.cppreference.com/w/cpp/chrono/c/strftime
const std::string current_datetime() {
  time_t     now = time(0);
  struct tm  tstruct;
  char       buf[80];
  tstruct = *localtime(&now);
  strftime(buf, sizeof(buf), "%Y-%m-%d %H:%M:%S", &tstruct);

  return buf;
}

int main() {
  std::cout << "Time: " << current_datetime() << std::endl;
  return 0;
}
