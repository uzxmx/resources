#include <stdio.h>
#include <sys/ptrace.h>

int main() {
  if (ptrace(PTRACE_TRACEME, 0, 1, 0) == -1) {
    printf("Don't trace me!!\n");
    return 1;
  }
  printf("Normal execution\n");
  return 0;
}
