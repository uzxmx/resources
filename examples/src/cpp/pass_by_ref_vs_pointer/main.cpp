#include <iostream>
#include <unistd.h>

using namespace std;

class Buffer {
public:
  Buffer(void *bytes, size_t len);
  void *GetBytes() const;
  size_t GetLen() const;

private:
  void *bytes;
  size_t len;
};

Buffer::Buffer(void *bytes, size_t len) : bytes(bytes), len(len) {}

void *Buffer::GetBytes() const {
  return this->bytes;
}

size_t Buffer::GetLen() const {
  return this->len;
}

void printBuffer(Buffer &buf) {
  cout << "Buffer len by reference: " << buf.GetLen() << endl;
}

void printBuffer(Buffer *buf) {
  cout << "Buffer len by pointer: " << buf->GetLen() << endl;
}

int main() {
  Buffer buffer = Buffer(nullptr, 256);
  while (true) {
    printBuffer(buffer);
    printBuffer(&buffer);
    sleep(2);
  }
  return 0;
}
