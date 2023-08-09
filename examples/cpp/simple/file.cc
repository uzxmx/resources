#include <iostream>
#include <fstream>

const std::string gen_filename(const char *ext) {
  time_t     now = time(0);
  struct tm  tstruct;
  char       buf[80];
  tstruct = *localtime(&now);
  strftime(buf, sizeof(buf), "%Y-%m-%d-%H-%M-%S", &tstruct);
  sprintf(buf, "%s%s", buf, ext);

  return buf;
}

int main() {
  auto filename = gen_filename(".txt");
  std::ofstream out(filename);
  out << "foo" << std::endl;
  out.close();
  std::cout << "Generated file: " << filename << std::endl;
  return 0;
}
