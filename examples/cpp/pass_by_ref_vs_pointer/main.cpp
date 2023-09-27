#include <iostream>
#include <unistd.h>

using namespace std;

class Buffer {
public:
  enum Type {
    kSmall,
    kMedium,
    kLarge
  };

  Buffer(void *bytes, size_t len, Type type);
  void *GetBytes() const;
  size_t GetLen() const;
  void Print() const;

  static constexpr int defaultSize = 1024;

private:
  void *bytes;
  size_t len;
  Type type;
};

Buffer::Buffer(void *bytes, size_t len, Type type) : bytes(bytes), len(len), type(type) {}

void *Buffer::GetBytes() const {
  return this->bytes;
}

size_t Buffer::GetLen() const {
  return this->len;
}

void Buffer::Print() const {
  cout << "Print method called" << endl;
}

void printBuffer(Buffer &buf) {
  cout << "Buffer len by reference: " << buf.GetLen() << endl;
  buf.Print();
}

void printBuffer(Buffer *buf) {
  cout << "Buffer len by pointer: " << buf->GetLen() << endl;
  buf->Print();
}

int main() {
  Buffer buffer = Buffer(nullptr, 256, Buffer::kMedium);
  while (true) {
    printBuffer(buffer);
    printBuffer(&buffer);
    sleep(2);
  }
  return 0;
}
