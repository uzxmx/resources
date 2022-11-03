#include <stdio.h>
#include <stdlib.h>

static void static_say_hello() {
  printf("static_say_hello called\n");
}

void say_hello() {
  printf("say_hello called\n");
}

int main() {
  void *buf = malloc(10240);
  if (!buf) {
    printf("Failed to allocate memory.\n");
    return 1;
  }

  free(buf);

  say_hello();
  static_say_hello();
  return 0;
}
