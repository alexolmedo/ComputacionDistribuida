#include <stdio.h>
#include <omp.h>

//$ gcc 2017.11.06.hello.c -fopenmp -o hello

int main() {
    int tid;
    omp_set_thread_num(16);
    #pragma omp parallel
    {
        tid=omp_get_thread_num();
        printf("Hello from %d\n", tid);
    }
    return 0;
}
