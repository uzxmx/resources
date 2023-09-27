#include <assert.h>
#include <stdbool.h>
#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <sys/sysctl.h>
#include <sys/ptrace.h>
#include <unistd.h>

void check_debugger_attached() {
  int                 junk;
  int                 mib[4];
  struct kinfo_proc   info;
  size_t              size;

  info.kp_proc.p_flag = 0;
  int flag = P_TRACED;
  printf("flag: %d", flag);
  // 0x00000800
  // 0x00005806

  mib[0] = CTL_KERN;
  mib[1] = KERN_PROC;
  mib[2] = KERN_PROC_PID;
  mib[3] = getpid();

  size = sizeof(info);
  junk = sysctl(mib, sizeof(mib) / sizeof(*mib), &info, &size, NULL, 0);
  assert(junk == 0);


  if ((info.kp_proc.p_flag & P_TRACED) != 0) {
    printf("Debugger is attached.\n");
  } else {
    printf("Debugger is not attached.\n");
  }
  printf("%x\n", info.kp_proc.p_flag);
}

int main() {
  check_debugger_attached();
  printf("%x\n", PT_ATTACH);
  ptrace(PT_DENY_ATTACH, 0, 0, 0);
  return 0;
}
